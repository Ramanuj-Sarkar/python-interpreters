# runs HQ9+2D
# if using a textfile, include the file extension
def run_HQ9p2D(code_string: str, textfile = False):
    code = []
    direction = '>'
    incrementer = 0
    if textfile:
        temp = ''
        for line in open(code_string, 'r'):
            temp += line
            code.append(line.strip('\n'))
        # this allows Q to work as intended
        code_string = temp
    else:
        code = code_string.split('\n')

    code_width = max([len(line) for line in code])
    # points to code[first argument][second argument]
    pointer = (0,0)
    while 0 <= pointer[0] < len(code) and 0 <= pointer[1] < code_width:
        # variable names look cleaner and indicate actual direction when incremented
        south = pointer[0]
        east = pointer[1]
        # the code can handle files with lines of variable length
        # and pass over comments, etc.
        if east >= len(code[south]) or code[south][east] not in 'HQ9+^v<>':
            pass
        else:
            char = code[south][east]
            
            if char in '^v<>':
                direction = char
            elif char == 'H': # Hello world
                print('Hello world!')
            elif char == 'Q': # quine
                print(code_string)
            elif char == '9': # 99 bottles of beer on the wall
                for i in range(99, 2, -1):
                    print(f'{i} bottles of beer on the wall,\n'
                          f'{i} bottles of beer!\n'
                          f"Take one down, pass it around,\n"
                          f"{i-1} bottles of beer on the wall!")
                # I've decided not to be lazy, and to write "1 bottle" and "No bottles"
                print("2 bottles of beer on the wall\n"
                      "2 bottles of beer!\n"
                      "Take one down, pass it around\n"
                      "1 bottle of beer on the wall!\n"
                      "1 bottle of beer on the wall,\n"
                      "1 bottle of beer!\n"
                      "Take one down, pass it around,\n"
                      "No bottles of beer on the wall!")
            elif char == '+': # increment some int
                incrementer += 1

        # sets direction
        if direction == '>':
            pointer = (pointer[0],pointer[1]+1)
        elif direction == 'v':
            pointer = (pointer[0]+1,pointer[1])
        elif direction == '<':
            pointer = (pointer[0],pointer[1]-1)
        else:
            pointer = (pointer[0]-1,pointer[1])
