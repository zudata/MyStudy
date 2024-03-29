# 24479
import sys
inputs = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]; path = []; res = [0]*(n+1); tmp = [-1]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in range(1, len(graph)):
    graph[i].sort()
def algorithm(x):
    tmp[x] = 1
    path.append(x)
    for i in graph[x]:
        if tmp[i] == -1: algorithm(i)
    return
algorithm(r)
for idx, node in zip(range(1, len(path)+1), path):
    res[node] = idx
print(*res[1:], sep = '\n')

# 24480
import sys
inputs = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1); tmp = 1
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph:
    i.sort(reverse = True)
def algorithm(v):
    global tmp
    res[v] = tmp
    for i in graph[v]:
        if res[i]: continue
        tmp += 1
        algorithm(i)
algorithm(r)
print(*res[1:], sep = '\n')

# 24444
import sys
from collections import deque
inputs = sys.stdin.readline
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph: 
    i.sort()
def algorithm(v):
    cnt = 1
    queue = deque([v])
    res[v] = cnt 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if res[i] == 0:
                cnt += 1
                queue.append(i)
                res[i] = cnt 
algorithm(r)
print(*res[1:], sep = '\n')

# 24445
import sys
from collections import deque
inputs = sys.stdin.readline
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph: 
    i.sort(reverse = True)
def algorithm(v):
    cnt = 1
    queue = deque([v])
    res[v] = cnt 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if res[i] == 0:
                cnt += 1
                queue.append(i)
                res[i] = cnt 
algorithm(r)
print(*res[1:], sep = '\n')

# 2606
import sys
from collections import deque
inputs = sys.stdin.readline
n = int(inputs())
m = int(inputs())
l = [[] for _ in range(n+1)]
res = [0]*(n+1)
for _ in range(m):
    a, b = map(int, inputs().split())
    l[a].append(b); l[b].append(a)
def algorithm(v):
    queue = deque([v])
    res[v] = 1
    while queue:
        t = queue.popleft()
        for i in l[t]:
            if not res[i]:
                queue.append(i)
                res[i] = 1
algorithm(1)
print(sum(res) - 1)

# 1260
import sys
from collections import deque
inputs = sys.stdin.readline
n, m, v = map(int, inputs().split())
l = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, inputs().split())
    l[x-1].append(y-1)
    l[y-1].append(x-1)
for d in l:
    d.sort(reverse = True)
def dfs(v):
    seen = [0]*n
    stack = [v]
    while stack:
        v = stack.pop()
        if not seen[v]:
            seen[v] = 1
            print(v+1, end=' ')
            stack += l[v]
def bfs(v):
    seen = [0]*n
    tmp = deque([v])
    seen[v] = 1
    while tmp:
        v = tmp.popleft()
        print(v+1, end = ' ')
        for d in reversed(l[v]):
            if not seen[d]:
                tmp.append(d)
                seen[d] = 1
dfs(v-1); print(); bfs(v-1)

# 2667
import sys
from collections import deque
inputs = sys.stdin.readline
n = int(inputs())
arr = [inputs().strip() for _ in range(n)]
visited = [[0]*n for _ in range(n)]
res = 0; l = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(i, j):
    global res, tmp
    visited[i][j] = 1
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if x >= 0 and x < n and y >= 0 and y < n:
            if arr[x][y] == '1' and visited[x][y] == 0:
                tmp += 1
                dfs(x, y)
    return
for i in range(n):
    for j in range(n):
        tmp = 1
        if arr[i][j] == '1' and visited[i][j] == 0:
            dfs(i,j)
            res += 1
            l.append(tmp)
print(res); l.sort(); print(*l, sep = '\n')