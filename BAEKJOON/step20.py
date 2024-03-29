# 10828
import sys
inputs = sys.stdin.readline
def push(x):
    stack.append(x)
def pop():
    if len(stack) == 0: return -1
    else: return stack.pop()
def size():
    return len(stack)
def empty():
    if stack: return 0
    else: return 1
def top():
    if stack: return stack[-1]
    else: return -1

n = int(inputs())
stack = []
for i in range(n):
    l = inputs().split()  # 입력값을 띄어쓰기 기준으로 나눔
    order = l[0]  # 입력값의 명령어
    if order == "push": push(l[1])
    elif order == "pop": print(pop())
    elif order == "size": print(size())
    elif order == "empty": print(empty())
    elif order == "top": print(top())

# 10773
import sys
inputs = sys.stdin.readline
k = int(inputs())
l = []
for _ in range(k):
    n = int(inputs())
    if n == 0: l.pop()
    else: l.append(n)
print(sum(l))

# 9012
import sys
inputs = sys.stdin.readline
t = int(inputs())
for _ in range(t):
    s = inputs().strip()
    while s.find('()') != -1:
        s = s.replace('()', '')
    if len(s) == 0:
        print('YES')
    else: print('NO')

# 4949
while True:
    ss = ''; s = input()
    if s == '.': break
    else:
        for i in s:
            if i == '(' or i == ')' or i == '[' or i == ']':
                ss += i
        while (ss.find('()') != -1) or (ss.find('[]') != -1):
            ss = ss.replace('()', '')
            ss = ss.replace('[]', '')
        if len(ss) == 0:
            print('yes')
        else: print('no')

# 1874
import sys
inputs = sys.stdin.readline
n = int(inputs())
stack = []; res = []; c = 1; test = 0
for _ in range(n):
    num = int(inputs())
    while c <= num:
        stack.append(c)
        res.append('+')
        c += 1
    if stack.pop() != num: test = 1
    else: res.append('-')
if test == 1: print('NO')
else: print('\n'.join(res))