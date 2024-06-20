distance = float(input('Введите расстояние в сантиметрах:'))
print(f'{distance/(3*12*2.54)} ярдов', f'{distance/(1760*3*12*2.54)} мили',
      f'{distance/(12*2.54)} футов', f'{distance/2.54} дюймов', sep='\n')
