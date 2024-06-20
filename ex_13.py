import math
radius_inside = float(input('Введите радиус слепой зоны:'))
radius_outside = float(input('Введите радиус дальности приема:'))
print(abs(math.pi*(radius_outside**2 - radius_inside**2)))
