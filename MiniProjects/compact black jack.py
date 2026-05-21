
money = int(input("How much money do you want to have?: "))
print( )
s = 1
import random
while s < 10:
    if money == 0:
        exit()

    print("Welcome to Python Blackjack!")
    print(" ")
    print("Your balance: " + str(money))
    print(" ")
    play = input("Do you want to play?: ")
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    play.lower()
    if play == "yes":
        i = 1
        hitn = 4
        bet = int(input("How much do you want to bet?: "))
        money = money - bet
        ip=[0,1,2,3,4,5,6,7,8,9,10,11,12]
        random.shuffle(ip)
        dealer= cards[ip[0]]
        player= cards[ip[1]] + cards[ip[3]]

        def playerlose():
            print(" ")
            print("Dealer: " + str(dealer))
            print(" ")
            print("You: " + str(player))
            print(" ")
            print("YOU LOSE!")
            print(" ")

        def playerwin():
            print(" ")
            print("Dealer: " + str(dealer))
            print(" ")
            print("You: " + str(player))
            print(" ")
            print("YOU WON!")
            print(" ")


        def playertie():
            print(" ")
            print("Dealer: " + str(dealer))
            print(" ")
            print("You: " + str(player))
            print(" ")
            print("YOU TIED!")
            print(" ")

        while i<10:
            if player >= 22:
                playerlose()
                i = i + 10
            else:
                print(" ")
                print("Dealer: " + str(dealer))
                print(" ")
                print("You: " + str(player))
                print("Your bet: "+ str(bet))
                hit = input("Do you want to hit? ")
                hit.lower()
                if hit == "yes":
                    player = player + cards[ip[hitn]]
                    hitn = hitn + 1
                if hit == "no":
                    dealer = dealer + cards[ip[2]]
                    if dealer < 16:
                        dealer = dealer + cards[ip[hitn]]
                        if dealer > 22 or player > dealer:
                            playerwin()
                            bet = bet * 2
                            i = i + 10
                        if player < dealer:
                            playerlose()
                            i = i + 10
                        if player == dealer:
                            playertie()
                            money = money + bet
                            i = i + 10
                    if dealer > 22 or player > dealer:
                        playerwin()
                        bet = bet * 2
                        i = i + 10
                    if player < dealer:
                        playerlose()
                        i = i + 10
                    if player == dealer:
                        playertie()
                        money = money + bet
                        i = i + 10


    else:
        print(" ")
        print("Good bye!")
        s = s+10





