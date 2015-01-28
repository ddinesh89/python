def palindrome(s) :
    def covertToChars(s) :
        s = s.lower()
        ans = ''
        for c in s :
            if c in 'abcdefghijklmnopqrstuvwxyz' :
                ans = ans + c
        return ans
        
    
    def isPalindrome(s) :
        if len(s) <= 1 :
            return True
        else :
            return s[0] == s[-1] and isPalindrome(s[1:-1])
    
    return isPalindrome(covertToChars(s))
    