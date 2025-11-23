// Time Complexity: O(n)
// Space Complexity: O(n)
#include <iostream>
#include <vector>
#include <deque>
#include <climits>
using namespace std;

struct Line {
    long long m, c;
    
    long long eval(long long x) const {
        return m * x + c;
    }
    
    double intersect_x(const Line& other) const {
        if (m == other.m) {
            return c >= other.c ? 1e18 : -1e18;
        }
        return (double)(other.c - c) / (m - other.m);
    }
};

bool is_bad(const Line& l1, const Line& l2, const Line& l3) {
    return l1.intersect_x(l3) <= l1.intersect_x(l2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<long long> steps(n), complexities(n);
    for (int i = 0; i < n; i++) {
        cin >> steps[i] >> complexities[i];
    }
    
    vector<long long> dp(n, LLONG_MAX);
    dp[0] = 0;
    
    deque<Line> hull;
    
    auto add_line = [&](Line line) {
        while (hull.size() >= 2 && is_bad(hull[hull.size()-2], hull[hull.size()-1], line)) {
            hull.pop_back();
        }
        hull.push_back(line);
    };
    
    auto query = [&](long long x) -> long long {
        while (hull.size() >= 2 && hull[0].eval(x) >= hull[1].eval(x)) {
            hull.pop_front();
        }
        return hull.empty() ? LLONG_MAX : hull[0].eval(x);
    };
    
    add_line({complexities[0], dp[0]});
    
    for (int i = 1; i < n; i++) {
        dp[i] = query(steps[i]);
        add_line({complexities[i], dp[i]});
    }
    
    cout << dp[n - 1] << endl;
    
    return 0;
}
