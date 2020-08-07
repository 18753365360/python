def longestCommonPrefix(s):
    'Written by myself'
    if not s:
        return ""
    str0 = min(s)

    str1 = max(s)

    for i in range(len(str0)):
        if str0[i] != str1[i]:
            return str0[:i]
    return str0
    'Answer'
    ans = ''
    for i in zip(*s):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans
    print(zip(*s))

result = longestCommonPrefix(["alower","awhtrht","alighthrth"])
# print(result)
