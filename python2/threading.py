from threading import *
class MyThread(Thread):
 def run(self):
    for i in range(5):
      print("this is child class")
t=MyThread()
t.start()
for i in range(5):
  print("\nthis is parent thread")
