"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

def calc(raw_expression):
    tokens = tokenize(raw_expression)
    if tokens is None:
        return None
    tokens = validate_tokens(tokens)
    if tokens is None:
        return None
    postfix_tokens = postfix_notation(tokens)
    if postfix_tokens is None:
        return None
    result = evaluate_postfix(postfix_tokens)
    return result

def tokenize(expression):
    tokens = []
    current_number = ""
    i = 0
    
    if expression == '':
        return None
    
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
            if not stack:  
                return None
            stack.pop() 
    while stack:
        if stack[-1] == '(':
            return None
        queue.append(stack.pop())

    return queue

def validate_tokens(tokens):
    if not tokens:
        return None
    elif tokens[0][0] == 'operator':
        return None
    elif tokens[-1][0] == 'operator':
        return None
    
    for i in range(len(tokens)-1):
        current_token = tokens[i][0]
        next_token =tokens[i+1][0]

        # Число перед открывающей скобкой
        if current_token == 'number' and next_token == 'parenthesis' and tokens[i+1][1] == '(':
            return None
        
        # Закрывающая скобка перед числом
        if current_token == 'parenthesis' and tokens[i][1] == ')' and next_token == 'number':
            return None
        
        # Оператор перед закрывающей скобкой
        if current_token == 'operator' and next_token == 'parenthesis' and tokens[i+1][1] == ')':
            return None
        
        # Открывающая скобка перед оператором
        if current_token == 'parenthesis' and tokens[i][1] == '(' and next_token == 'operator':
            return None
        
        # Число перед числом (без операции)
        if current_token == 'number' and next_token == 'number':
            return None
        
        #Два оператора подряд
        if current_token == 'operator' and next_token == 'operator':
            return None
      
    return tokens

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
    if len(stack) != 1:  
        return None
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
        "1/2-1/2", 
        "15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(0.5+1.5))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))"          # -30.0721649485
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")