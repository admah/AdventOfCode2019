program = []

def opcode_1(current_position):
  dest = int(program[current_position+3])
  operand_1 = int(program[current_position+1])
  operand_2 = int(program[current_position+2])
  program[dest] = int(program[operand_1]) + int(program[operand_2])
 
def opcode_2(current_position):
  dest = int(program[current_position+3])
  operand_1 = int(program[current_position+1])
  operand_2 = int(program[current_position+2])
  program[dest] = int(program[operand_1]) * int(program[operand_2])


function_lookup = {
  '1': opcode_1,
  '2': opcode_2,
}

filepath = 'input'
with open(filepath) as fp:
   line = fp.readline()
   program = line.split(',')
   program_reset = program[:]

   for noun in range(0,99):
     for verb in range(0,99):
       program = program_reset[:]
       program[1] = noun
       program[2] = verb
       current_position = 0
       while program[current_position] != '99':
         function_lookup[program[current_position]](current_position)
         current_position += 4
       if program[0] == 19690720:
         print(noun,verb)
         print((100*noun)+verb)
