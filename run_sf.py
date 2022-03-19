# Interpreter for a programming language which can be found here
# https://esolangs.org/wiki/Smallfuck
def run_sf(code: str, textfile=False) -> None:
    pointer = 0  # for instructions
    location = 0  # for tape
    tape = [0] * int(input('Indicate the number of cells in the tape:'))
    assert len(tape) > 0, 'The length of the tape must be greater than 0.'

    if textfile:
        code = ''.join(open(f'{code}', 'r').readlines())

    corresponding_bracket = {}  # dictionary where the values are the corresponding bracket positions of the keys
    bracket_stack = []  # acts as a stack for the last bracket
    for num, char in enumerate(code):
        if char == '[':
            bracket_stack.append(num)
        elif char == ']':
            assert len(bracket_stack) > 0, 'unmatched ]'
            corresponding_bracket[num] = bracket_stack[-1]
            corresponding_bracket[bracket_stack[-1]] = num
            bracket_stack.pop()
    assert len(bracket_stack) == 0, 'unmatched ['

    while pointer < len(code):
        if code[pointer] == '>':
            location += 1
            assert location < len(tape), f'The > at location #{pointer} moves the tape too far right.'
        elif code[pointer] == '<':
            assert location > 0, f'The < at location #{pointer} moves the tape too far left.'
            location -= 1
        elif code[pointer] == '*':
            tape[location] = (tape[location] + 1) % 2
        elif code[pointer] == '[':
            if tape[location] == 0:
                pointer = corresponding_bracket[pointer]
        elif code[pointer] == ']':
            if tape[location] != 0:
                pointer = corresponding_bracket[pointer]
        pointer += 1
