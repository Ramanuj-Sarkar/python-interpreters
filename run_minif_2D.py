def run_minif_2D(code_string, file_name=False):
    # This is the code itself.
    code = []

    # This is the memory
    memory = [0] * 8

    # You can use text files.
    if file_name:
        for line in open(code_string, 'r'):
            code.append(line.rstrip('\n'))
    else:
        code = code_string.split('\n')

    # This makes sure you can still go down
    # when one line is shorter than all the rest
    max_line = max([len(line) for line in code])

    # This indicates the next instruction in the code.
    pointer = (0, 0)

    # This indicates the current memory location.
    cell = 0

    # The direction is equal to direction * 90 degrees counterclockwise from right.
    direction = 0
    while -1 < pointer[0] < len(code) and -1 < pointer[1] < max_line:
        row = pointer[0]
        column = pointer[1]
        step_number = 1

        if column < len(code[row]) and code[row][column] in '<.!@':
            instruction = code[row][column]
            if instruction == '<' and cell != 0:
                cell -= 1
            elif instruction == '@':
                direction = (direction + 1) % 4
            elif instruction in ('.', '!'):
                # makes sure there are always 8 zeroes to query
                if cell + 8 == len(memory):
                    memory.append(0)
                cell += 1
                memory[cell] ^= 1

                if instruction == '.':
                    # 8 cells are always available
                    out = memory[cell:cell+8]

                    out_num = sum(2 ** (7 - power) for power, digit in enumerate(out) if digit == 1)
                    if out_num == 0:
                        in_str = input("Input ASCII value between 0 and 255, inclusive:")
                        if in_str == '':
                            in_num = 0
                        else:
                            in_num = ord(in_str[0])
                        while not 0 <= in_num <= 255:
                            in_str = input("Input ASCII value between 0 and 255, inclusive:")
                            if in_str == '':
                                in_num = 0
                            else:
                                in_num = ord(in_str[0])
                        for power in range(7, -1, -1):
                            memory[cell+7-power] = in_num // 2 ** power
                            in_num %= 2 ** power
                    else:
                        print(chr(out_num))
                elif instruction == '!' and memory[cell] == 0:
                    step_number = 2

        for _ in range(step_number):
            if direction == 0:
                pointer = (row, column + 1)
            elif direction == 1:
                pointer = (row + 1, column)
            elif direction == 2:
                pointer = (row, column - 1)
            else:  # direction == 3
                pointer = (row - 1, column)
            row = pointer[0]
            column = pointer[1]
    return memory
