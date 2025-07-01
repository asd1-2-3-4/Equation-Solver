def add_multiplication(text):
    result = []
    for i, char in enumerate(text):
        if char.isalpha() or char.isdigit():
            if result and (result[-1].isalpha() or result[-1].isdigit()):
                if not (result[-1].isdigit() and char.isdigit()):
                    result.append('*')
            result.append(char)
        elif char == '(':
            if result and (result[-1].isalpha() or result[-1].isdigit()):
                result.append('*')
            result.append(char)

        elif char == ')':
            result.append(char)
            
            if i + 1 < len(text) and (text[i + 1].isalpha() or text[i + 1].isdigit()):
                result.append('*')
            if i + 1 < len(text) and text[i + 1] == '(':
                if result and (result[-1] == ')'):
                    result.append('*')
        else:
            result.append(char)

    return ''.join(result)


#print(add_multiplication("20x(1d+1)(30a*b)()()"))

