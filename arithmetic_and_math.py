import math
w = 5.099
print(f"Pi Value: {math.pi}")
print(f"e Value: {math.e}")
sqrt = math.sqrt(w)
print(f"Square Root: {sqrt}")
ceil = math.ceil(w)
print(f"Ceil: {ceil}")
floor = math.floor(w)
print(f"floor: {floor}")

###############################################################

friends = 10
print(f"The current number of your friends is: {friends}")

#Augmented assignments
# friends = friends + 1 --> friends += 1
# friends = friends - 1 --> friends -= 1
# friends = friends * 1 --> friends *= 1
# friends = friends / 1 --> friends /= 1
# friends = friends ** 1 --> friends **= 1
# modulo
remainder = friends % 3
print(f"Remainder: {remainder}")

x = 3.54
y = -5
z = 7
result = round(x)
print(f"Round off: {result}")
absolute = abs(y)
print(f"Absolute Value: {absolute}")
power = pow(5, 5)
print(f"Power: {power}")
max = max(x, y, z)
print(f"The highest value above all three is: {max}")