import random
    
cards = [1,2,3,4,5,6,7,8,9,10,10,10]
player = 0

dealer = random.choice (cards)
dealer2 = random.choice (cards)
player = random.choice (cards) 
player2 = random.choice (cards) 
total = player + player2
dealer_total = dealer + dealer2
print ("do you want to play black jack?")
print (" let me explain how the cards will diplay. I will automatically give you two cards and show you the dealer's up card. From there you can either decide to 'hit' or 'stay'. if you decide to 'hit' then it will display the total of the first two cards then the number under that is the random card that you were given and then the number shown under that is the sum of the two numbers displayed above") 
answer1= input()
if answer1 == "yes" or answer1 == "Yes" or answer == "YES": 
    print ("your two cards are:" )
    print (player,"and", player2) 
    print("Dealers upcard is:")
    print (dealer)
    answer = input ("do you want to hit? or stay")
    while answer == "hit" or answer == "yes" or answer == "Hit":
        if player > 21:
            print(" you went over 21! you loose")
            break
        player1 = total
        print (player1)
        player = player + player2
        player3 =random.choice(cards)
        print(player3) 
        total = player + player3
        print(total)
        if player == 21:
            print (" you won!" )
            break
        if player > 21:
            print(" you went over 21! you loose")
            break

        answer = input ("do you want to hit? or stay")

    if answer == "stay" or answer == "Stay" or answer == "No":
        print ("remember your total is:")
        print (total)
        print ("These are the dealers cards:") 
        print (dealer, "and", dealer2)
        print ("the dealers total:")
        print (dealer_total)
        while dealer_total <= 17:
            dealer3= random.choice(cards)
            print ("this is the dealer's new card")
            print (dealer3)
            dealer_total = dealer_total + dealer3
            print ("this is the dealer's new total")
            print(dealer_total)
    print ("your total is:")
    print (total)
    print ("The dealer's total is:")
    print (dealer_total)
 
