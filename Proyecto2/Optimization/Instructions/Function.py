from Optimization.C3DInstruction import *

class Function(C3DInstruction):

    def __init__(self, instr, id, line, column):
        C3DInstruction.__init__(self, line, column)
        self.instr = instr
        self.id = id
    
    def getCode(self):
        ret = f'func {self.id}(){{\n'
        for ins in self.instr:
            auxText = ins.getCode()
            if(auxText == ''):
                continue
            ret = ret + f'\t{auxText}'
            if ins.isLeader:
                ret = ret + "\t\t\t\t\t\t\t// Lider"
            ret = ret + "\n"
        ret = ret + '}'
        return ret