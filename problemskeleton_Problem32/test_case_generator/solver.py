# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

def solve_for_output(lines):
    it = iter(lines)
    n = int(next(it))

    steps = []
    complexities = []
    for _ in range(n):
        s, c = map(int, next(it).split())
        steps.append(s)
        complexities.append(c)

    dp = [float('inf')] * n
    dp[0] = 0

    class Line:
        def __init__(self, m, c):
            self.m = m 
            self.c = c  
        
        def eval(self, x):
            return self.m * x + self.c
        
        def intersect_x(self, other):
            if self.m == other.m:
                return float('inf') if self.c >= other.c else float('-inf')
            return (other.c - self.c) / (self.m - other.m)

    hull = deque()

    def is_bad(l1, l2, l3):
        return l1.intersect_x(l3) <= l1.intersect_x(l2)

    def add_line(line):
        while len(hull) >= 2 and is_bad(hull[-2], hull[-1], line):
            hull.pop()
        hull.append(line)

    def query(x):
        while len(hull) >= 2 and hull[0].eval(x) >= hull[1].eval(x):
            hull.popleft()
        return hull[0].eval(x) if hull else float('inf')

    add_line(Line(complexities[0], dp[0]))

    for i in range(1, n):
        dp[i] = query(steps[i])
        add_line(Line(complexities[i], dp[i]))

    return int(dp[-1])
