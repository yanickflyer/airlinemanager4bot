import launch, threading

thread1=threading.Thread(target=launch.launch.depart_maintenance)
thread2=threading.Thread(target=launch.launch.fuel)

thread1.start()
thread2.start()

while True:
    pass