import threading
import time

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
