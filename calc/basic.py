"""
Basic arithmetic calculator
  use Prefic notation

"""

ops = ('+', '-', '*', '/')

def do_math(a: float, b: float, op: str):
    if op == '+':
        return a + b
    else:
        return 0

num1 = 3
num2 = 2
operation = '-'

print(f'{num1} {operation} {num2} = {do_math(num1, num2, operation)}')


