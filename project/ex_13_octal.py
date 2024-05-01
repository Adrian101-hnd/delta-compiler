# Author: A01752067 Adrian Bravo Lopez
from delta import Compiler, Phase


source = '#o123765'


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