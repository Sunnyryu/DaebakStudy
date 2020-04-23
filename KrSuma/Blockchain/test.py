# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self._temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("getting value")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value
#
#
# temp = Celsius(10)
#
# print(temp.temperature)
#
# temp.temperature = 15
#
# print(temp.temperature)



from hashlib import sha256
x = 5
y = 0

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y+=1
print(f'The solution is y = {y}')

hash(5*21)