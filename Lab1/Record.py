from Operand import Operand
from Operator import Operator


class Record:
    def __init__(self, operator: Operator, operand_one: Operand =None, operand_two: Operand =None,
                 operand_three: Operand=None):
        self.operator = operator
        self.operand_one = operand_one
        self.operand_two = operand_two
        self.operand_three = operand_three


class RecordList(list):
    def generate_vr_code(self):
        pass
