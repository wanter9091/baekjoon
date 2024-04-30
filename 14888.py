#곱하기만 뒤로 남겨서 써보자

n = int(input())
n_input = list(map(int, input().split()))
op_input = list(map(int, input().split()))
op_val = ['+', '-', '*', '/']

count = op_input[0] + op_input[1] + op_input[2]+ op_input[3]  #곱하기를 제외한 연산횟수

val=[]

def cal(op):
    start = n_input[0]
    for i in range(count):
        if op[i] == '+':
            start += n_input[i + 1]
        elif op[i] == '-':
            start -= n_input[i + 1]
        elif op[i] == '*':
            start *= n_input[i + 1]
        elif op[i] == '/':
            start = int(start/n_input[i + 1])

    return start


def q14888(depth, op):
    if depth == count:  #곱하기를 제외한 연산자를 전부 썼다면
        val.append(cal(op))
        return

    for i in range(4):
        if op_input[i] > 0:
            op_input[i] -= 1
            q14888(depth + 1, op + op_val[i])
            op_input[i] += 1


q14888(0,"")
print(max(val))
print(min(val))