import random
computer_choice = (random.randint(1,3))
my_choice = input("enter a number 1 to 3 : ")
my_number = int(my_choice)
print(computer_choice)
if computer_choice == my_number :
    print("you win")
else:
    print("you loose,,computer win")