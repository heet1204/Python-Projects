import random
   
def calculate_score(cards):
    """ calculates the score of the passed cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    """ Generates a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score, bot_score):
    if user_score == bot_score:
        return "\nDraw"
    elif bot_score == 0:
        return "\nLose, Opponent has the Blackjack!!!"
    elif user_score == 0:
        return "\nWin with a Blackjack!!"
    elif user_score > 21:
        return "\nYou went over, you lose"
    elif bot_score > 21:
        return "Opponent went over, you win"
    elif user_score > bot_score:
        return "\nYou Win"
    else:
        return "\nYou Lose"
    
def play_game():
    user_cards = []
    bot_cards = []
    is_game_over = True

    for _ in range(2):
        user_cards.append(deal_card())
        bot_cards.append(deal_card())

    # code for User to draw cards
    while is_game_over:
        
        user_score = calculate_score(user_cards)
        bot_score =  calculate_score(bot_cards)
        print(f"Your Cards : {user_cards} || Current_score = {user_score}")
        print(f"Computer's first Card : {bot_cards[0]}") 

        if user_score == 0 or user_score > 21 or bot_score == 0:
            is_game_over = False
            
        else:
            user_input = input("\nType 'y ' to get another card or type 'n' to pass : ")
            if user_input == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = False

    # code for computer to draw cards
    while bot_score !=0 and bot_score < 17:
        bot_cards.append(deal_card())
        bot_score =  calculate_score(bot_cards)

    print(f"\nYour final hand : {user_cards} || User Score : {user_score}")
    print(f"Computer's final hand : {bot_cards} || Computer Score : {bot_score}")
    print(compare(user_score, bot_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n' : ") == "y":
    print()
    play_game()
