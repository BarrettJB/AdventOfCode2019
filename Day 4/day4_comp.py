in_l = 156218
in_h = 652527

#could just start at 156666
def GeneratePassword(low, high, level, flag_double):
  

low = [int(d) for d in str(in_l)]
high = [int(d) for d in str(in_h)]

for d1 in range(low[0],high[0]):
  for d2 in range(min(low[1],d1),high[1]):