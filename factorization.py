def factorize(equation):
    result = ""
    i = 0
    length = len(equation)

    while i < length:
        if i + 2 < length and equation[i + 1] == '*' and equation[i + 2] == '*':
            variable = equation[i]
            exponent_start = i + 3
            
            exponent_end = exponent_start
            while exponent_end < length and equation[exponent_end].isdigit():
                exponent_end += 1
            
            exponent = int(equation[exponent_start:exponent_end])
            
            result += '*'.join([variable] * exponent)
            
            i = exponent_end
        else:
            result += equation[i]
            i += 1

    return result

#input1 = "a**4=16"
#print(factorize(input1))