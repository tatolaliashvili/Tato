users = {}

def register():
    while True:
        username = input('Username must be atleast 6 characters: ')
        if len(username) < 6:
            print('Username is too short, try again')
            continue
        password = input('Enter your pin(only numbers): ')
        if not password.isdigit():
            print("PIN must be only numbers")
            continue

        users[username] = password
        print('You have successfully registered!')
        break

def login():
    while True:
        username = input('Enter your username: ')
        if username not in users:
            print('User not found!')
            continue
        password = input('Enter you pin: ')
        if users[username] == password:
            print('You have logged successfully!')
            break
        else:
            print('Wrong details')

def user_input():
    user_choose = input('> ')
    if user_choose == '1':
        print('Your total will be ', sedan_price)
    elif user_choose == '2':
        print('Your total will be ', suv_price)
    elif user_choose == '3':
        print('Your total will be ', truck_price)



print('Welcome to the car cleaning service! \nRegister so you can give us all the details')
register()
login()

sedan_price = '15.99$'
suv_price = '25.99$'
truck_price = '45.99$'

print('Our prices are the following:\n' + '1.Sedan price: ',sedan_price,' 2.SUV price: ',suv_price,' 3.Truck price: ', truck_price)
user_input()