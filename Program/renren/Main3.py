mapp = [[True for i in range(1010)] for j in range(1010)]
root = [0 for i in range(1010)]
count = [0 for i in range(1010)]


def findRoot(x):
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root[x])


def merge(x, y):
    root[findRoot(x)] = findRoot(y)


def completeGraph():
    T = int(input())
    while (T):
        n, m = map(int, input().split())
        for i in range(m):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            mapp[x][y] = mapp[y][x] = False
        m = n * (n - 1) / 2 - m
        for i in range(n - 1):
            for j in range(i + 1, n):
                if mapp[i][j]:
                    merge(i, j)
        for i in range(n):
            count[i] = 0
        for i in range(n):
            count[findRoot(i)] += 1
        total = 0
        for i in range(n):
            total += count[i] * (count[i] - 1) // 2
        print('Yes' if total == m else 'No')
        T -= 1


completeGraph()
