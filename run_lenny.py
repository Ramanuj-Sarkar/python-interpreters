def run_lenny(code: str, actually_run = False) -> None:
    pointer = 0  # for instructions
    row = 0     # for up and down tape
    column = 0  # for left and right tape
    tape = [[0]]
    input_string = chr(10)  # allows multiple inputs easily

    # checks balance
    balance = 0
    for char in code:
        if char == '( ͡°(':
            balance += 1
        elif char == ']':
            balance -= 1
        assert balance >= 0, 'unmatched ) ͡°)'
    assert balance == 0, 'unmatched ( ͡°('

    while pointer < len(code):
        skip = 1
        if code[pointer:pointer+11] == 'ᕦ( ͡°ヮ ͡°)ᕥ':
            column += 1
            if column == len(tape[row]):
                for row_number in range(len(tape)):
                    tape[row_number].append(0)
            skip = 11
        elif code[pointer:pointer+18] == '(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ.*':
            column -= 1
            if column < 0:
                for row_number in range(len(tape)):
                    tape[row_number] = [0] + tape[row_number]
                column += 1
            skip = 18
        elif code[pointer:pointer+12] == '( ͡°╭͜ʖ╮ ͡°)':
            row += 1
            if row == len(tape):
                tape.append([0]*(column+1))
            skip = 12
        elif code[pointer:pointer+13] == 'ᕦ( ͡° ͜ʖ ͡°)ᕥ':
            row -= 1
            if row < 0:
                tape = [[0]*(column+1)] + tape
                row += 1
            skip = 13
        elif code[pointer:pointer+11] == '( ͡° ͜ʖ ͡°)':
            tape[row][column] = (tape[row][column] + 1) % 256
            skip = 11
        elif code[pointer:pointer+7] == '(> ͜ʖ<)':
            tape[row][column] = (tape[row][column] - 1) % 256
            skip = 7
        elif code[pointer:pointer+7] == '(♥ ͜ʖ♥)':
            print(chr(tape[row][column]),end='')
            skip = 7
        elif code[pointer:pointer+13] == 'ᕙ( ͡° ͜ʖ ͡°)ᕗ':
            if input_string == chr(10):
                input_string = input(">>") + chr(10)
            if len(input_string) > 0 and ord(input_string[0]) != chr(10):
                tape[row][column] = ord(input_string[0])
            input_string = input_string[1:]
            skip = 13
        elif code[pointer:pointer+5] == '( ͡°(':
            if tape[row][column] == 0:
                nest_counter = 0
                while code[pointer:pointer+5] != ') ͡°)' or nest_counter >= 0:
                    pointer += 1
                    if code[pointer:pointer+5] == '( ͡°(':
                        nest_counter += 1
                    elif code[pointer:pointer+5] == ') ͡°)':
                        nest_counter -= 1
        elif code[pointer:pointer+5] == ') ͡°)':
            if tape[row][column] != 0:
                nest_counter = 0
                while code[pointer:pointer+5] != '( ͡°(' or nest_counter >= 0:
                    pointer -= 1
                    if code[pointer:pointer+5] == ') ͡°)':
                        nest_counter += 1
                    elif code[pointer:pointer+5] == '( ͡°(':
                        nest_counter -= 1
        elif code[pointer:pointer+3] == 'ಠ_ಠ':
            break
        pointer += skip
