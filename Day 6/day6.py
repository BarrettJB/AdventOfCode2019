class SpaceRock:
  def __init__(self,name,parent):
    self.Name = name
    self.Parent = parent
    if not parent is None:
      parent.Children.append(self)
    self.Children = []
  
  def CountOrbits(self,level):
    orbits = level
    for child in self.Children:
      #print(self.Name + ')' + child.Name)
      orbits += child.CountOrbits(level + 1)
    
    return orbits
    
  def ListElders(self, elders):
    elders.append(self.Name)
    if self.Parent is None:
      return elders
    else:
      return self.Parent.ListElders(elders)
    

path = 'input.txt'
  
rocks = {}
with open(path) as file:
  while True:
    line = file.readline()
    line = line.rstrip()
    print(line)
    if not line:
      break
    parent,child = line.split(')')
    if parent in rocks:
      if not child in rocks:
        #print('Adding new child ['+child+'] to parent ['+parent+']')
        rocks[child] = SpaceRock(child,rocks[parent])
      else:
        rocks[parent].Children.append(rocks[child])
        rocks[child].Parent = rocks[parent]
    else:
      if not child in rocks:
        #print('Adding new child ['+child+'] to new parent ['+parent+']')
        rocks[parent] = SpaceRock(parent, None)
        rocks[child] = SpaceRock(child, rocks[parent])
      else:
        #print('Adding child ['+child+'] to new parent ['+parent+']')
        rocks[parent] = SpaceRock(parent, None)
        rocks[parent].Children.append(rocks[child])
        rocks[child].Parent = rocks[parent]

#part 1
sum = 0
for rock in rocks:
  srock = rocks[rock]
  if srock.Parent is None:
    #print(srock.CountOrbits(0))
    sum += srock.CountOrbits(0)

print(sum)
input()

#part 2
you_path = []
san_path = []
print(rocks['YOU'].Parent.ListElders(you_path))
print(rocks['SAN'].Parent.ListElders(san_path))
print(len(set(you_path)-set(san_path)) + len(set(san_path)-set(you_path)))
input()

