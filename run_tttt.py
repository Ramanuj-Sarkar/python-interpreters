# This is based on a programming language.
def run_tttt(data: str, textfile: False) -> None:
    code = list(data)

    if textfile:
        code = ''.join(open(f'{code}', 'r').readlines())

    variables = [0, 0, 0]
    pointer = 0
    which_var = 0
    input_string = ''  # allows multiple inputs to happen easily

    corresponding_thing = {}  # dictionary for the corresponding beginning/ending things
    loop_queue = []  # acts as a queue for the last loop
    comment_queue = []  # acts as a queue for the last comment
    in_comment = False
    for num, char in enumerate(code):
        if char == 'k':
            in_comment = True
            comment_queue.append(num)
        elif char == 'l':
            assert len(comment_queue) > 0, 'unmatched l'
            corresponding_thing[num] = comment_queue[0]
            corresponding_thing[comment_queue[0]] = num
            comment_queue = comment_queue[1:]
            in_comment = False
        elif not in_comment:
            if char == 'i':
                loop_queue.append(num)
            elif char == 'j':
                assert len(loop_queue) > 0, 'unmatched j'
                corresponding_thing[num] = loop_queue[0]
                corresponding_thing[loop_queue[0]] = num
                loop_queue = loop_queue[1:]
    assert len(loop_queue) == 0, 'unmatched i'
    assert len(comment_queue) == 0, 'unmatched k'

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
            if input_string == '':
                input_string = input(">>")
            if len(input_string) > 0:
                variables[which_var] = ord(input_string[0])
                input_string = input_string[1:]
        elif 'i' == code[pointer]:
            if variables[which_var] == 0:
                pointer = corresponding_thing[pointer]
        elif 'j' == code[pointer]:
            if variables[which_var] != 0:
                pointer = corresponding_thing[pointer]
        elif 'k' == code[pointer]:
            pointer = corresponding_thing[pointer]
        assert 0 <= which_var <= 2, "the pointer must always be between 0 and 2, inclusive"
        pointer += 1
