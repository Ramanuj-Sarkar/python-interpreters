# runs language from https://esolangs.org/wiki/Generic_2D_Brainfuck
def run_generic_2d_bf(code_string: str, textfile = False) -> None:
    pointer = (0, 0)  # for instructions
    row = 0     # for up and down tape
    column = 0  # for left and right tape
    direction = 'r'  # for direction
    tape = [[0]]
    input_string = ''  # allows multiple inputs easily
    nest_counter = 0    # allows code with nested parentheses to work

    # this checks if the code is in a loop and what caused the loop
    # it can be [ or ], or _ if not in a loop
    loop_maker = '_'

    code = []
    if textfile:
        for line in open(code_string, 'r'):
            code.append(line.strip('\n'))
    else:
        code = code_string.split('\n')

    code_width = max([len(line) for line in code])

    while 0 <= pointer[0] < len(code) and 0 <= pointer[1] < code_width:
        # variable names look cleaner and indicate actual direction when incremented
        down = pointer[0]
        right = pointer[1]

        if right >= len(code[down]) or code[down][right] not in '><^vudlr+-.,[]':
            pass
        else:
            char = code[down][right]

            if loop_maker in '[]':
                if char in '[]':
                    nest_counter = nest_counter + 1 if loop_maker == char else nest_counter - 1
                    if nest_counter == 0:
                        loop_maker = '_'
            else:
                if char in 'udlr':
                    direction = char
                elif char == '>':
                    column += 1
                    if column == len(tape[row]):
                        for row_number in range(len(tape)):
                            tape[row_number].append(0)
                elif char == '<':
                    column -= 1
                    if column < 0:
                        for row_number in range(len(tape)):
                            tape[row_number] = [0] + tape[row_number]
                        column += 1
                elif char == 'v':
                    row += 1
                    if row == len(tape):
                        tape.append([0]*(column+1))
                elif char == '^':
                    row -= 1
                    if row < 0:
                        tape = [[0]*(column+1)] + tape
                        row += 1
                elif char == '+':
                    tape[row][column] = (tape[row][column] + 1) % 256
                elif char == '-':
                    tape[row][column] = (tape[row][column] - 1) % 256
                elif char == '.':
                    print(chr(tape[row][column]),end='')
                elif char == ',':
                    if input_string == '':
                        input_string = input(">>")
                    # the following thing is when
                    # the input isn't an empty string
                    if len(input_string) > 0:
                        tape[row][column] = ord(input_string[0])
                        input_string = input_string[1:]
                elif char in '[':
                    if tape[row][column] == 0:
                        loop_maker = '['
                        nest_counter = 1
                elif char == ']':
                    if tape[row][column] != 0:
                        loop_maker = ']'
                        nest_counter = 1

        # sets direction
        if (loop_maker == ']' and direction == 'd') or (loop_maker != ']' and direction == 'u'):    # normally up
            pointer = (pointer[0] - 1, pointer[1])
        elif (loop_maker == ']' and direction == 'u') or (loop_maker != ']' and direction == 'd'):  # normally down
            pointer = (pointer[0] + 1, pointer[1])
        elif (loop_maker == ']' and direction == 'r') or (loop_maker != ']' and direction == 'l'):  # normally left
            pointer = (pointer[0], pointer[1] - 1)
        else:  # normally right
            pointer = (pointer[0], pointer[1] + 1)
