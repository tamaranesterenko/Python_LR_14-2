#Вариант №12
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import fractions

f_one = fractions.Fraction(3, 5)
f_two = fractions.Fraction(4, 9)

print('{} + {} = {}'.format(f_one, f_two, f_one + f_two))
print('{} - {} = {}'.format(f_one, f_two, f_one - f_two))
print('{} * {} = {}'.format(f_one, f_two, f_one * f_two))

if f_one > f_two:
    print('{} > {}'.format(f_one, f_two))
else:
    print('{} < {}'.format(f_one, f_two))
