import random
from collections import Counter

# Card Ranks and Suits
RANKS = "23456789TJQKA"
SUITS = "CDHS"

# Hand Rankings (High to Low)
HAND_RANKS = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

# Generate a Deck of Cards
def generate_deck():
    return [rank + suit for rank in RANKS for suit in SUITS]

# Deal Cards
def deal_hand(deck, num=5):
    return random.sample(deck, num)

# Evaluate Hand Strength
def evaluate_hand(hand):
    ranks = sorted([RANKS.index(card[0]) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    
    rank_counts = Counter(ranks)
    most_common = rank_counts.most_common()
    is_flush = len(set(suits)) == 1
    is_straight = len(rank_counts) == 5 and (ranks[0] - ranks[-1] == 4)
    
    if is_flush and is_straight and ranks[0] == RANKS.index('A'):
        return "Royal Flush", HAND_RANKS["Royal Flush"]
    if is_flush and is_straight:
        return "Straight Flush", HAND_RANKS["Straight Flush"]
    if most_common[0][1] == 4:
        return "Four of a Kind", HAND_RANKS["Four of a Kind"]
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        return "Full House", HAND_RANKS["Full House"]
    if is_flush:
        return "Flush", HAND_RANKS["Flush"]
    if is_straight:
        return "Straight", HAND_RANKS["Straight"]
    if most_common[0][1] == 3:
        return "Three of a Kind", HAND_RANKS["Three of a Kind"]
    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return "Two Pair", HAND_RANKS["Two Pair"]
    if most_common[0][1] == 2:
        return "One Pair", HAND_RANKS["One Pair"]
    return "High Card", HAND_RANKS["High Card"]

# Poker Bot Decision-Making
def poker_bot_decision(hand_strength):
    if hand_strength >= 7:
        return "Raise"
    elif hand_strength >= 5:
        return "Call"
    else:
        return "Fold"

# Simulate Poker Round
def simulate_poker_game():
    deck = generate_deck()
    player_hand = deal_hand(deck)
    opponent_hand = deal_hand(deck)
    
    player_hand_rank, player_hand_strength = evaluate_hand(player_hand)
    opponent_hand_rank, opponent_hand_strength = evaluate_hand(opponent_hand)
    
    bot_action = poker_bot_decision(player_hand_strength)
    
    print(f"Player Hand: {player_hand} ({player_hand_rank})")
    print(f"Opponent Hand: {opponent_hand} ({opponent_hand_rank})")
    print(f"Poker Bot Decision: {bot_action}")

# Run Simulation
simulate_poker_game()
