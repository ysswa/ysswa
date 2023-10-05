#importing built-in library math
import math
#printing pie value
pie_value=math.pi
print(f"value of pie is: {pie_value}")

#printing square root of an integer
integer=int(input("enter an integer value"))
sq_value=math.sqrt(integer)
print(f"sqare root of an integer value  is: {sq_value}")

#rounding a number using ceil(),floor() functions
above_value=math.ceil(199999.55)
print(f"after rounding the value is: {above_value}")

below_value=math.floor(199999.55)
print(f"after rounding the value is: {below_value}")

#conversion of degrees to radians and vice versa
degrees_value=int(input("enter degrees value"))
radians_value=math.radians(degrees_value)
print(f"value of radians is: {radians_value}")

radians_value=int(input("enter radians value"))
degree_value=math.degrees(radians_value)
print(f"value in degrees is: {degrees_value}")
