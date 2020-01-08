from tqdm import tnrange

path = 'input.txt'
with open(path) as file:
  line = file.readline()
  data = line.split(',')
  code_base = [int(i) for i in data]
  
def interpret(n, v, code):
  ip = 0
  code[1] = n
  code[2] = v
  while True:
    op = code[ip]
    if op == 1:
      #print(str(code[ip+3]) + " <- " + str(code[code[ip+1]]) + " + " + str(code[code[ip+2]]) + ";")
      code[code[ip+3]] = code[code[ip+1]] + code[code[ip+2]]
      ip += 4
      continue
    if op == 2:
      #print(str(code[ip+3]) + " <- " + str(code[code[ip+1]]) + " * " + str(code[code[ip+2]]) + ";")
      code[code[ip+3]] = code[code[ip+1]] * code[code[ip+2]]
      ip += 4
      continue
    if op == 99:
      #print("done")
      break
    print("error op code " + str(op) + "is not valid")
    break
  return code[0]

for n in range(100):
  for v in range(100):
    code = code_base.copy()
    print(str(100*n + v))
    if(interpret(n,v,code) == 19690720):
      print("Solution found! n:" + str(n) + " v:" + str(v))
      input("press enter to continue")      

code = code_base.copy()
print(interpret(12,2,code))

a = input('press enter to continue')