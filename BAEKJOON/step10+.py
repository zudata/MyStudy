# 24262
print(1); print(0)

# 24263
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n); print(1)

# 24264
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n**2); print(2)

# 24265
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n*(n-1)//2); print(2)

# 24266
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n**3); print(3)

# 24267
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n*(n-1)*(n-2)//6); print(3)

# 24313
import sys
inputs = sys.stdin.readline
a1, a2 = map(int, inputs().split())
c = int(inputs())
n = int(inputs())
if c >= a1 and a1*n+a2 <= c*n:
    print(1)
else: print(0)