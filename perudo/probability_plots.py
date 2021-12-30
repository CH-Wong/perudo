import matplotlib.pyplot as plt
import numpy as np

from perudo import perudo

plt.style.use('ggplot')



def bid_probability():
    player_counts = range(2,7)
    [print(x) for x in player_counts]
    # print(player_counts)

    plt.figure()
    plt.xlabel("k [# occurences]")
    plt.ylabel("Probability [%]")
    p = perudo.Perudo()

    for count in player_counts:
        p.set_player_count(count)
        
        probabilities_two_to_six = []
        probability_ace_palifico = []
        
        for occurences in range(5*count):
            print(count, occurences)
            prob = 100*p.calculate_bid_probability({2:occurences})
            probabilities_two_to_six.append(prob)
            prob = 100*p.calculate_bid_probability({1:occurences})
            probability_ace_palifico.append(prob)
        
        line, = plt.plot(probabilities_two_to_six, label=f"#dice = {5*count}")
        plt.plot(probability_ace_palifico, label=f"#dice = {5*count} (palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()


def normalized_bid_probability():
    player_counts = range(2,7)
    [print(x) for x in player_counts]
    # print(player_counts)

    plt.figure()
    plt.xlabel("#Occurences/number of dice []")
    plt.ylabel("Probability []")
    p = perudo.Perudo()

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
        plt.plot(normalized_occurence_data, probability_ace_palifico, label=f"#dice = {5*count} (palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()


def calza_probability():
    print('CALZA-----------\n\n')
    player_counts = range(2,7)

    plt.figure()
    plt.xlabel("k [# occurences]")
    plt.ylabel("Probability [%]")
    p = perudo.Perudo()

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
        plt.plot(probability_ace_palifico, label=f"#dice = {5*count} (palifico/aces)", linestyle=":", color=line.get_color())

    plt.legend()



def main():
    bid_probability()
    normalized_bid_probability()
    calza_probability()

    plt.show()

if __name__ == "__main__":
    main()