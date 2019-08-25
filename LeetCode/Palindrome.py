class Solution:
    def longestPalindrome(self, s):
        if s :  #setup the default max_str,as 0 index
            max_str_len = 1
            max_str = s[0]
        else:
            return ""


        for i in range(len(s)):
            str_odd,len_odd   = self.aroundCenter(s,i,i)
            str_even,len_even = self.aroundCenter(s,i,i+1)
            #print(str_odd)
            #print(len_odd)
            str_sub  = str_odd if len_odd>len_even else str_even
            if len(str_sub) > max_str_len:
                max_str_len = len(str_sub)
                max_str = str_sub

        return max_str



    def aroundCenter(self,s,left,right):
        size = len(s)
        while left >= 0  and right < size and s[left] == s[right]:
            left  -= 1
            right += 1
        #print("left={}  right = {}".format(left,right))
        return s[left+1:right],(right-1)-(left+1) +1   #

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    target = 6
    result = s.longestPalindrome("abcba")
    print(result)
