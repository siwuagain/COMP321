// Time Complexity: O(n)
// Space Complexity: O(n)
package COMP321.problemskeleton_Problem32.submissions.accepted;

import java.util.*;
import java.io.*;

public class accepted {
    static class Line {
        long m, c;
        
        Line(long m, long c) {
            this.m = m;
            this.c = c;
        }
        
        long eval(long x) {
            return m * x + c;
        }
        
        double intersectX(Line other) {
            if (m == other.m) {
                return c >= other.c ? Double.POSITIVE_INFINITY : Double.NEGATIVE_INFINITY;
            }
            return (double)(other.c - c) / (m - other.m);
        }
    }
    
    static boolean isBad(Line l1, Line l2, Line l3) {
        return l1.intersectX(l3) <= l1.intersectX(l2);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        
        long[] steps = new long[n];
        long[] complexities = new long[n];
        
        for (int i = 0; i < n; i++) {
            String[] parts = br.readLine().split(" ");
            steps[i] = Long.parseLong(parts[0]);
            complexities[i] = Long.parseLong(parts[1]);
        }
        
        long[] dp = new long[n];
        Arrays.fill(dp, Long.MAX_VALUE);
        dp[0] = 0;
        
        ArrayDeque<Line> hull = new ArrayDeque<>();
        
        hull.addLast(new Line(complexities[0], dp[0]));
        
        for (int i = 1; i < n; i++) {
            while (hull.size() >= 2) {
                Line[] arr = hull.toArray(new Line[0]);
                if (arr[0].eval(steps[i]) >= arr[1].eval(steps[i])) {
                    hull.pollFirst();
                } else {
                    break;
                }
            }
            
            if (!hull.isEmpty()) {
                dp[i] = hull.peekFirst().eval(steps[i]);
            }
            
            Line newLine = new Line(complexities[i], dp[i]);
            while (hull.size() >= 2) {
                Line last = hull.pollLast();
                Line secondLast = hull.peekLast();
                if (isBad(secondLast, last, newLine)) {
                    // Keep polling
                } else {
                    hull.addLast(last);
                    break;
                }
            }
            hull.addLast(newLine);
        }
        
        System.out.println(dp[n - 1]);
    }
}
