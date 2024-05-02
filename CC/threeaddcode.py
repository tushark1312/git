import re
def generate_tac(expression):
    # Split the expression by operators while keeping the operators
    tokens = re.split(r'(\W)', expression.replace(' ', ''))

    # List to hold intermediate results and temporary variables
    tac = []
    temp_counter = 0  # Counter for temporary variable names

    # Helper function to create a new temporary variable name
    def new_temp():
        nonlocal temp_counter
        temp_var = f"t{temp_counter}"
        temp_counter += 1
        return temp_var

    # Stack for operands and operators
    operand_stack = []
    operator_stack = []

    # Priority of operators
    precedence = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    # Shunting-yard algorithm to parse the expression and convert to TAC
    for token in tokens:
        if re.match(r'\w+', token):  # Operand (variable or number)
            operand_stack.append(token)
        elif token in precedence:  # Operator
            while (operator_stack and precedence[operator_stack[-1]] >= precedence[token]):
                op = operator_stack.pop()
                right = operand_stack.pop()
                left = operand_stack.pop()
                temp_var = new_temp()
                tac.append(f"{temp_var} = {left} {op} {right}")
                operand_stack.append(temp_var)
            operator_stack.append(token)

    # Process remaining operators in the stack
    while operator_stack:
        op = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        temp_var = new_temp()
        tac.append(f"{temp_var} = {left} {op} {right}")
        operand_stack.append(temp_var)

    # Return the generated TAC
    return tac


# Test the function with a sample expression
expression = "w = u*u - u*v+ v*v"
tac = generate_tac(expression)

# Output the TAC
print("Three-Address Code:")
for line in tac:
    print(line)