from tqdm import tnrange

path = 'input.txt'
with open(path) as file:
  line = file.readline()
  #line = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
  data = line.split(',')
  code_base = [int(i) for i in data]
  
def interpret(code):
  ip = 0
  while True:
    op = code[ip]
    
    #End
    if op == 99:
      print("DONE")
      break
     
    #print("OP: " + str(op))
    if (op//100)%10 == 1:
      a = ip+1
    else:
      a = code[ip+1]
      
    if (op//1000)%10 == 1:
      b = ip+2
    else:
      b = code[ip+2]
        
    if (op//10000)%10 == 1:
      c = ip+3
    else:
      c = code[ip+3]    
    
    #Addition
    if op%100 == 1:
      #print(str(code[ip+3]) + " <- " + str(code[code[ip+1]]) + " + " + str(code[code[ip+2]]) + ";")
      code[c] = code[a] + code[b]
      ip += 4
      continue
      
    #Multiplication
    if op%100 == 2:
      #print(str(code[ip+3]) + " <- " + str(code[code[ip+1]]) + " * " + str(code[code[ip+2]]) + ";")
      code[c] = code[a] * code[b]
      ip += 4
      continue
      
    #Input
    if op%100 == 3:
      val = input("IN: ")
      code[a] = int(val)
      ip += 2
      continue
      
    #Output
    if op%100 == 4:      
      print("OUT: " + str(code[a]))
      ip += 2
      continue
      
    #Jump-if-True
    if op%100 == 5:
      if code[a] != 0:
        ip = code[b]
      else:
        ip += 3
      continue
    
    #Jump-if-False
    if op%100 == 6:
      if code[a] == 0:
        ip = code[b]
      else:
        ip += 3
      continue
        
    #Less than
    if op%100 == 7:
      if code[a] < code[b]:
        code[c] = 1
      else:
        code[c] = 0
      ip += 4
      continue
      
    #Equals
    if op%100 == 8:
      if code[a] == code[b]:
        code[c] = 1
      else:
        code[c] = 0
      ip += 4
      continue
      
    print("error op code " + str(op) + "is not valid")
    break
   

code = code_base.copy()
interpret(code)

a = input('press enter to continue')