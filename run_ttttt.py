def run_ttttt(data: str) -> None:
    code = list(data)
    variables = [0, 0, 0]
    pointer = 0
    which_var = 0

    while pointer < len(code):
        if 'a' == code[pointer]:
            variables[which_var] += 2
        elif 'b' == code[pointer]:
            variables[which_var] -= 1
        elif 'c' == code[pointer]:
            which_var += 1
            if which_var == len(variables):
                variables.append(0)
        elif 'd' == code[pointer]:
            which_var -= 2
            while which_var < 0:
                variables = [0] + variables
                which_var += 1
        elif 'e' == code[pointer]:
            print(chr(variables[which_var]), end="")
        elif 'f' == code[pointer]:
            print(variables[which_var], end="")
        elif 'g' == code[pointer]:
            print("\n", end="")
        elif 'h' == code[pointer]:
            variables[which_var] = ord(input())
        elif 'i' == code[pointer]:
            if variables[which_var] == 0:
                nest_counter = 0
                while code[pointer] != 'j' or nest_counter >= 0:
                    pointer += 1
                    if code[pointer] == 'i':
                        nest_counter += 1
                    elif code[pointer] == 'j':
                        nest_counter -= 1
                    elif code[pointer] == 'k':
                        pointer += code[pointer:].index('l')
        elif 'j' == code[pointer]:
            if variables[which_var] != 0:
                nest_counter = 0
                while code[pointer] != 'i' or nest_counter >= 0:
                    pointer -= 1
                    if code[pointer] == 'j':
                        nest_counter += 1
                    elif code[pointer] == 'i':
                        nest_counter -= 1
                    elif code[pointer] == 'l':
                        while code[pointer] != 'k':
                            pointer -= 1
                pointer -= 1
        elif 'k' == code[pointer]:
            pointer += code[pointer:].index('l')
        pointer += 1
    print(variables)
