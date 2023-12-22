import random

class PokerPlayer():
    def __init__(self , player_id , player_purse , player_position , player_hand):
        self.position = player_position
        self.id = player_id
        self.player_purse = player_purse
        self.player_hand = player_hand

    def player_info(self):
        return [self.id , self.player_purse , self.position , self.player_hand]

class Cards():
    def __init__(self):
        self.community_cards = []
        self.cards = ["Diamonds", "Spades", "Hearts", "Clubs"] 
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] 
        self.colors = ["black" , "red"]
        

    def PickCard(self):
        # storing the signs and the rank value 

        color = random.choices(self.colors)
        card = random.choices(self.cards) 
        rank = random.choices(self.ranks) 

        if [card , rank , color] in self.dealt_cards:
            re_rank = random.choices(self.ranks)
            re_card = random.choices(self.cards)
            self.dealt_cards.append([re_card , re_rank , color]) 
            return([re_card , re_rank , color]) 
        else:
            self.dealt_cards.append([card , rank , color])  
            return([card , rank , color]) 



class PokerGame():
    def __init__(self , player_num , player_purse):
        self.game_state = 100
        self.players = player_num
        self.player_purse = player_purse
        self.dealt_cards = []

    def deal(self):
        pass
    
    def create_players(self):
        # p_type = ""
        human = PokerPlayer("user" , self.player_purse , 0 , [])
        dealer = PokerPlayer("dealer" , random.randint(300, 500) , 1 , [])
        player_array = [ human.player_info() , dealer.player_info() ]
        for i in range(self.players):
            player_array.append(PokerPlayer(f"computer {i}" , random.randint(300, 500) , i , []).player_info())

        return player_array
    
    def deal_cards(self):
        pass

    def start_game(self):
        self.create_players()

    
    


if __name__ == "__main__":

    player_number = int(input("Enter the number of players in the game: "))

    player_purse = int(input("Enter the amount of money you have to gamble: "))

    new_game = PokerGame(player_number , player_purse)

    print(new_game.create_players())
