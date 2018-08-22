"""
Basic arithmetic calculator
  - conventional notation: a <space> + <space> b

"""

ops = ('+', '-', '*', '/')

def do_math(a: float, b: float, op: str):
    """
    perform single operation calculation here

    returns result or None if confused
    """
    if op == '+':
        return a + b
    else:
        return None

num1 = 3.0
num2 = 2
operation = '+'

answer = do_math(num1, num2, operation)

print(type(answer))   # TODO: do I care what the return type is?
print(f'{num1} {operation} {num2} = {answer}')
