s = "()[]{}"
'''
先进后出，栈
'''
def isValid(s: str):

    if len(s) % 2 != 0:
        return False
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1



result = isValid(s)
print(result)
