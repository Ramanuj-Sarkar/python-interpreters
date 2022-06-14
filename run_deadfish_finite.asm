.data
new_line: .asciiz "\n"
readable: .asciiz ">> "

testcode1: .asciiz "iissso"
testcode2: .asciiz "diissisdo"
testcode3: .asciiz "iissisdddddddddddddddddddddddddddddddddo"
testcode4: .asciiz "put carry"

.text

j main

# a0 = code
deadfish:
move $t0, $a0 # code pointer
li $t1, 0 # character
li $t2, 0 # numeral
start_deadfish_loop:
lbu $t1, ($t0)
beqz $t1, end_deadfish_loop
li $v0, 4
la $a0, readable
syscall
li $v0, 11
move $a0, $t1
syscall
bne $t1, 100, not_d
addi $t2, $t2, -1
j end_chars
not_d:
bne $t1, 105, not_i
addi $t2, $t2, 1
j end_chars
not_i:
bne $t1, 111, not_o
la $a0, new_line
li $v0, 4
syscall
move $a0, $t2
li $v0, 1
syscall
j end_chars
not_o:
bne $t1, 115, end_chars
mul $t2, $t2, $t2
end_chars:
la $a0, new_line
li $v0, 4
syscall
blt $t2, $zero, set_to_zero
beq $t2, 256, set_to_zero
end_number_checking:
addi $t0, $t0, 1
j start_deadfish_loop
set_to_zero:
li $t2, 0
j end_number_checking
end_deadfish_loop:
jr $ra

main:

la $a0, testcode1
jal deadfish

la $a0, testcode2
jal deadfish

la $a0, testcode3
jal deadfish

la $a0, testcode4
jal deadfish

li $v0, 10
syscall
