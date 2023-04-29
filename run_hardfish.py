def run_hardfish(code):
    runnable = list(code)
    code_length = len(runnable)
    previous = ''
    for char in runnable:
        if char == previous:
            return "Repetition is not allowed."
        previous = char

    number = 0
    pointer = 0

    while pointer < code_length:
        char = runnable[pointer]
        if char == 'o':
            print(number)
        elif char == 'i':
            number += 1
        elif char == 'r':
            runnable[pointer] = ' '
            pointer = -1
        elif char == 'q':
            if number % 3 == 0:
                number //= 3
            else:
                number = 2 * number + 1
        elif char == 'c':
            if number % 2 == 0:
                number //= 2
            else:
                number = 3 * number + 1

        if number == -1 or number == 256:
            number = 0
        pointer += 1
    return f'{number}'
