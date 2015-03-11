def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result

def str_reverse(string):
    result=""

    for ch in range(len(string)-1, -1, -1):
        result += string[ch]
    return result
        
def join(delimiter, items):
    string=""
    for i in range(0,len(items)-1):
        string += str(items[i])
        string += delimiter
    string += str(items[len(items)-1])
    return string

def startswith(search, string):
    starts=False
    n=string[:len(search)]
    if n==search:
        starts=True
    return starts

def endswith(search, string):
    ends=False
    n=string[len(string)-len(search):]
    if n==search:
        ends=True
    return ends

def trim(string):
    
    for i in range(0,len(string)):
        if string[i]!=" ":
            break
    for j in range(len(string)-1, -1,-1):
        if string[j]!=" ":
            break
    return string[i:j+1]
