from delta import Compiler, Phase


source = '''

var x, y;
                            x = 1;
                            y = 0;
                            do {
                                x = x - 1;
                                y = 1;
                            } while x;
                            x + y
'''

c = Compiler('program')
c.realize(source)
print()
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)