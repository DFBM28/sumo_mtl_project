# This code monitors the behavior of a vehicle at an intersection using MTL specifications.
# It checks if the vehicle respects the red light and if it crosses the intersection within a certain time.

import rtamt, sys

# Define MTL Specification for safety
spec1 = rtamt.StlDiscreteTimeSpecification()

# Declare variables for safety
spec1.declare_var('inIntersection', 'float')
spec1.declare_var('redLight', 'float')
spec1.declare_var('greenLight', 'float')

# Define constraints
# Safety: Vehicle should not enter when light is red 
spec1.spec = "(redLight -> not inIntersection)"

# Define MTL Specification for efficiency
spec2 = rtamt.StlDiscreteTimeSpecification()
# Declare variables for efficiency
spec2.declare_var('inIntersection', 'float')

# Efficiency: Vehicle should cross the intersection within 10 seconds
spec2.spec = "(inIntersection until[0,10](not inIntersection))"

try:
    spec1.parse()
    spec1.pastify()
    spec2.parse()
    spec2.pastify()
except rtamt.RTAMTException as e:
    print(f"Parse error: {e}")
    sys.exit()
