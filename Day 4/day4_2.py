in_l = 156218
in_h = 652527
count = 0

for pswd in range(in_l, in_h):
  digits = [int(d) for d in str(pswd)]
  flag_double = False
  flag_increase = True
  rep_count = 0
  flag_triple = False
  for i in range(len(digits)-1):
  
    if(digits[i] == digits[i+1]):
      rep_count += 1
      
    if(digits[i] != digits[i+1]):
      if(rep_count == 1):
        flag_double = True
      rep_count = 0
    else:
      flag_double_delay = False
      
    if(digits[i] > digits[i+1]):
      flag_increase = False
  
  if(rep_count == 1):
        flag_double = True
        
  if(flag_double and flag_increase):
    print(str(pswd) + " is a match")
    count += 1
    
print(str(count) + " possible passwords")
input("press enter to continue")    