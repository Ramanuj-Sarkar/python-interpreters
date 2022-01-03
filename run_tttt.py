# This is based on a programming language.
def run_tttt(data: str) -> None:
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
        elif 'd' == code[pointer]:
            which_var -= 2
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
                while code[pointer] != 'j':
                    if code[pointer] == 'k':
                        pointer += code[pointer:].index('l')
                    pointer += 1
        elif 'j' == code[pointer]:
            if variables[which_var] != 0:
                while code[pointer] != 'i':
                    if code[pointer] == 'l':
                        # I don't know how to best use index here
                        while code[pointer] != 'k':
                            pointer -= 1
                    pointer -= 1
                pointer -= 1
        elif 'k' == code[pointer]:
            pointer += code[pointer:].index('l')
        pointer += 1
