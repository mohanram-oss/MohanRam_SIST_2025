def solve(s):
    idx = 0
    for i in range(len(s)):
        if s[i] == " ":
            idx = i
            break
    a = s[:i].title()
    b = s[i+1:].title()
    return a+" "+b
res = solve("hello world")
print(res)
