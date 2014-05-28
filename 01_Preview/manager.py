#!python
# cd c:\Users\tmulher\Documents\_dev\Python\PP4E\Preview
# cd /c/Users/tmulher/Documents/_dev/Python/PP4E/Preview

# PP4E\Preview\person_start.py
from person import Person

class Manager(Person):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
        
    def giveRaise(self, percent, bonus=0.1):
        #self.pay *= (1.0 + percent + bonus)
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    import os
    os.system('cls')
    #print(tom.lastName(), ' ', tom.pay)
    #tom.giveRaise(.20)
    print('I am ' + tom.name + '.  I am a ' + tom.job + ' and I get paid ' + str(tom.pay) + '.')
    print('\n' + str(tom))