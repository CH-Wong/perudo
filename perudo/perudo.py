import names

class Perudo:
    players = {}
    current_guess = []
    trust_threshold = 0.5

    def __init__(self, n_players=2):
        
        
        for i in range(n_players):
            self.add_players()
            


    def add_player(self, dice=5):
        # Prevent double names from generating duplicate keys in player dictionary
        name = ''
        while name in self.players.keys():
            name = names.get_first_name()
            
        self.players[name] = dice
        print(f"Added {name} to player list with {dice} dice.")


    def remove_player(self, name):
        try:
            del self.players[name]
        except KeyError:
            print(f"Error in remove_player: Player {name} does not exist.")


    def remove_dice(self, name):
        # Check if there are dice left by seeing if 
        if self.players[name][-1] > 0:
            self.players[name].append(self.players[name][-1] + 1)

        else: 
            print("Player no longer has dice. ")

    def add_dice(self, name):
        # Check if player doesn't already have maximum dice, and if player is still playing
        if self.players[name][-1] < 5 and self.players[name][-1] > 0:
            self.players[name].append(self.players[name][-1] + 1)
        elif self.players[name][-1] == 5:
            print(f"Player {name} already has the maximum of 5 dice.")
        else:
            print(f"Error in add_dice: player {name} has either 0 dice or more than 5 dice.")


def calc_p(N_dices, N_bid, N_hand):
    p_array = []
    if N_bid <= N_hand:
        print("Hand contains more than bid.")
        return 1
    else:
        N_total = N_dices - N_hand
        print(N_bid-N_hand)
        p = 0

        for number in range(0,N_bid - N_hand + 1):
            prob = (1/6)**number * (5/6)**(N_total-number)
            print(prob)
            p += prob

    return p

def main():
    p = Perudo()


if __name__ == '__main__':
    main()
