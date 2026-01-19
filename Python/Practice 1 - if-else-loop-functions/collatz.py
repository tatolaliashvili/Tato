import time, sys

def collatz():
    global number
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1  

first_time = True

while True:
    try:
        if first_time:
            print('Enter a number (Ctrl+C to quit):')
            first_time = False
        else:
            print('\nEnter new number:')
            
        number = int(input('> '))
        
        print(number, end=' ')
        
        while number != 1:
            collatz()
            print(number, end=' ')
            time.sleep(0.05)
            
        print()
    except KeyboardInterrupt:
        sys.exit()        