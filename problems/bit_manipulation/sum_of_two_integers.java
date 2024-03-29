// ecommended to solve this in Java in the interview. This solution will not work in Python.
// https://leetcode.com/problems/sum-of-two-integers/
//
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int answer = a ^ b;
            int carry = (a & b) << 1;
            a = answer;
            b = carry;
        }

        return a;
    }
}