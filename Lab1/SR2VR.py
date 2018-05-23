from Record import RecordList
from Operator import Operator


class SR2VR:
    SIDE_EFFECT_OPERATOR = ['loadI', 'load', 'mult', 'add']

    def __init__(self, record_list: RecordList):
        self.record_list = record_list
        self.sr2vr = {}

    def construct(self):
        for i in reversed(range(len(self.record_list))):
            record = self.record_list[i]

            if record.operator.name in Operator.SIDE_EFFECT_OPERATOR:
                record.operand_three.VR = self.sr2vr[record.operand_three.SR]

                operator_list = (record.operand_one, record.operand_three)
                if record.operator.name in Operator.CONSTANT_OPERATOR:
                    operator_list = (record.operand_three, )

                for op in operator_list:
                    if op.SR.startswith('r'):
                        if op.SR not in self.sr2vr:
                            self.sr2vr.update(
                                {op.SR: Item(lu=i)}
                            )
                        op.VR = self.sr2vr[op.SR]
            else:
                for op in (record.operand_one, record.operand_two, record.operand_three):
                    if op is None:
                        continue

                    # this is constant
                    if op.SR.isnumeric():
                        continue

                    # this is a register
                    if op.SR.startswith('r'):
                        if op.SR not in self.sr2vr:
                            self.sr2vr.update(
                                {op.SR: Item(lu=i)}
                            )
                        op.VR = self.sr2vr[op.SR]


class Item:
    counter = 0

    def __init__(self, vr=None, lu=None):
        if vr is None:
            vr = ''.join(['vr', str(self.counter)])
        self.vr = vr

        self.lu = lu
