def run_2deadfish(code_string: str, file_name=False):
    # This is the code itself.
    code = []

    # This debug string prints the equivalent code in Deadfish
    debug_string = ''

    # You can use text files
    # Newline characters don't affect anything
    # Therefore, the code is different when using or not using a text file
    if file_name:
        with open(code_string, 'r') as file:
            code = file.readlines()
    else:
        code = code_string.split('\n')

    # This makes sure you can still go down
    # when one line is shorter than all the rest
    max_line = max([len(line) for line in code])

    pointer = (0, 0)
    # This is the actual counter.
    counter = 0
    # The direction is equal to direction * 90 degrees counterclockwise from right.
    # I couldn't make math.sin and math.cos work with this, even using radians.
    # It would say int(math.cos(radians(270))) was -1
    direction = 0
    while -1 < pointer[0] < len(code) and -1 < pointer[1] < max_line:
        row = pointer[0]
        column = pointer[1]
        if column < len(code[row]) and code[row][column] in 'diso':
            instruction = code[row][column]
            debug_string += instruction

            if instruction == 'o':
                print(counter)
            elif instruction == 'i':
                counter += 1
                direction += 1
            elif instruction == 's':
                counter **= 2
                direction += 2
            elif instruction == 'd':
                counter -= 1
                direction += 3

        # 4 * 90 = 360 degrees = 0 degrees
        direction %= 4

        if counter == 256 or counter == -1:
            counter = 0

        if direction == 0:
            pointer = (row, column+1)
        elif direction == 1:
            pointer = (row+1, column)
        elif direction == 2:
            pointer = (row, column-1)
        elif direction == 3:
            pointer = (row-1,column)

    return debug_string
