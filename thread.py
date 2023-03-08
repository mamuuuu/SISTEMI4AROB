from time import sleep
from threading import Thread

class Task(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
    
    def run(self):
        print(f"Start {self.id}")
        sleep(1)
        print(f"End {self.id}")

#t1 = Task(1)
#t1.start()

#t2 = Task(2)
#t2.start()

#t1.join()

t = []
for i in range(0,10):
    t_ = Task(i)
    t.append(t_)
    t[i].start()

    

