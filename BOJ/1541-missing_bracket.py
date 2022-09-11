def isPlus(num):
    return num >= 0


def isPlusOp(op):
    return op == '+'


exp = input()
numberList = []
opList = []

nowNumber = ""

for e in exp:
    if (e.isdigit()):
        nowNumber += e
    else:
        opList.append(e)
        numberList.append(int(nowNumber))
        nowNumber = ""

numberList.append(int(nowNumber))

i = 0

while (i < len(opList)):
    if (opList[i] == '+'):
        numberList[i] += numberList[i + 1]
        del opList[i]
        del numberList[i + 1]
    else:
        i += 1

i = 0
while (i < len(opList)):
    if (opList[i] == '-'):
        numberList[i] -= numberList[i + 1]
        del opList[i]
        del numberList[i + 1]
    else:
        i += 1

print(numberList[0])
