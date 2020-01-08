def GetFuelNeeded(mass):
  return (mass//3) - 2

def DifferentialFuel(mass):
  base = GetFuelNeeded(mass)
  additional = 0
  if base > 0:
    additional = DifferentialFuel(base)
  return base + (additional if additional > 0 else 0);
  
#Check
print('Check 1')
print(DifferentialFuel(14))
print('Check 2')
print(DifferentialFuel(1969))
print('Check 3')
print(DifferentialFuel(100756))  
  
path = 'input.txt'
p1 = 0
p2 = 0
with open(path) as input:
  while True:
    line = input.readline()
    if not line:
      break
    p1 = p1 + GetFuelNeeded(int(line))
    p2 = p2 + DifferentialFuel(int(line))

print('Problem 1')    
print(p1)
print('Problem 2')
print(p2)