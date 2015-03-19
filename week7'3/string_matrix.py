def join(delimiter, items):
    string=delimiter
    for i in range(0,len(items)):
        string += str(items[i])
        string += delimiter
    return string

def string_matrix(matrix_width, strings):
    lel=""
    for string in strings:
        if len(string)>matrix_width:
            lel += join("|",string[: matrix_width])
        elif len(string)<matrix_width:
            while len(string)!=matrix_width:
                string+="X"
            lel += join("|",string)
        else:
            lel += join("|",string)
        lel+="\n"
    return lel
            
