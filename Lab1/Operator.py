class Operator:
    NOP_OPERATOR = ['nop']
    UNARY_OPERATOR = ['output']
    BINARY_OPERATOR = ['load', 'store', 'loadI']
    TRIPLE_OPERATOR = ['add', 'sub', 'mult', 'lshift', 'rshift']

    SIDE_EFFECT_OPERATOR = ['loadI', 'load', 'mult', 'add']

    CONSTANT_OPERATOR = ['loadI']

    OPERATORS = ['nop','output','load','store','loadI','add','sub', 'mult', 'lshift', 'rshift']

    def __init__(self, name: str):
        if name not in self.OPERATORS:
            raise ValueError("Name {} not in operator list {}".format(name,self.OPERATORS))

        self.name = name