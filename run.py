# This script runs the simulation with different speed modes and max speeds for the autonomous vehicle (a.v.) in the SUMO simulation environment.
# It uses the TraCI API to control the simulation and monitor the behavior of the a.v. using MTL specifications.
# It checks if the a.v. respects the red light and if it crosses the intersection within a certain time.
# It also adds other vehicles to the simulation and checks for violations of the MTL specifications.
# It logs any violations to a file.
# The script can be run with different speed modes and max speeds to test the behavior of the a.v. under different conditions.

import traci
import mtl_monitor

sumoBinary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"
sumoCmd = ["sumo-gui", "-c", "cross.sumocfg"] # Path to the SUMO configuration file
sumoCmd_no_gui = ["sumo", "-c", "cross.sumocfg"] # Path to the SUMO configuration file without GUI

spec1 = mtl_monitor.spec1
spec2 = mtl_monitor.spec2

def run(speed_mode, max_speed=None):
    traci.start(sumoCmd_no_gui)  # Start the SUMO simulation without GUI, change to sumoCmd for GUI
    step = 0
    av_id = "av"  # ID of the autonomous vehicle

    while step < 5000: # Check if simulation is running
        traci.simulationStep()  # Step the simulation
        step += 1

        # Check if the autonomous vehicle is in the simulation
        if av_id not in traci.vehicle.getIDList():
            # Add the autonomous vehicle to the simulation
            try:
                traci.vehicle.add(vehID=av_id, routeID="circle", typeID="autonomous", depart="now")
            
            except traci.exceptions.TraCIException:
                pass

        if av_id in traci.vehicle.getIDList():
            if max_speed is not None:
                traci.vehicle.setSpeed(vehID=av_id, speed=max_speed)  # Set max speed
                
            traci.vehicle.setSpeedMode(vehID=av_id, speedMode=speed_mode)  # Set speed mode 

            # Get the traffic light state of the lane of the a.v.
            traffic_state = traci.trafficlight.getRedYellowGreenState("0")[0]
            
            x, y = traci.vehicle.getPosition(av_id)  # Get the position of the vehicle
            in_intersection = (502.8 <= x <= 517.2) and (502.8 <= y <= 517.2)  # Check if the vehicle is in the intersection
            red_light = traffic_state == "r"    # Check if the light is red
            green_light = traffic_state == "G"  # Check if the light is green
            
            rob = spec1.update(step, [("inIntersection", 1.0 if in_intersection == True else 0.0),
                                     ("redLight", 1.0 if red_light == True else 0.0),
                                     ("green_light", 1.0 if green_light else 0.0),
            ])

            rob2 = spec2.update(step, [("inIntersection", 1.0 if in_intersection == True else 0.0)])

            # Check MTL constraint satisfaction
            if rob < 0:
                with open(f"speedMode{speed_mode}_maxSpeed{max_speed}.txt", "a") as f:
                    
                    f.write(f"Violation of red light rule at step {step}: {rob}\n")
                print(f"Violation of red light rule at step {step}!")

            if rob2 < 0:
                with open(f"speedMode{speed_mode}_maxSpeed{max_speed}.txt", "a") as f:
                    f.write(f"Violation of efficiency rule at step {step}: {rob2}\n")
                print(f"Violation of efficiency rule at step {step}!")    
            
        if step % 25 == 0:  # Add vehicles every 25 steps
                try:
                    traci.vehicle.add(vehID=f"WE_id_{step}", routeID="right", typeID="typeWE", depart=str(step))
                    traci.vehicle.add(vehID=f"EW_id{step}", routeID="left", typeID="typeEW", depart=str(step))
                except traci.exceptions.TraCIException:
                    pass

    traci.close()  # Close the simulation


if __name__ == "__main__":
    run(speed_mode=31) # Set speed mode to 31 (respect all traffic rules) 
    run(speed_mode=1)  # Set speed mode to 1 (respect speed limits)
    run(speed_mode=0)  # Set speed mode to 0 (ignore everything)
    run(speed_mode=31, max_speed=1) # Set speed mode to 31 (respect all traffic rules) and max speed to 1 m/s
    run(speed_mode=0, max_speed=1)  # Set speed mode to 0 (ignore everything) and max speed to 1 m/s