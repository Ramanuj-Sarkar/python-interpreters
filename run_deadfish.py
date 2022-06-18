def run_deadfish():
    num = 0
    cont = True
    while cont:
        instructions = input('Enter line of code:')
        for char in instructions:
            print(f'>> {char}')
            if char == 'i': num += 1
            elif char == 's': num *= num
            elif char == 'd': num -= 1
            elif char == 'o':print(num)
            elif char == 'h':cont = False; break

            if num < 0 or num == 256: num = 0


if __name__ == '__main__':
    run_deadfish()
