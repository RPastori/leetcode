def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    temp = ""
    for c in s:
        if c not in temp:
            temp += c
            d[len(temp)] = temp
        else:
            temp = temp[temp.index(c)+1:] + c
    if d:
        return max(d)
    else:
        return 0
