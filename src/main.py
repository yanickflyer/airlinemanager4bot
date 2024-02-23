import launch, threading


thread1=threading.Thread(target=launch.launch.depart_maintenance)
thread2=threading.Thread(target=launch.launch.fuel)
thread3=threading.Thread(target=launch.launch.check_marketing)

thread1.start()
thread2.start()
thread3.start()


while True:
    pass