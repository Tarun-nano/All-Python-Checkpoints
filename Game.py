#Prompt the user to withdraw money from the wallet to start the game. 
#a. For this problem, consider that the minimum balance to start the game is Rs.500.
#b. After one game is over add/deduct money from the account.
#c. Prompt the user if he/she would like to play one more time.
#i. If the user says “Yes” then check if the user has enough balance to play the game again. If not prompt the user to withdraw money from his wallet before the program starts the game. When the balance will be greater than Rs. 500 the program will automatically start the game.
#ii. If the user says “No”, then stop the game with a message “Have a wonderful day!”
wal=float(input("Please Enter Your Wallet Balance"))
a=float(input("The Game cost 500 INR ****Press 1 to Play"))
if a==1:
    while(wal>=500):
        print("Enjoy The Game *****Best Of Luck")
        print("YEAH!!!!! YOU WON!!!!!")
        wal=wal-500
        x=int(input("Do You Want To Contnue ??******Press 1 To Continue")
        
        if x==1:
            wal=wal-500
        else:
            print("Thank You For Playing")
            break
    
    
    
