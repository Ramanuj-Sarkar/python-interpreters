# runs Bitwise Cyclic Tag from https://esolangs.org/wiki/Bitwise_Cyclic_Tag
# using program program
# and data data
# hit enter after each line
# or input something to stop the program
def run_bct_1(program: str, data: str) -> None:
    # Will not operate on strings which contain non-bits
    for bit in program:
        if bit not in "01":
            return
    for bit in data:
        if bit not in "01":
            return
    # padding for print statements
    padding = ""
    # allows you to step through the program
    # and quickly stop infinite loops
    stop = ""
    # if data is empty, it stops
    # if input is not empty, it stops
    while data != "" and stop == "":
        if program[0] == "0":
            # prints output similar to esolangs page
            print(f" {program[0]}|{padding}{data}", end="")
            program = program[1:] + program[:1]
            padding += " "
            data = data[1:]
        else:
            print(f"{program[:2]}|{padding}{data}", end="")
            if data[0] == "1":
                data += program[1]
            program = program[2:] + program[:2]
        stop = input()

# runs the "CT" program on the esolangs page
# corresponds to BCT
# where 0 = 10, 1 = 11, ; = 0
# the trit corresponding to ; can be represented by any character that isn't 0 or 1
def run_ct(program: str, data: str) -> None:
    baseline = "01"
    for trit in program:
        if trit not in baseline:
            if len(baseline) == 3:
                return
            baseline += trit
    prod_list = program.split(baseline[2])
    prod_padding = max([len(x) for x in prod_list])
    data_padding = ""
    stop = ""
    while data != "" and stop == "":
        print(" " * (prod_padding - len(prod_list[0])), f"{prod_list[0]}|{data_padding}{data}", sep="", end="")
        if data[0] == "1":
            data += prod_list[0]
        data_padding += " "
        data = data[1:]
        temp = prod_list[0]
        prod_list = prod_list[1:]
        prod_list.append(temp)
        stop = input()
