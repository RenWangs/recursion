# 回文字符串
def ispalindrome(s):
    if len(s) <=1: return True
    else: return s[0] == s[-1] and ispalindrome(s[1:-1])

def ispalindrome1(s,indent):
    print(indent,"ispalindrome1调用",s)
    if len(s) <= 1:
        print(indent,"准备从基础情况返回true")
        return True
    else:
        ans = s[0] == s[-1] and ispalindrome1(s[1:-1],indent + indent)
        print(indent, "准备返回",ans)

print(ispalindrome("abccba"))

'''this id github learnning'''