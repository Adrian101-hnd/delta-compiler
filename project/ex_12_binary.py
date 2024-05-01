# Author: A01752067 Adrian Bravo Lopez
from delta import Compiler, Phase


source = '#b010101'


# source2 = source[2:]

# print(source2)

# counter = 0
# value = 1
# print(source2)
# for char in source2[::-1]:
#             if(char == '1'):
#                 counter = counter + value
#             value = value * 2
# print(counter)

c = Compiler('program')
c.realize(source)
print()
#print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)