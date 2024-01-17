
def reverse_polish_notation(tokens):

    operators = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "/": lambda x, y: int(x/y),
        "*": lambda x, y: x*y
    }
    result = []

    for i in tokens: 
        
        if i in operators: 
            y =result.pop()
            x = result.pop()
            operand = operators[i](x,y)
            result.append(operand)

        else: 
            result.append(int(i))

    return result[0]


tokens = ["18"]
result = reverse_polish_notation(tokens)
print(result)

