def output_preorder(upper, start=1):
    output = [start - 1]
    if start * 2 <= upper:
        output += output_preorder(upper, start * 2)
    if start * 2 + 1 <= upper:
        output += output_preorder(upper, start * 2 + 1)
    return output


def run_minitree(code, input_mode='tree'):
    assert input_mode in ('tree', 'linear'), 'The only valid input modes are tree and linear.'

    valid_instructions = ('<', '>', '^', '+', '-', '.', ',', '[', ']')
    code_tree = [inst for inst in code if inst in valid_instructions]
    data_tree = [0]
    iteration_order = output_preorder(len(code_tree))
    cp = 0  # code pointer
    dp = 1  # tape pointer

    input_string = ''

    if input_mode == 'linear':
        new_tree = [''] * len(code_tree)
        for num, char in enumerate(code_tree):
            new_tree[iteration_order[num]] = char
        print('Warning: The format is intended to be tree-based.\n'
              'This is your code as intended (tree):\n'
              f'{"".join(new_tree)}')
        code_tree = new_tree

    bracket_stack = []  # checks if brackets are fine
    corresponding_bracket = {}  # makes looping quicker

    for num, position in enumerate(iteration_order):
        if code_tree[position] == '[':
            bracket_stack.append(num)
        elif code_tree[position] == ']':
            assert len(bracket_stack) > 0, 'unmatched ]'
            corresponding_bracket[num] = bracket_stack[-1]
            corresponding_bracket[bracket_stack[-1]] = num
            bracket_stack.pop()
    assert len(bracket_stack) == 0, 'unmatched ['

    while cp < len(iteration_order):
        inst = code_tree[iteration_order[cp]]
        if inst == '>':
            dp = dp * 2 + 1
            if dp > len(data_tree):
                data_tree += [0] * (dp - len(data_tree))
        elif inst == '<':
            dp *= 2
            if dp > len(data_tree):
                data_tree += [0] * (dp - len(data_tree))
        elif inst == '^':
            assert dp != 1, 'Cannot move up from root'
            dp //= 2
        elif inst == '+':
            data_tree[dp - 1] = (data_tree[dp - 1] + 1) % 256
        elif inst == '-':
            data_tree[dp - 1] = (data_tree[dp - 1] - 1) % 256
        elif inst == '.':
            print(chr(data_tree[dp - 1]), end='')
        elif inst == ',':
            if input_string == '':
                input_string = input(">>")
            if len(input_string) > 0:
                data_tree[dp - 1] = ord(input_string[0])
                input_string = input_string[1:]
        elif inst == '[':
            if data_tree[dp - 1] == 0:
                cp = corresponding_bracket[cp]
        elif inst == ']':
            if data_tree[dp - 1] != 0:
                cp = corresponding_bracket[cp]
        cp += 1
