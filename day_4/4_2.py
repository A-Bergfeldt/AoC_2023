import re

def win_counter(cards, card_nr):
    if card_nr >= len(cards):
        return 0

    n_wins = 0

    card = re.split('\:|\|', cards[card_nr])
    win_nrs = re.findall('\d+', card[1])
    nrs = re.findall('\d+', card[2])
    for nr in nrs:
        if nr in win_nrs:
            n_wins += 1
    
    total_wins = 0
    if n_wins:
        for i in range(n_wins):
            total_wins += win_counter(cards, card_nr + i + 1)

    return total_wins + 1

def main():
    with open('day_4\\input.txt', 'r') as f:
        cards = f.readlines()
        
        total_cards = 0
        for i in range(len(cards)):
            total_cards += win_counter(cards, i)
        
    print(f'Total scratchcards = {total_cards}')

if __name__ == '__main__':
    main()