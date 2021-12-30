import names
import random
import math

class Perudo:
    # Dictionary containing the player names and the number of dices they have
    players = {}
    # Dictionary containing the player names and the dices they have thrown this round
    rolled_dice = {}
    # List of all dice throws 
    roll_history = [] 
    
    count_history = []

    last_guess = {}
    
    # Computer trust level
    trust_threshold = 0.5

    # Palifico state variable
    palifico = False

    
    def __init__(self, n_players=2, seed=None, debug=True):
        # Optional argument to be used as seed for random number generator. If nothing is passed, system time is used
        random.seed(seed)
        self.debug = debug
        for i in range(n_players):
            self.add_player()
            
    def add_player(self, name=None, dice=5):
        # If no name is passed, generate a random name using the names library.
        if name == None:
            # While loop ensures the generated name is unique. 
            # TODO: For large number of players the list could be exhausted, causing infinite loop!
            while name in self.players.keys() or name == None:
                name = names.get_first_name()
            
        self.players[name] = dice
        self.rolled_dice[name] = []
        self.log(f"Added {name} with {dice} dice.")

    def remove_player(self, name):
        # Remove selected player
        # Catch unknown player IDs, and print an error to log instead.
        try:
            self.log(f"Removing {name}...")
            del self.players[name]
        except KeyError:
            print(f"Error in remove_player: Player {name} does not exist.")

    def reset_dice(self, dice = 5):
        for player in self.players.keys():
            self.players[player] = dice

    def set_player_count(self, target):
        if len(self.players) > target:
            excess_players = len(self.players) - target
            for i in range(excess_players):
                self.remove_player(random.choice(list(self.players.keys())))
                
        elif len(self.players) < target:
            shortage_players = target - len(self.players)
            for i in range(shortage_players):
                self.add_player()
        else:
            self.log(f"Player count is already {target}!")

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

    def roll_dice(self):
        # Simulate dice-throw for each player
        # Dice throws are saved as dict in <thrown_dice>

        for name, number_of_dice in self.players.items():
            roll = []
            for i in range(number_of_dice):
                roll.append(random.randint(1, 6))

            self.rolled_dice[name] = roll

    def count_occurences(self):
        # Initialize empty counter
        # Initialized as dict because then a 1 can use index 1 instead of 0
        count = {
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0
        }

        # Count the occurences of the numbers 1-6 in all the dices rolled. 
        # Loop through each players dice roll
        for roll in self.rolled_dice.values():
            # Loop through each dice in the set of dice
            for dice in roll:
                # Add the dice to the correct number
                count[dice] += 1

        return count

    def calculate_calza_probability(self, guess, name=None):
        # Get the total number of dice in the game from our players dictionary for probability calculation
        n = sum(self.players.values())
        
        # Split the guess in the number and the occurences <k>
        [(number, k)] = guess.items()

        # Calculate the probability for the dice throw.
        if number == 1 or self.palifico:
            p = 1/6
        elif number > 1 and number <= 6:
            p = 2/6
        else:
            raise ValueError(f"Error in calculate_probability(): invalid number {number} given, must be between 1-6.")
        
        self.log(f"{n}, {k}, {p}")
        probability = combinations(n, k)* p**k * (1-p)**(n-k) 
        
        return probability

    def calculate_bid_probability(self, guess, name=None):
        # Get the total number of dice in the game from our players dictionary for probability calculation
        n = sum(self.players.values())
        
        # Split the guess in the number and the occurences <k>
        [(number, k)] = guess.items()

        if name != None:
            n -= self.players[name]
            k -= self.rolled_dice[name]
            if k < 0:
                k = 0
        
        

        # Calculate the probability for the dice throw.
        # Given that most realistic dice-throws will have low occurences (i.e. low risk), we will calculate the inverse probability instead.
        # Subsequently, we will subtract the reverse probability from 100%
        inverse_probability = 0

        if number == 1 or self.palifico:
            p = 1/6
        elif number > 1 and number <= 6:
            p = 2/6
        else:
            raise ValueError(f"Error in calculate_probability(): invalid number {number} given, must be between 1-6.")

        # Apply binomial theorem
        for x in range(k):
            inverse_probability += combinations(n, x)* p**x * (1-p)**(n-x) 

        self.log(f"{n}, {k}, {p}")
        return 1 - inverse_probability

    def log(self, string):
        if self.debug:
            print(string)


def combinations(n, k):
    # Standard formula for number of combinations (selection of k from a group of n, without accounting for the selection order)
    # https://en.wikipedia.org/wiki/Combination

    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))

def main():
    p = Perudo(n_players=9)
    p.roll_dice()
    count = p.count_occurences()
    

if __name__ == '__main__':
    main()
