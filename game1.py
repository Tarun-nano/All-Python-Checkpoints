
#Prompt the user to withdraw money from the wallet to start the game. 
#a. For this problem, consider that the minimum balance to start the game is Rs.500.
#b. After one game is over add/deduct money from the account.
#c. Prompt the user if he/she would like to play one more time.
#i. If the user says “Yes” then check if the user has enough balance to play the game again. If not prompt the user to withdraw money from his wallet before the program starts the game. When the balance will be greater than Rs. 500 the program will automatically start the game.
#ii. If the user says “No”, then stop the game with a message “Have a wonderful day!”
import random
w=float(input("Please Enter Your Wallet Balance : "))
a=float(input("The Game will cost 500 INR if lost****Press 1 to Play "))
keep=0
if a==1:
    while(w>=500):
        print("Enjoy The Game *****Best Of Luck")
        keep=keep+1    
        if keep>4:
            print("maximum attempt reached")
            break

        c=random.randrange(1,20)
        guess=int(input("Take a Guess From 1 to 20 Einstein !!!"))
        if guess==c:
            if keep>4:
                
                w=w+1000
            print("YEAH!!!!! YOU WON!!!!!")
            print("Your balance is :",w)
           
    
        else:
            if keep==4:
                w=w-500
            print("You lost Your attempts remaining are and balance: ",4-keep,w)
            c=input(" To continue Press 1 ?")
            if w<500:
                print("Sorry no balance")
                break
            while c==1:
                keep=keep+1
                if keep>4:
                    print("maximum attempt reached")
                    break
                c=random.randrange(1,20)
                guess=int(input("Take a Guess From 1 to 20 Einstein !!!"))
                if guess==c:
                    if keep>3:
                        w=w+1000
                    print("YEAH!!!!! YOU WON!!!!!")
                    print("Your new balance is :",w)
                    if wal<500:
                        print("Please recharge your balance")
                        break
        