.data
readable: .asciiz ">> "
character: .space 2 # 1 bit + \0
new_line: .asciiz "\n"
.text
li $t0, 0 # character
li $t1, 0 # numeral
start_deadfish_loop:
la $a0, readable
li $v0, 4
syscall
la $a0, character
li $a1, 2
li $v0, 8
syscall
lbu $t0, ($a0)
bne $t0, 100, not_d
addi $t1, $t1, -1
j end_chars
not_d:
bne $t0, 105, not_i
addi $t1, $t1, 1
j end_chars
not_i:
bne $t0, 111, not_o
la $a0, new_line
li $v0, 4
syscall
move $a0, $t1
li $v0, 1
syscall
j end_chars
not_o:
bne $t0, 115, end_chars
mul $t1, $t1, $t1
end_chars:
la $a0, new_line
li $v0, 4
syscall
blt $t1, $zero, set_to_zero
beq $t1, 256, set_to_zero
end_number_checking:
j start_deadfish_loop
set_to_zero:
li $t1, 0
j end_number_checking

li $v0, 10
syscall
