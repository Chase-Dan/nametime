name = input('Enter Name:')
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print ('Hello ' + name)
print ('Your current local time is ' + current_time)

fact = int(input('Would you like to hear a fact? Enter 1 for yes or 2 for no:'))

if fact == 1:
    import random
    my_list = ['Snails can nap for up to 3 years.', 'Hippopotamus milk is pink.', 'The smallest country in the world takes up .2 square miles: Vatican City', 'A tsunami can travel as fast as a jet.' ,'Before 1913 parents could mail their kids to grandmas - through the postal service.']
    rannum = random.choice(my_list)
    print (rannum)

elif fact == 2:
    print ('Have a nice day!!!')

else: 
    print ('That was not an option.  Next time follow the rules.')