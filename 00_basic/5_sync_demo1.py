
import time

def task(id):
    print("start task -- ", id)
    time.sleep(2)
    print("end task", id)


start = time.time()
task(1)
task(2)
task(3)
task(4)
end = time.time()
print((end - start)*1000)