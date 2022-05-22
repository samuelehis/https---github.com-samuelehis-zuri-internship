import random

#generate a random 5 numbers between 1 and 100
randomlist = random.sample(range(1, 100), 5)
print(randomlist)

#randomly select a number from the 5 numbers above
our_fav_number = random.choice(randomlist)

user_name = input("Please enter your name : ")

#accept number from the player
guess_num = input("Hi " + user_name + " please enter your choice number : ")

#convert the player's number from a string to an integer
guess_num = int(guess_num)

#print (guess_num)

try: 
    guess_num = int(guess_num)

    if guess_num == our_fav_number:
        print ("Congratulations! You guessed the number right. Our guess number is : " + str(our_fav_number))

    elif guess_num < our_fav_number: 
            print("Ouch! Our selected number is "+ str(our_fav_number) + " is less than the number you guessed.")

    else:
        print("Ouch! The selected number is " + str(our_fav_number) + " is higher than the number you guessed " )

except: 
        print("Sorry! That is not a number")

        