# Autonomous Vehicle Simulation with SUMO
This project simulates an autonomous vehicle (a.v.) in a traffic environment using the Simulation of Urban MObility (SUMO) tool. The simulation includes different speed modes and max speeds for the autonomous vehicle, and checks if it respects the red light and crosses the intersection within a specific time. The system also evaluates whether the vehicle adheres to predefined Metric Temporal Logic (MTL) specifications.

## Features
- MTL Specifications Monitoring: The script uses MTL formulas to monitor traffic rule violations such as running a red light and crossing the intersection within a time limit.

- Dynamic Vehicle Speed Control: The autonomous vehicle can be controlled by setting different speed modes and maximum speeds, simulating real-world conditions.

- Adding Other Vehicles: The simulation allows other vehicles to join the traffic, adding realism to the scenario.

- Logging Violations: Any violations of the MTL specifications are logged in a file for further analysis.

## Installation
### Prerequisites
Before running this project, ensure you have the following tools installed:

- SUMO (Simulation of Urban MObility)

    - Follow the installation instructions at SUMO's website.

- Python 3.x

    - Install Python from python.org.

- Required Python Libraries

  - traci (SUMO's TraCI API for Python)

  - mtl_monitor (for handling MTL specifications)

To install the required libraries, run the following command:
```python
pip install traci
pip install rtamt
```
Make sure SUMO is properly installed and the sumo-gui.exe and sumo.exe binaries are accessible in your environment.

## Usage
### Running the Simulation
The script allows you to control whether to run the simulation with or without the SUMO GUI. You can also configure the speed mode and the maximum speed of the autonomous vehicle.

### Speed Modes and Configuration
You can configure the autonomous vehicle’s behavior by adjusting the speed mode and maximum speed.

- Speed Modes:

    - `0`: Ignore traffic rules.

    - `1`: Respect speed limits.

    - `31`: Respect all traffic rules.

- Max Speed:

    - You can specify the maximum speed for the autonomous vehicle in meters per second. If not set, it will run with default speed limits.

The simulation will run for 5000 steps, checking for traffic rule violations and logging any violations in a text file named according to the speed mode and maximum speed settings.

## Code Structure
- run.py: The main script to run the simulation. It configures SUMO, controls the autonomous vehicle, checks for MTL specification violations, and logs any violations.

- mtl_monitor.py: Contains the MTL specifications used in the simulation to monitor the behavior of the autonomous vehicle.

## Contributing
Feel free to fork the repository and submit pull requests. If you find any bugs or have suggestions, open an issue in the repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- SUMO: The Simulation of Urban MObility (SUMO) is a powerful tool for simulating urban transportation.

- MTL: Metric Temporal Logic (MTL) is used for specifying and monitoring temporal properties in real-time systems.

## Contact
Barbosa Monteiro Diogo - monteiro@cl.uni-heidelberg.de