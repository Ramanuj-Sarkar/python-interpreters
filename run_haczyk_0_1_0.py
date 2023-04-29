# the coder gives alphanumeric characters to the variables
# who barter with each other
# they like the stuff in their names
# they share everything else equally
def run_haczyk_0_1_0(code_string: str, textfile = False):
    code = []       # this holds the code
    pointer = 0     # this points to the line being read
    var_dict = {}   # this holds all the variables
    nested_loop = False     # this checks if it is already in a loop

    # prints out error message
    # is not an error
    class Haczyk_Error():
        def __init__(self, message):
            print('Error:', message, sep="\n")

    # assigns data
    def assign_data(variable, relation, value):
        sign = relation[0]
        times = relation[2]     # must be between 0 and 9
        if variable not in var_dict:
            var_dict[variable] = dict()

        if not times.isdigit():
            return Haczyk_Error(f'Character {times} must be a digit between 0 and 9, inclusive.')
        else:
            times = int(times)
            if times != 0:
                if sign == '+':
                    for ch in value:
                        if ch not in var_dict[variable]:
                            var_dict[variable][ch] = 0
                        var_dict[variable][ch] += times
                        if var_dict[variable][ch] == 0:
                            del var_dict[variable][ch]
                elif sign == '-':
                    for ch in value:
                        if ch not in var_dict[variable]:
                            var_dict[variable][ch] = 0
                        var_dict[variable][ch] -= times
                        if var_dict[variable][ch] == 0:
                            del var_dict[variable][ch]
                else:
                    return Haczyk_Error(f'Sign {sign} has not been implemented yet.')

    # checks if the variable and value contain only letters and numbers
    def good_variable(variable):
        for char in variable:
            if not (char.isdigit() or char.isalpha()):
                return Haczyk_Error(f'"{variable}" has characters which are not allowed.\n'
                                    f'It can only contain letters and numbers.')
        return variable

    if textfile:
        for line in open(code_string, 'r'):
            code.append(line.strip('\n'))
    else:
        code += code_string.split('\n')

    # checks if parentheses are valid
    while_count_dict = {}
    to_open_paren = {}
    to_close_paren = {}
    open_paren_stack = []
    for num, chars in enumerate(code):
        if chars.strip() == '':
            continue
        elif chars.strip()[0] == '?':
            if '(' not in chars or ')' not in chars:
                continue
            while_statement = chars.strip()
            maximum_number = while_statement[while_statement.index('?')+1:while_statement.index('(')].strip()
            if not ((maximum_number.isdigit() and int(maximum_number) >= 0) or maximum_number == '?'):
                return Haczyk_Error(f'"{maximum_number}" is not a valid number of maximum iteration times'
                                    f' in "{while_statement}" at line {num-1}.'
                                    f'Maximum number of times must be a non-negative integer'
                                    f' or "?" which signifies infinite looping.')
            while_count_dict[num] = maximum_number
            open_paren_stack.append(num)
            print(open_paren_stack)
        elif chars.strip() == ')':
            if len(open_paren_stack) == 0:
                return Haczyk_Error(f'")" at line {num} has no corresponding if statement or while loop.')
            to_open_paren[num] = open_paren_stack[-1]
            to_close_paren[open_paren_stack[-1]] = num
            open_paren_stack.pop()
    if len(open_paren_stack) > 0:
        return Haczyk_Error(f'There are unpaired "?" at lines: {open_paren_stack}')

    # actually interprets code
    while pointer < len(code):
        # interprets one line of code
        # bartering happens after each line of code is seen
        line = code[pointer].strip()
        if '//' in line:
            line = line[:line.index('//')]
        if len(line) > 0:
            if line[0] == '?':
                if pointer not in while_count_dict:
                    print(line)
                else:
                    if while_count_dict[pointer] == '0':
                        if nested_loop:
                            while_statement = line.strip()
                            while_count_dict[pointer] = while_statement[while_statement.index('?')+1:
                                                                        while_statement.index('(')].strip()
                        if while_count_dict[pointer] == '0':
                            pointer = to_close_paren[pointer]
                            continue
                    else:
                        nested_loop = True
                # implement if-statement rules
            elif line.strip() == ')':
                repeats_number = while_count_dict[to_open_paren[pointer]]
                if repeats_number != '0':
                    if repeats_number.isdigit():
                        while_count_dict[to_open_paren[pointer]] = str(int(repeats_number)-1)
                    pointer = to_open_paren[pointer] - 1
                nested_loop = False
            elif '<' in line:
                var, val = line.split('<', 1)
                command = f'{var[-1]}<{val[0]}'
                var, val = good_variable(var[:-1].strip()), good_variable(val[1:].strip())
                if isinstance(var, Haczyk_Error):
                    return var
                sanity = assign_data(var, command, val)
                if isinstance(sanity, Haczyk_Error):
                    return sanity
            else:
                if line[-1] == ']' and '[' in line and line[:line.index('[')] in var_dict:
                    var_line = line[:line.index('[')]
                    letter = line[line.index('[')+1:line.index(']')]
                    if letter == '':
                        print(f'{var_line}: {var_dict[var_line]}')
                    elif letter not in var_dict[var_line]:
                        print(f'{var_line}[{letter}]: 0')
                    else:
                        print(f'{var_line}[{letter}]: {var_dict[var_line][letter]}')
                else:
                    print(line)
        pointer += 1

        # begins bartering
        for var1 in [one for one in var_dict][::-1]:
            for var2 in [two for two in var_dict]:
                if var1 != var2:
                    var1_wants = [char for char in var1] + [key for key in var_dict[var1] if var_dict[var1][key] < 0]
                    for char_var1_wants in var1_wants:
                        if char_var1_wants in var_dict[var2]:
                            var2_wants = [char for char in var2] + [key for key in var_dict[var2] if var_dict[var2][key] < 0]
                            for char_var2_wants in var2_wants:
                                if char_var2_wants in var_dict[var1]:
                                    if char_var1_wants == char_var2_wants:
                                        continue
                                    if char_var1_wants not in var_dict[var1]:
                                        var_dict[var1][char_var1_wants] = 0
                                    if char_var2_wants not in var_dict[var2]:
                                        var_dict[var2][char_var2_wants] = 0
                                    num_var1_has = var_dict[var1][char_var2_wants]
                                    num_var2_has = var_dict[var2][char_var1_wants]
                                    if num_var1_has > num_var2_has:
                                        var_dict[var1][char_var1_wants] += num_var2_has
                                        var_dict[var2][char_var1_wants] = 0
                                        var_dict[var1][char_var2_wants] -= num_var2_has
                                        var_dict[var2][char_var2_wants] += num_var2_has
                                    elif num_var2_has > num_var1_has:
                                        var_dict[var1][char_var1_wants] += num_var1_has
                                        var_dict[var2][char_var1_wants] -= num_var1_has
                                        var_dict[var1][char_var2_wants] = 0
                                        var_dict[var2][char_var2_wants] += num_var1_has
                                    else:
                                        var_dict[var1][char_var1_wants] += num_var2_has
                                        var_dict[var2][char_var1_wants] = 0
                                        var_dict[var1][char_var2_wants] = 0
                                        var_dict[var2][char_var2_wants] += num_var1_has

                                    if char_var1_wants in var_dict[var1] and var_dict[var1][char_var1_wants] == 0:
                                        del var_dict[var1][char_var1_wants]
                                    if char_var2_wants in var_dict[var1] and var_dict[var1][char_var2_wants] == 0:
                                        del var_dict[var1][char_var2_wants]
                                    if char_var1_wants in var_dict[var2] and var_dict[var2][char_var1_wants] == 0:
                                        del var_dict[var2][char_var1_wants]
                                    if char_var2_wants in var_dict[var2] and var_dict[var2][char_var2_wants] == 0:
                                        del var_dict[var2][char_var2_wants]

                                    break
                    # another idea I had
                    # var1_not_wants = [key for key in var_dict[var1] if key not in var1_wants]
    return 'File ended'
