n = int(input())
p = list(input().split())

first_list = ""
second_list = ""
num = [0] * 10


def check(one, two, c):
    if c == "<":
        return one < two
    else:
        return one > two


def q02529(depth, s):
    global first_list, second_list

    if len(s) == n + 1:
        if first_list == "":
            first_list = s
            return
        else:
            second_list = s
            return

    for i in range(10):
        if not num[i]:
            if depth == 0 or check(int(s[-1]), i, p[depth - 1]):
                num[i] = True
                q02529(depth + 1, s + str(i))
                num[i] = False


q02529(0, "")
print(second_list)
print(first_list)
