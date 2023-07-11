from random import randint
import math
#The user inputs a range of two numbers ..normally the lower bound and upper bound
lower_bound= int(input('Enter the lower bound interger !'))
upper_bound = int(input('Enter the upper bound interger !'))
base_gueses = int(math.log(upper_bound - lower_bound + 1,2))
print(f' You have {base_gueses} attempts in your basket !!!!')
computer_number = randint(lower_bound,upper_bound)
count = 0
while(count < base_gueses):
    guesed_number = int(input('Guese your number ..!'))
    if guesed_number > computer_number:
        print(f'{guesed_number} Too High !! try again')
        guesed_number = int(input('Guese your number ..!'))
    elif guesed_number < computer_number:
        print(f'{guesed_number} Too Loo !! try again')
        guesed_number = int(input('Guese your number ..!'))
    else:
        print(f'{guesed_number} is correct !!,congradulations  you made in {count} trys !!')
        break

    count = count + 1

print(f'Your attempts are over !! try some other time')    

    