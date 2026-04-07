"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

def calc(raw_expression):
    tokens = tokenize(raw_expression)
    postfix = postfix_notation(tokens)
    return postfix

def tokenize(expression):
    tokens = []
    current_number = ""
    i = 0
    
    while i < len(expression):
        char = expression[i]
        
        if char.isdigit():
            current_number = char
            i += 1
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                current_number += expression[i]
                i += 1

            if current_number.count('.') > 1:
                return None
            tokens.append(('number', float(current_number)))
            current_number = ""
            continue
        
        elif char in '+-*/':
            tokens.append(('operator', char))
        
        elif char in '()':
            tokens.append(('parenthesis', char))
        
        elif char == '.':

            current_number = "0."
            i += 1
            while i < len(expression) and expression[i].isdigit():
                current_number += expression[i]
                i += 1
            tokens.append(('number', float(current_number)))
            current_number = ""
            continue
        
        else:
            return None  
        
        i += 1
    
    return tokens


def postfix_notation(tokens):
    stack = []
    queue = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        char = token[1]
        if isinstance(char, (int, float)):
            queue.append(char)
        elif char in '+-*/':
            while stack and (priority[stack[-1]] >= priority[char]):
            #while not (stack[-1] in low_priority and char in high_priority):
                queue.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char ==')':
            if stack:
                while stack[-1] != '(':
                    queue.append(stack[-1]) 
            stack.pop()
        else:
            while len(stack) > 0:
                if stack[-1] == '(':
                    return None
                queue.append(stack.pop())

    return queue


if __name__ == "__main__":
    expressions = [
        ".6+3",
        "2+3",              # 5
        "1-2*3",            # -5
        "(1-2)*3",          # -3
        "(1+(2/2))-(3-5)",  # 4
        "1/2-1/2"           # 0
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")