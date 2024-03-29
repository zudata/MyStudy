# 5086
import sys
inputs = sys.stdin.readline
while True:
    a, b = map(int, inputs().split())
    if a == b == 0: break
    elif b%a == 0: print('factor')
    elif a%b == 0: print('multiple')
    else: print('neither')

# 1037
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
l.sort()
print(l[0]*l[n-1])

# 2609
import sys
inputs = sys.stdin.readline
a, b = map(int, inputs().split())
d = 2; res = 1
while a >= d and b >= d:
    if a%d == 0 and b%d == 0:
        a = a/d; b = b/d
        res = res*d
    else: d += 1
print(res)
print(int(res*a*b))

# 1934
import sys
inputs = sys.stdin.readline
def lc(x, y):
    r = x%y
    if r == 0: return y
    else: return lc(y, r)
for i in range(int(inputs())):
    a, b = map(int, inputs().split())
    l = lc(a, b)
    print((a//l)*(b//l)*l)

# 2981
import sys, math
inputs = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def gcd_N(arr): # N개의 최대공약수
    gcdi = arr[0]
    for i in arr:
        gcdi = gcd(gcdi, i)
    return gcdi
n = int(inputs())
l = [int(inputs()) for i in range(n)]
ll = min(l); l.remove(ll); res = []
for j in range(n-1):
    l[j] -= ll
gcv = gcd_N(l); res.append(gcv)
if gcv == 4:
    res.append(2)
else:
    for k in range(2, int(math.sqrt(gcv))+1):
        if math.isclose(gcv%k, 0):
            if k not in res: res.append(k)
            if gcv//k not in res: res.append(gcv//k)
# 시간 복잡도를 줄이기 위해 약수를 구할 때 해당 수의 제곱근까지만 반복하면 된다.
for p in range(len(res)):
    pp = min(res); res.remove(pp)
    print(pp, end = ' ')

# 3036
import sys
inputs = sys.stdin.readline
def lc(x, y):
    r = x%y
    if r == 0: return y
    else: return lc(y, r)
n = int(inputs())
l = list(map(int, inputs().split()))
lv = l.pop(0)
for i in l:
    lcv = lc(lv, i)
    print(f"{int(lv/lcv)}/{int(i/lcv)}")

# 11050
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
res = n
for i in range(1, n):
    res *= i
for j in range(1, k+1):
    res /= j
for l in range(1, n-k+1):
    res/= l
print(int(res))

# 11051
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
up = 1; under = 1
for i in range(1, k+1):
    up *= n-i+1
    under *= i
res = int(up//under)%10007
print(res)

# 1010
import sys
inputs = sys.stdin.readline
t = int(inputs())
for i in range(t):
    n, m = map(int, inputs().split())
    up = 1; under = 1
    for j in range(1, n+1):
        up *= m-j+1
        under *= j
    print(int(up//under))

# 9375
import sys
inputs = sys.stdin.readline
items = {}
for i in range(int(inputs())):
    items.clear()
    for j in range(int(inputs())):
        k, s = map(str, inputs().split())
        if s in items: items[s] += 1
        else: items[s] = 2
    res = 1
    for value in items.values():
        res *= value
    print(res-1)

# 1676
import sys
inputs = sys.stdin.readline
n = int(inputs())
for i in range(1, n):
    n *= i
n = str(n); res = 0
for j in range(len(n)-1, 0, -1):
    if n[j] == '0': res += 1
    else: break
print(res)

# 2004
import sys
inputs = sys.stdin.readline
def div(x, y):
    c = 0
    while y <= x:
        x //= y
        c += x
    return c
n, m = map(int, inputs().split())
up2 = div(n, 2); up5 = div(n, 5)
un2 = div(m, 2) + div(n-m, 2)
un5 = div(m, 5) + div(n-m, 5)
print(min(up2 - un2, up5 - un5))

# 13241
import sys
inputs = sys.stdin.readline
a, b = map(int, inputs().split())
if a == b: print(a)
else:
    check = False; res = a*b; tmp = a
    while True:
        tmp += a
        if tmp % b == 0:
            check = True
            break
        if tmp == res: break
    if check == False: print(res)
    else: print(tmp)

# 1735
import sys
inputs = sys.stdin.readline
a1, b1 = map(int, inputs().split())
a2, b2 = map(int, inputs().split())
c = a1*b2 + b1*a2; d = b1*b2
a = max(c, d); b = min(c, d)
while a % b != 0:
    ans = a%b; a = b; b = ans
if b == 1: print(f'{c} {d}')
else: print(f'{c//b} {d//b}')

# 2485
import sys
inputs = sys.stdin.readline
def fungcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
n = int(inputs())
gaps = []; tree = [int(inputs()) for _ in range(n)]
for i in range(1, n):
    gaps.append(tree[i] - tree[i-1])
gset = list(set(gaps)); gcd = gset[0]; res = 0
for i in range(1, len(gset)):
    gcd = fungcd(gcd, gset[i])
for gap in gaps:
    res += gap//gcd - 1
print(res)

# 4134
import sys
inputs = sys.stdin.readline
def check(x):
    if x == 0 or x == 1: return False
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0: return False
    return True
for _ in range(int(inputs())):
    n = int(inputs())
    while True:
        if check(n):
            print(n)
            break
        n += 1

# 17103
import sys
inputs = sys.stdin.readline
t = int(inputs())
m = 1000000; arr = [1 for _ in range(m+1)]; l = []
for i in range(2, m + 1):
    if arr[i]:
        l.append(i)
        for j in range(i*2, m+1, i):
            if j > m: break
            arr[j] = 0
for _ in range(t):
    n = int(inputs())
    res = 0
    for i in l:
        if n - i < i: break
        if arr[n-i]: res += 1
    print(res)