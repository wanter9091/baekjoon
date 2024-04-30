n=int(input())
s_input=[input() for _ in range(n)]

use = []
alpha = [0] * 91  #65~90
num = [0] * 10
res=0


def use_check(s):  #사용하는 단어의 알파뱃이 use에 없다면 추가한다 순서는 신경안씀
    for c in s:
        if ord(c) not in use:
            use.append(ord(c))

def alpha_sum():
    for s in s_input:
        l=len(s)-1
        for c in s:
            if l>-1:
                alpha[ord(c)]+=10**l
            l-=1

def use_sort():
    for i in range(len(use)-1):#4라면 0~2
        for j in range(len(use)-1-i):
            if alpha[use[j]]>alpha[use[j+1]]:
                box=use[j]
                use[j]=use[j+1]
                use[j+1]=box

checked_s_input=""
for s in s_input:
    checked_s_input+=s

use_check(checked_s_input)
alpha_sum()
use_sort()

for i in range()

for i in use:
    print(str(i)+" "+str(alpha[i]))

"""

4 3 2 1 길이가4라면 0~2 0~1 0
3421
3241
3214
2314
2134
2134


"""