"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

def calc(raw_expression):
    tokens = tokenize(raw_expression)
    if tokens is None:
        return None
    postfix_tokens = postfix_notation(tokens)
    result = evaluate_postfix(postfix_tokens)
    return result

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
            if expression[i+1] == '.':
                return None
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
            while stack and (stack[-1] in '+-*/') and (priority[stack[-1]] >= priority[char]):
                queue.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char ==')':
            while stack and stack[-1] != '(':
                queue.append(stack.pop()) 
            stack.pop()
        '''else:
            while len(stack) > 0:
                if stack[-1] == '(':
                    return None
                queue.append(stack.pop())'''
    while stack:
        if stack[-1] == '(':
            return None
        queue.append(stack.pop())

    return queue

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif token in '+-*/':
            operand = token
            right = stack.pop()
            left = stack.pop()
            result = apply_operation(operand, left, right)
            stack.append(result)
    return stack[-1]        

def apply_operation(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right 
    return result          


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