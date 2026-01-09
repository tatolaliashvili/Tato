import random

while True:
    def get_answer(answer_number):
        if answer_number == 1:
            return 'It is certain'
        elif answer_number == 2:
            return 'Yes'
        elif answer_number == 3:
            return 'very doubtful'
        elif answer_number == 4:
            return 'my reply is no'
        elif answer_number == 5:
            return 'no'

    print('Ask a yes or no question:')
    input('>')
    r = random.randint(1,5)
    fortune = get_answer(r)
    print(fortune)