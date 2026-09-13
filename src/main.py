"""
Checks if the conveyor belt can carry the packages based on motor count and total weight.
"""

MOTOR_CAPACITY = 12

### YOUR CODE HERE

motor_count = int(input("How many motors are carrying the packages?"))
print(motor_count)
total_package_weight = int(input("How many kg of packages do we expect?"))
print(total_package_weight)

if total_package_weight <= motor_count*MOTOR_CAPACITY:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")
