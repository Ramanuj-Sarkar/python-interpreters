def run_ct(program: str, data: str) -> None:
    # Will not operate on strings which contain non-bits
    assert set(program).issubset({'0', '1', ';'}),\
        "The input strings must contain only 0, 1, and ;. The program string contains at least one illegal trit."
    assert set(data).issubset({'0', '1'}),\
        "The input strings must contain only 0, 1, and ;. The data string contains at least one illegal trit."
    # padding for print statements
    padding = ""
    # allows you to step through the program
    # and quickly stop infinite loops
    stop = ""
    # if data is empty, it stops
    # if input is not empty, it stops
    print('Commands|Data')
    while data != "" and stop == "":
        if program[0] == ";":
            # prints output similar to esolangs page
            print(f"    {program[0]}   |{padding}{data}", end="")
            program = program[1:] + program[:1]
            padding += " "
            data = data[1:]
        else:
            print(f"    {program[0]}   |{padding}{data}", end="")
            if data[0] == "1":
                data += program[0]
            program = program[1:] + program[:1]
        stop = input()


if __name__ == '__main__':
    run_ct('1', '1')
