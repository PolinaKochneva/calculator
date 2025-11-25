"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""
# Константы, обозначающие тип токена
TOKEN_NUMBER = "number"
TOKEN_OPERATOR = "operator"
TOKEN_PARENTHESIS = "parenthesis"

# Константы, обозначающие класс символа
DIGIT = "digit"
POINT = "point"
OPERATOR = "operator"
PARENTHESIS = "parenthesis"
OTHER = "other"

# Константы, обозначающие состояние КА
NEW_TOKEN = "new_token"
NUMBER_INTEGER_PART = "number_integer_part"
NUMBER_FRACTIONAL_PART = "number_fractional_part"
ERROR = "error"

# Поддерживаемые математические операции в выражении вместе с их реализацией
# и приоритетом. Чем больше значение поля "priority", тем выше приоритет
OPERATORS = {
    "*": {"func": lambda a, b: a * b, "priority": 2},
    "/": {"func": lambda a, b: a / b, "priority": 2},
    "+": {"func": lambda a, b: a + b, "priority": 1},
    "-": {"func": lambda a, b: a - b, "priority": 1},
}


def start_accumulating_number():
    ...

def accumulate_number():
    ...

def accumulate_operator():
    ...

def accumulate_parenthesis():
    ...


FSM = {
    # Символ
    DIGIT: {
        # Текущее состояние        Новое состояние         Действие
        NEW_TOKEN:              (NUMBER_INTEGER_PART, start_accumulating_number),
        NUMBER_INTEGER_PART:    (NUMBER_INTEGER_PART, accumulate_number),
        NUMBER_FRACTIONAL_PART: (NUMBER_FRACTIONAL_PART, accumulate_number),
    },
    POINT: {
        NEW_TOKEN:              (NUMBER_FRACTIONAL_PART, start_accumulating_number),
        NUMBER_INTEGER_PART:    (NUMBER_FRACTIONAL_PART, accumulate_number),
        NUMBER_FRACTIONAL_PART: (ERROR, None),
    },
    OPERATOR: {
        NEW_TOKEN:              (NEW_TOKEN, accumulate_operator),
        NUMBER_INTEGER_PART:    (NEW_TOKEN, accumulate_operator),
        NUMBER_FRACTIONAL_PART: (NEW_TOKEN, accumulate_operator),
    },
    PARENTHESIS: {
        NEW_TOKEN:              (NEW_TOKEN, accumulate_parenthesis),
        NUMBER_INTEGER_PART:    (NEW_TOKEN, accumulate_parenthesis),
        NUMBER_FRACTIONAL_PART: (NEW_TOKEN, accumulate_parenthesis),
    },
    OTHER: {
        NEW_TOKEN:              (ERROR, None),
        NUMBER_INTEGER_PART:    (ERROR, None),
        NUMBER_FRACTIONAL_PART: (ERROR, None),
    },
}




def calc(raw_expression):
    ...

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