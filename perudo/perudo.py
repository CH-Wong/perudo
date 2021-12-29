import names

class Perudo:
    # Dictionary containing the player names and the number of dices they have
    players = {}
    # Dictionary containing the player names and the dices they have thrown this round
    thrown_dices = {}
    # List of all dice throws 
    throw_history = [] 
    
    # 
    last_guess = {}
    
    # Computer trust level
    trust_threshold = 0.5

    # Palifico state variable
    palifico = False

    


    def __init__(self, n_players=2):
        for i in range(n_players):
            self.add_players()
            

    def add_player(self, name=None, dice=5):
        # If no name is passed, generate a random name using the names library.
        if name == None:
            # While loop ensures the generated name is unique. 
            # TODO: For large number of players the list could be exhausted, causing infinite loop!
            while name in self.players.keys():
                name = names.get_first_name()
            
        self.players[name] = dice
        print(f"Added {name} to player list with {dice} dice.")


    def remove_player(self, name):
        # Remove selected player
        # Catch unknown player IDs, and print an error to log instead.
        try:
            del self.players[name]
        except KeyError:
            print(f"Error in remove_player: Player {name} does not exist.")


    def remove_dice(self, name):
        # After every round, a dice is removed or gained. 
        # When removing a dice, set the palifico setting to False. 
        
        self.palifico = False

        # Check if there are dice left by seeing if 
        if self.players[name][-1] > 0:
            self.players[name].append(self.players[name][-1] - 1)
        else: 
            print(f"Player {name} no longer has dice and has been eliminated. ")
        
        if self.players[name] == 1:
            self.palifico = True


    def add_dice(self, name):
        # One possible round ending is with "calza", meaning that a dice could be added to someones hand.
        # After every round, palifico state should in principle be reset to False, unless someone happens drop down to 1 dice again.

        self.palifico = False

        # Check if player doesn't already have maximum dice, and if player is still playing
        if self.players[name][-1] < 5 and self.players[name][-1] > 0:
            self.players[name].append(self.players[name][-1] + 1)
        elif self.players[name][-1] == 5:
            print(f"Player {name} already has the maximum of 5 dice.")
        else:
            print(f"Error in add_dice: player {name} has either 0 dice or more than 5 dice.")


    def calculate_probability(self, guess, name=None, throw=None):
        # Initialize the probability of the guess as 100%
        probability = 1

        # Get the total number of dice in the game from our players dictionary for probability calculation
        number_of_dice = sum(self.players.values())
        
        # Split the guess in the number and the occurences
        [(number, occurences)] = guess.items()




        
        return probability


def main():
    p = Perudo()


if __name__ == '__main__':
    main()
