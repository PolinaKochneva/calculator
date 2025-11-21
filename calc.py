"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

tokenized_expression = []

def calc(raw_expression):
    i = 0
    token = raw_expression[i]
    match token:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            save_integer_part_of_number(token, raw_expression, i)
        case "(" | ")":
            ...
        case "*" | '/' | '-' | '+':
            ...
        case '.':
            ...
        case _:
            return None


def save_integer_part_of_number(token, expression, i):
   i += 1
   integer_part_of_number += token
   token = expression[i]
   match token:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            save_integer_part_of_number(token, expression, i)
        case "(" | ")":
            ...
        case "*" | '/' | '-' | '+':
            ...
        case '.':
            ...
        case _:
            return None


def save_fractional_part_of_number(token):
    ...

def read_single_token(token):
    ...



if __name__ == "__main__":
    expressions = [
        "2+3",              # 5
        "1-2*3",            # -5
        "(1-2)*3",          # -3
        "(1+(2/2))-(3-5)",  # 4
        "1/2-1/2"           # 0
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")