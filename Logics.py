from Memory import memory


class logic:

    def clearAll(x):
        memory.dis1 = '0'
        memory.operator = '@'
        memory.input = True
        memory.atm = 0
        memory.total = 0
        memory.n1 = 0
        memory.n2 = 0
        memory.result = False
        memory.answer = 0

    def solve(x):
        if x == '+':
            memory.answer = memory.n1 + memory.n2
        elif x == '-':
            memory.answer = memory.n1 - memory.n2
        elif x == 'x':
            if memory.n1 == 0:
                memory.answer = 0
            elif memory.n2 == 0:
                memory.answer = 0
            else:
                memory.answer = memory.n1 * memory.n2
        elif x == '/':
            if memory.n2 == 0:
                memory.answer = 'invalid'
            else:
                memory.answer = memory.n1 / memory.n2
        else:
            return

    def ca():
        memory.dis1 = '0'
        memory.operator = '@'
        memory.input = False
        memory.total = 0
        memory.n1 = 0
        memory.n2 = 0
        memory.result = False
        memory.answer = 0


