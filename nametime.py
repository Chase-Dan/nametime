name = input('Enter Name:')
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print ('Good Morning ' + name)
print ('The current time in Jacksonville, FL is ' + current_time)
