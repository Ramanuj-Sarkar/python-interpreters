def run_bfp3(code: str) -> None:
    pointer=0   # for instructions
    row = 0   # for up and down tape
    column=0  # for left and right tape
    tape=[[0]]
    while pointer < len(code):
        if code[pointer] == '>':
            column += 1
            if column == len(tape[row]):
                for row_number in range(len(tape)):
                    tape[row_number].append(0)
        elif code[pointer] == '<':
            column -= 1
            if column < 0:
                for row_number in range(len(tape)):
                    tape[row_number] = [0] + tape[row_number]
                column += 1
        elif code[pointer] == 'v':
            row += 1
            if row == len(tape):
                tape.append([0]*(column+1))
        elif code[pointer] == '^':
            row -= 1
            if row < 0:
                tape = [[0]*(column+1)] + tape
                row += 1
        elif code[pointer] == '+':
            tape[row][column] = (tape[row][column] + 1) % 256
        elif code[pointer] == '-':
            tape[row][column] = (tape[row][column] - 1) % 256
        elif code[pointer] == '.':
            print(chr(tape[row][column]),end='')
        elif code[pointer] == ',':
            tape[row][column] = ord(input())
        elif code[pointer] == '[':
            if tape[row][column] == 0:
                nest_counter = 0
                while code[pointer] != ']' or nest_counter >= 0:
                    pointer += 1
                    if code[pointer] == '[':
                        nest_counter += 1
                    elif code[pointer] == ']':
                        nest_counter -= 1
        elif code[pointer] == ']':
            if tape[row][column] != 0:
                nest_counter = 0
                while code[pointer] != '[' or nest_counter >= 0:
                    pointer -= 1
                    if code[pointer] == ']':
                        nest_counter += 1
                    elif code[pointer] == '[':
                        nest_counter -= 1
        elif code[pointer] == 'x':
            break
        pointer += 1
