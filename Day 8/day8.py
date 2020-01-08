import numpy as np
from matplotlib import pyplot as plt

path = 'input.txt'
with open(path) as file:
  line = file.readline()
  line = line.rstrip()
  
min_count = [151,0,0];
#part 1
for i in range(len(line)-150):
  count = [0,0,0];
  layer = line[i:i+150]
  for p in layer:
    count[int(p)] += 1
  
  if count[0] < min_count[0]:
    min_count = count;
  
  #print(count)
print(min_count)
print(min_count[1]*min_count[2])
input()

#part2
numLayers = len(line)//150
img = np.ones((25,6))*2
for i in range(numLayers):
  for j in range(150):
    x = j//6
    y = j%6
    if line[i*150+j] != 2 and img[x,y] == 2:
      img[x,y] = int(line[i*150+j])
  print(img)

print(img)
    
#display the image      
for x in range(25):
  for y in range(6):
    if(img[x,y] == 1):
      plt.plot(x,y,'ro')
    if(img[x,y] == 0):
      plt.plot(x,y,'bo')
      
plt.show()