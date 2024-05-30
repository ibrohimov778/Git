import threading
import time

def eat_breacfast():
    time.sleep(3)

def drink_coffee():
    time.sleep(4)
    print('You drink coffee!')

def study():
    time.sleep(5)
    print('You Finish studying!')

x = threading.Thread(target=eat_breacfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()

# eat_breacfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())



