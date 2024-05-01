# Author: A01752067 Adrian Bravo Lopez
from arpeggio import PTNodeVisitor


class SemanticMistake(Exception):

    def __init__(self, message):
        super().__init__(f'Semantic error: {message}')


class SemanticVisitor(PTNodeVisitor):

    RESERVED_WORDS = ['true', 'false', 'var',
                      'if', 'else', 'while', 'do']

    def __init__(self, parser, **kwargs):
        super().__init__(**kwargs)
        self.__parser = parser
        self.__symbol_table = []

    def position(self, node):
        return self.__parser.pos_to_linecol(node.position)

    @property
    def symbol_table(self):
        return self.__symbol_table

    def visit_decimal(self, node, children):
        value = int(node.value)
        if value >= 2 ** 31:
            raise SemanticMistake(
                'Out of range decimal integer literal at position '
                f'{self.position(node)} => { value }'
            )

    def visit_decl_variable(self, node, children):
        name = node.value
        if name in SemanticVisitor.RESERVED_WORDS:
            raise SemanticMistake(
                'Reserved word not allowed as variable name at position '
                f'{self.position(node)} => {name}'
            )
        if name in self.__symbol_table:
            raise SemanticMistake(
                'Duplicate variable declaration at position '
                f'{self.position(node)} => {name}'
            )
        self.__symbol_table.append(name)

    def visit_lhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Assignment to undeclared variable at position '
                f'{self.position(node)} => {name}'
            )

    def visit_rhs_variable(self, node, children):
        name = node.value
        if name not in self.__symbol_table:
            raise SemanticMistake(
                'Undeclared variable reference at position '
                f'{self.position(node)} => {name}'
            )
        
    #Changes to help the compiler notice overflows in the int values
    
    def visit_binary(self,node,children):
        decimal = int(node.value[2:], 2)
        if decimal < 0 or decimal >= 2 ** 31:
            raise SemanticMistake(
                f'Integer literal out of range at position {self.position(node)} => {decimal}'
            )
    def visit_octal(self,node,children):
        decimal = int(node.value[2:], 8)
        if decimal < 0 or decimal >= 2 ** 31:
            raise SemanticMistake(
                f'Integer literal out of range at position {self.position(node)} => {decimal}'
            )
    def visit_hexadecimal(self,node,children):
        decimal = int(node.value[2:], 16)
        if decimal < 0 or decimal >= 2 ** 31:
            raise SemanticMistake(
                f'Integer literal out of range at position {self.position(node)} => {decimal}'
            )
