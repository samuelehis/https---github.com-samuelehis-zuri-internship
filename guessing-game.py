

our_fav_number = "10"

guess_num = input("Please enter your guessing number : ")

guess_num = int(guess_num)

#print (guess_num)

try: 
    guess_num = int(guess_num)

    if guess_num == 10:
        print ("Congratulations! You guessed the number right. Our guess number is : " + str(guess_num))

    elif guess_num < 10: 
            print("Ouch! Your guess number is "+ str(guess_num) + " which is less than the number you entered.")

    else:
        print("Ouch! Your guess number is " + + str(guess_num) + " which is higher than the number you entered " )

except: 
        print("Sorry! That is not a number")

        