from time import sleep
def collatz(num):
    step = 0
    numlist = []
    print(num)
    while num != 1:
       if num < 1:
           print('error')
           break
       if num % 2 == 0:
           num /= 2
           numlist.append(num)
           step += 1
       else:
           num = num*3+1
           numlist.append(num)
           step += 1
    return numlist, step

while True:
    inn = int(input('What number would you like to enter?:'))
    numlist, steps = collatz(inn)
    print('It took {} steps for {} to be reduced to one!'.format(steps, inn))
    inn = input('would you like to see the steps individually?(y/n):')
    if inn == 'y':
        for step in numlist:
            print(step)
            sleep(0.1)
