from sys import stdin
# Greedy approach is wrong
n = int(input())
steps = []
complexities = []
for i in range(n):
    s, c = map(int, input().split())
    steps.append(s)
    complexities.append(c)

print(steps[n - 1] * complexities[0])