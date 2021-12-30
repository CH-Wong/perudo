import matplotlib.pyplot as plt
import numpy as np

from perudo import perudo
import os

plt.style.use('ggplot')

root = os.path.dirname(__file__)
player_counts = range(2,7)
p = perudo.Perudo()


def bid_probability():
    plt.figure()
    plt.title("Probability of correctly bidding")
    plt.xlabel("k [# occurences]")
    plt.ylabel("Probability [%]")
    

    for count in player_counts:
        print(count)
        p.set_player_count(count)
        print(p.players, len(p.players))

        probabilities_two_to_six = []
        probability_ace_palifico = []
        
        for occurences in range(5*count):
            print(count, occurences)
            prob = 100*p.calculate_bid_probability({2:occurences})
            probabilities_two_to_six.append(prob)
            prob = 100*p.calculate_bid_probability({1:occurences})
            probability_ace_palifico.append(prob)
        
        line, = plt.plot(probabilities_two_to_six, label=f"#dice = {5*count}")
        plt.plot(probability_ace_palifico, label=f"(palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()
    

    plt.savefig(root + r"\output\id_probability.png")


def normalized_bid_probability():
    plt.figure()
    plt.title("Normalized probability of correctly bidding")
    plt.xlabel("#occurences/#dice []")
    plt.ylabel("Probability []")

    for count in player_counts:
        p.set_player_count(count)

        probabilities_two_to_six = []
        probability_ace_palifico = []
        normalized_occurence_data = []
        for occurences in range(5*count):
            print(count, occurences)
            normalized_occurence_data.append(occurences/(5*count))
            probabilities_two_to_six.append(p.calculate_bid_probability({2:occurences}))
            probability_ace_palifico.append(p.calculate_bid_probability({1:occurences}))
        
        line, = plt.plot(normalized_occurence_data, probabilities_two_to_six, label=f"#dice = {5*count}")
        plt.plot(normalized_occurence_data, probability_ace_palifico, label=f"(palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()

    plt.savefig(root + r"\output\bid_probability_normalized.png")

def calza_probability():
    plt.figure()
    plt.title("Probability for a correct 'calza'")
    plt.xlabel("k [# occurences]")
    plt.ylabel("Probability [%]")
    for count in player_counts:
        p.set_player_count(count)
        probabilities_two_to_six = []
        probability_ace_palifico = []
        
        for occurences in range(5*count):
            print(count, occurences)
            prob = 100*p.calculate_calza_probability({2:occurences})
            probabilities_two_to_six.append(prob)
            prob = 100*p.calculate_calza_probability({1:occurences})
            probability_ace_palifico.append(prob)
        
        line, = plt.plot(probabilities_two_to_six, label=f"#dice = {5*count}")
        plt.plot(probability_ace_palifico, label=f"(palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()
    plt.savefig(root + r"\output\calza_probability.png")



def main():
    bid_probability()
    normalized_bid_probability()
    calza_probability()

    plt.show()

if __name__ == "__main__":
    main()