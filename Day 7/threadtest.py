import threading
import time

class MyThread(threading.Thread):
  def __init__(self,id,delay,loops):
    self.id = id
    self.delay = delay
    self.loops = loops
    super(MyThread,self).__init__()
    
  def run(self):
    for i in range(self.loops):
      print("ID:"+str(self.id))
      time.sleep(self.delay)
    print("ID:"+str(self.id)+" done")
      
t1 = MyThread(1,1,12)
t2 = MyThread(2,2,6)
t3 = MyThread(3,4,3)

t1.start()
t2.start()
t3.start()
