str = '4433555555666096667775553'

def decode(str):
    decoder = [[' '], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], 
               ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], 
               ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    skip = 0
    str = str + '  ' # pad the end to prevent buffer overflow
    out = ''
    for i, c in enumerate(str):
        count = 0
        if c == ' ':    # lots of gross branching code but it works
            continue    # TODO: change it later
        if skip > 0:
            skip -= 1
            continue
        if str[i+1] == c: 
            count += 1
            if str[i+2] == c:
                count += 1
        x = int(c)
        out += decoder[x][count]
        skip = count
    return out

print(decode(str))