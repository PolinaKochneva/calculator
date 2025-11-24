"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

tokenized_expression = []

    
def calc(raw_expression):
    global tokenized_expression
    tokenized_expression = []
    start(raw_expression)

def start(expression):
    i = 0
    token = expression[i]
    match token:
        case '0' | '1' | '2' | '3'| '4' | '5' | '6' | '7' | '8' | '9':
            save_integer_part_of_number(token, expression, i)
        case "(" | ")":
            ...
        case "*" | '/' | '-' | '+':
            ...
        case '.':
            save_fractional_part_of_number(token, expression, i)
        case _:
            return None

def save_integer_part_of_number(token, expression, i):
   global tokenized_expression
   integer_part_of_number_list = []
   i += 1
   integer_part_of_number_list += token
   token = expression[i]
   match token:
        case '0' | '1' | '2' | '3'| '4' | '5' | '6' | '7' | '8' | '9':
            save_integer_part_of_number(token, expression, i)
        case "(" | ")":
            integer_part_of_number = "".join(integer_part_of_number_list)
            tokenized_expression += integer_part_of_number
            ...
        case "*" | '/' | '-' | '+':
            integer_part_of_number = "".join(integer_part_of_number_list)
            tokenized_expression += integer_part_of_number
            ...
        case '.':
            integer_part_of_number = "".join(integer_part_of_number_list)
            save_fractional_part_of_number(token, expression, i, integer_part_of_number)
            ...
        case _:
            return None


def save_fractional_part_of_number(token, expression, i, integer_part_of_number):
    global tokenized_expression
    fractional_part_of_number = []
    i += 1
    fractional_part_of_number += token
    token = expression[i]
    match token:
        case '0' | '1' | '2' | '3'| '4' | '5' | '6' | '7' | '8' | '9':
            save_fractional_part_of_number(token, expression, i, integer_part_of_number)
        case "(" | ")":
            number = "".join(fractional_part_of_number)
            tokenized_expression += number
            ...
        case "*" | '/' | '-' | '+':
            number = "".join(fractional_part_of_number)
            tokenized_expression += number
            ...
        case '.':
            return None
        case _:
            return None

def read_single_token(token, expression, i):
    single_token = []
    i += 1
    fractional_part_of_number += token
    token = expression[i]
    match token:
        case '0' | '1' | '2' | '3'| '4' | '5' | '6' | '7' | '8' | '9':
            save_integer_part_of_number(token, expression, i)
        case "(" | ")":
            read_single_token(token, expression, i)
        case "*" | '/' | '-' | '+':
            read_single_token(token, expression, i)
        case '.':
            save_fractional_part_of_number(token, expression, i)
        case _:
            return None



if __name__ == "__main__":
    expressions = [
        "15+3",
        "2+3",              # 5
        "1-2*3",            # -5
        "(1-2)*3",          # -3
        "(1+(2/2))-(3-5)",  # 4
        "1/2-1/2"           # 0
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")