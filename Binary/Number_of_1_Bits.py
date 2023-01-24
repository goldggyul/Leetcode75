class Solution:
    # 파이썬은 32비트여도 long으로 넘어가고,
    # 자바에선 상위 비트가 1이면 2의 보수로 음수로 처리되는 듯하다
    # 근데 파이썬엔 zero fill right shift가 없는듯? 어차피 long으로 넘어가서 그런가
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += n & 1
            n >>= 1
        return ans


"""Java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        while (n != 0) {
            ans += n & 1;
            n >>>= 1;
        }
        return ans;
    }
}
"""


"""Kotlin

class Solution {
    // you need treat n as an unsigned value
    fun hammingWeight(n:Int):Int {
        var n = n
        var ans = 0
        while(n != 0){
            ans += n and 1
            n = n ushr 1
        }
        return ans
    }
}

"""