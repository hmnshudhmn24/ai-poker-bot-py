# AI Poker Bot

## Description
The AI Poker Bot is a Python-based poker-playing bot that evaluates hand strength and makes intelligent betting decisions. It simulates a poker round with an opponent and decides whether to fold, call, or raise based on hand rankings.

## Features
- Generates a standard deck of cards.
- Deals hands to both the player and the opponent.
- Evaluates hand strength based on poker rules.
- Makes decisions using a predefined strategy.
- Simulates a poker round.

## Requirements
- Python 3.x

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/ai-poker-bot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ai-poker-bot
   ```
3. Run the script:
   ```sh
   python ai_poker_bot.py
   ```

## How It Works
1. A deck of 52 cards is generated.
2. Two hands are randomly dealt (one for the player and one for the opponent).
3. The bot evaluates the hands and assigns a ranking.
4. The bot makes a decision (Raise, Call, or Fold) based on the hand strength.
5. The results are displayed in the console.

## Hand Rankings (High to Low)
1. **Royal Flush**
2. **Straight Flush**
3. **Four of a Kind**
4. **Full House**
5. **Flush**
6. **Straight**
7. **Three of a Kind**
8. **Two Pair**
9. **One Pair**
10. **High Card**

## Future Improvements
- Implement advanced AI strategies (e.g., Monte Carlo simulations, reinforcement learning).
- Support multi-round betting.
- Add a GUI for better visualization.
- Improve opponent AI logic.

## License
This project is open-source and available for modification and distribution.
