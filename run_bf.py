def run_bf(code: str, textfile = False) -> None:
    pointer = 0     # for instructions
    location = 0    # for tape
    tape = [0]
    input_string = ''  # allows multiple inputs to happen easily

    if textfile:
        code = ''.join(open(f'{code}', 'r').readlines())

    corresponding_right_bracket = {}       # dictionary where keys are left brackets and values are right brackets
    corresponding_left_bracket = {}  # dictionary where keys are right brackets and values are left brackets
    bracket_stack = []     # acts as a stack for the last bracket
    for num, char in enumerate(code):
        if char == '[':
            bracket_stack.append(num)
        elif char == ']':
            assert len(bracket_stack) > 0, 'unmatched ]'
            corresponding_left_bracket[num] = bracket_stack[-1]
            corresponding_right_bracket[bracket_stack[-1]] = num
            bracket_stack.pop()
    assert len(bracket_stack) == 0, 'unmatched ['

    while pointer < len(code):
        if code[pointer] == '>':
            location += 1
            if location == len(tape):
                tape.append(0)
        elif code[pointer] == '<':
            location -= 1
            if location < 0:
                tape = [0] + tape
                location += 1
        elif code[pointer] == '+':
            tape[location] = (tape[location] + 1) % 256
        elif code[pointer] == '-':
            tape[location] = (tape[location] - 1) % 256
        elif code[pointer] == '.':
            print(chr(tape[location]),end='')
        elif code[pointer] == ',':
            if input_string == '':
                input_string = input(">>")
            if len(input_string) > 0:
                tape[location] = ord(input_string[0])
            else:
                tape[location] = 10
            input_string = input_string[1:]
        elif code[pointer] == '[':
            if tape[location] == 0:
                pointer = corresponding_right_bracket[pointer]
        elif code[pointer] == ']':
            if tape[location] != 0:
                pointer = corresponding_left_bracket[pointer]
        pointer += 1
