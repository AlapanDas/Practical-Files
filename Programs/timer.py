import time,threading,random
a=random.randint(-100,100)
b=random.randint(-100,100)
print("FIND THE SUM OF ",a,"+",b)
print("U have 10 secs to do this")
def quiz():
    print("The answer is ",(a+b))
for i in range(10):
    time.sleep(1)
    print(i+1,end='\r')
timer=threading.Timer(0,quiz)
timer.start()
