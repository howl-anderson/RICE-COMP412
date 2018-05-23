from Record import Record, RecordList
from Operand import Operand
from Operator import Operator


class Parser:
    def __init__(self, src_file):
        self.src = src_file

    def parse(self) -> RecordList:
        record_list = RecordList()

        with open(self.src) as fd:
            for line in fd.readlines():
                line = line.replace('=>', ' ')
                line = line.replace(',', ' ')

                operator, *operand = line.split()
                if operator.startswith("//"):
                    # this is comment line
                    continue

                # remove inline comment
                i = 0
                for i, _ in enumerate(operand):
                    op = operand[i]
                    if op == '//':
                        break
                operand = operand[:i+1]

                if operator in Operator.NOP_OPERATOR:
                    record_list.append(
                        Record(Operator(operator))
                    )
                elif operator in Operator.UNARY_OPERATOR:
                    record_list.append(
                        Record(Operator(operator),
                               Operand(operand[0]))
                    )
                elif operator in Operator.BINARY_OPERATOR:
                    if len(operand) != 2:
                        raise ValueError("invalid operand: {}".format(operand))

                    record_list.append(
                        Record(Operator(operator),
                               operand_one=Operand(operand[0]),
                               operand_three=Operand(operand[1]))
                    )
                elif operator in Operator.TRIPLE_OPERATOR:
                    record_list.append(
                        Record(Operator(operator),
                               Operand(operand[0]),
                               Operand(operand[1]),
                               Operand(operand[2]))
                    )
                else:
                    raise ValueError("invalid operator: {}".format(operator))

        return record_list
