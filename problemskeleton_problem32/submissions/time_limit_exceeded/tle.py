# Time complexity: O(n^2)
n = int(input())
steps = []
complexities = []
for i in range(n):
    s, c = map(int, input().split())
    steps.append(s)
    complexities.append(c)

dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        cost = dp[j] + (complexities[j] * steps[i])
        dp[i] = min(dp[i], cost)
print(int(dp[n - 1]))
