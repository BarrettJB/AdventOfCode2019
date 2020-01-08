from itertools import permutations
import threading
import time

path = 'input.txt'
with open(path) as file:
  line = file.readline()
  #line = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
  #line = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
  #line = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
  #line = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
  #line = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
  data = line.split(',')
  code_base = [int(i) for i in data]

def opmode1(opcode):
  if (op//100)%10 == 1:
    a = self.ip+1
  else:
    a = self.memory[self.ip+1]
  return a
    

class Int_Machine(threading.Thread):
  def opmode3(self,op):
    if (op//100)%10 == 1:
      a = self.ip+1
    else:
      a = self.memory[self.ip+1]
    
    if (op//1000)%10 == 1:
      b = self.ip+2
    else:
      b = self.memory[self.ip+2]
      
    if (op//10000)%10 == 1:
      c = self.ip+3
    else:
      c = self.memory[self.ip+3]
    
    return a,b,c
      
  def opmode2(self,op):
    if (op//100)%10 == 1:
      a = self.ip+1
    else:
      a = self.memory[self.ip+1]
    
    if (op//1000)%10 == 1:
      b = self.ip+2
    else:
      b = self.memory[self.ip+2]
      
    return a,b  
      
  def opmode1(self,op):
    if (op//100)%10 == 1:
      a = self.ip+1
    else:
      a = self.memory[self.ip+1]
    return a

  def __init__(self,id,code):
    self.id = id
    self.code = code
    self.reset()
    super(Int_Machine,self).__init__()
    
  def reset(self):
    self.memory = self.code
    self.ip = 0
    self.inputs = []
    self.outputs = []
    
  def step(self):
    op = self.memory[self.ip]
    
    #End
    if op == 99:
      #print("DONE")
      return 1 
  
    #Addition
    if op%100 == 1:
      #print(str(self.memory[self.ip+3]) + " <- " + str(self.memory[self.memory[ip+1]]) + " + " + str(self.memory[self.memory[self.ip+2]]) + ";")
      a,b,c = self.opmode3(op)
      self.memory[c] = self.memory[a] + self.memory[b]
      self.ip += 4
      return
      
    #Multiplication
    if op%100 == 2:
      #print(str(self.memory[self.ip+3]) + " <- " + str(self.memory[self.memory[ip+1]]) + " * " + str(self.memory[self.memory[self.ip+2]]) + ";")
      a,b,c = self.opmode3(op)
      self.memory[c] = self.memory[a] * self.memory[b]
      self.ip += 4
      return
      
    #Input
    if op%100 == 3:
      a = self.opmode1(op)
      #val = input("IN: ")
      failsafe = 0
      while(len(self.inputs) == 0):
        time.sleep(0.001)
        failsafe += 1
        if(failsafe > 200):
          print("["+str(self.id)+"] input took to long exiting...")
          return -1
      val = self.inputs.pop()
      #print("["+str(self.id)+"]IN:  "+str(val))
      self.memory[a] = int(val)
      self.ip += 2
      return
      
    #Output
    if op%100 == 4:   
      a = self.opmode1(op)
      #print("["+str(self.id)+"]OUT: " + str(self.memory[a]))
      self.outputs.append(self.memory[a])
      self.ip += 2
      return
      
    #Jump-if-True
    if op%100 == 5:
      a,b = self.opmode2(op)
      if self.memory[a] != 0:
        self.ip = self.memory[b]
      else:
        self.ip += 3
      return
    
    #Jump-if-False
    if op%100 == 6:
      a,b = self.opmode2(op)
      if self.memory[a] == 0:
        self.ip = self.memory[b]
      else:
        self.ip += 3
      return
        
    #Less than
    if op%100 == 7:
      a,b,c = self.opmode3(op)
      if self.memory[a] < self.memory[b]:
        self.memory[c] = 1
      else:
        self.memory[c] = 0
      self.ip += 4
      return
      
    #Equals
    if op%100 == 8:
      a,b,c = self.opmode3(op)
      if self.memory[a] == self.memory[b]:
        self.memory[c] = 1
      else:
        self.memory[c] = 0
      self.ip += 4
      return
      
    print("error op code " + str(op) + "is not valid")
    return -1
    
  def run(self):
    while True:
      res = self.step()
      if res is not None:
        break;

class AmpChain:
  def __init__(self,code):
    self.amps = []
    for i in range(5):
      self.amps.append(Int_Machine(i,code.copy()))
  
#part 1  
  def run_p1(self,phases):
    for i in range(5):
      self.amps[i].inputs.append(phases[i])
      self.amps[i].start()
      
    self.amps[0].inputs.append(0)  
    for i in range(4):
      self.amps[i+1].inputs = self.amps[i].outputs
    
    self.amps[4].join()
    return self.amps[4].outputs
    
  def run_p2(self,phases):
    for i in range(5):
      self.amps[i].inputs.append(phases[i])
      self.amps[i].start()
      
    self.amps[0].inputs.append(0)
    #give programs some time to run before hooking up inputs
    time.sleep(0.1)
    for i in range(5):
      self.amps[(i+1)%5].inputs = self.amps[i].outputs
    
    self.amps[4].join()
    return self.amps[4].outputs
      
#phases = [0,1,2,3,4]  
#phases = [4,3,2,1,0]
#phases = [1,0,4,3,2]  
phases = [9,7,8,5,6]

#Create our amplifiers
thrustAmp = AmpChain(code_base)
print(thrustAmp.run_p2(phases))
a = input('press enter to continue')


#part 1
sig_max = 0
phase_max = [-1,-1,-1,-1,-1]
for phases in permutations(range(5)):
  thrustAmp = AmpChain(code_base)
  sig_out = thrustAmp.run_p1(phases)
  if sig_out[0] > sig_max:
    sig_max = sig_out[0]
    phase_max = phases

print('')
print(sig_max)
print(phase_max)
a = input('press enter to continue')

#part 2
sig_max = 0
phase_max = [-1,-1,-1,-1,-1]
for phases in permutations(range(5,10)):
  print(phases)
  thrustAmp = AmpChain(code_base)
  sig_out = thrustAmp.run_p2(phases)
  if len(sig_out) == 0:
    continue
  if sig_out[0] > sig_max:
    sig_max = sig_out[0]
    phase_max = phases

print('')
print(sig_max)
print(phase_max)
a = input('press enter to continue')