def run_top_height_1_0(code_string: str, text_file = True) -> None:
    stack = [0]
    code = []

    if text_file:
        with open(code_string, 'r') as file:
            # The newlines don't affect the outcome
            code = file.readlines()
    else:
        code = code_string.split('\n')

    while len(stack) > 0:

        # The pointer's next position is always x_coord, y_coord.
        x_coord = abs(stack[-1])
        y_coord = len(stack)-1

        if y_coord < len(code) and x_coord < len(code[y_coord]):
            instruction = code[y_coord][x_coord]

            # appends digits
            if instruction.isdigit():
                stack.append(int(instruction))

            # appends the ASCII values of letters
            elif instruction.isalpha() or '!' == instruction:
                stack.append(ord(instruction))

            # move down one space
            elif ':' == instruction:
                stack.append(stack[-1])

            # arithmetic instructions
            elif instruction in {'+', '-', '*', '<', '>', '\\', '/', '%', '^'}:
                if y_coord > 0:
                    a = stack.pop()
                    b = stack.pop()
                    if '+' == instruction:
                        stack.append(a+b)
                    elif '-' == instruction:
                        stack.append(a-b)
                    elif '*' == instruction:
                        stack.append(a*b)
                    elif '>' == instruction:
                        stack.append(max({a,b}))
                    elif '<' == instruction:
                        stack.append(min(a,b))
                    elif '\\' == instruction:
                        stack.append(a)
                        stack.append(b)
                    elif '^' == instruction:
                        anum = (-(a+1) if a+1 < len(stack) else 0)
                        c = stack[anum]
                        stack[anum] = b
                        stack.append(c)
                    else:
                        if b == 0:
                            break
                        elif '/' == instruction:
                            stack.append(a//b)
                        else:
                            stack.append(a%b)
                else:
                    break

            # popping instructions
            elif instruction in {'$', '.', ','}:
                new = stack.pop()
                if '.' == instruction:
                    print(new,end='')
                elif ',' == instruction:
                    print(chr(abs(new)),end='')

            elif '~' == instruction:
                new = input()[0]
                if new.isdigit():
                    stack.append(int(new))
                else:
                    stack.append(ord(new))
            else:
                break
        else:
            break


if __name__ == '__main__':
    run_top_height_1_0('~\n2:\n..\\', False)
