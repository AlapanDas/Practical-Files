import time
start=time.time()
st=1234
passw=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                passw=(i*1000)+(j*100)+(k*10)+l
                if st==passw:
                    print("PASS FOUND-",passw)
end=time.time()
print(end-start)                
