def main():
    card_importance = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1
    }

    # Helper function to sort hands based on card importance
    def hand_key(hand):
        return [card_importance[card] for card in hand]

    with open('day_7\\input.txt', 'r') as f:
        hands = f.readlines()
        for i in range(len(hands)):
            hands[i] = hands[i].strip().split()
            value_counts = {}
            for card in hands[i][0]:
                value = card_importance[card]
                value_counts[value] = value_counts.get(value, 0) + 1

            counts = list(value_counts.values())
            counts.sort(reverse=True)

            if counts == [5]:
                hands[i].append(5.0)  # Five of a kind
            elif counts == [4, 1]:
                hands[i].append(3.0)  # Four of a kind
            elif counts == [3, 2]:
                hands[i].append(2.0)  # Full house (3 of a kind + one pair)
            elif counts == [3, 1, 1]:
                hands[i].append(1.5)  # Three of a kind
            elif counts == [2, 2, 1]:
                hands[i].append(1.0)  # Two pairs
            elif counts == [2, 1, 1, 1]:
                hands[i].append(0.5)  # One pair
            else:
                hands[i].append(0.0)  # No pairs

        # Sort hands by the third index (score), then by the hand based on card importance
        hands = sorted(hands, key=lambda x: (x[2], hand_key(x[0])))

        total_score = sum(int(hand[1]) * (i + 1) for i, hand in enumerate(hands))

        print(f"Total score: {total_score}")

if __name__ == '__main__':
    main()
