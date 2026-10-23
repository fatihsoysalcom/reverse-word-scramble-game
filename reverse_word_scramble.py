import random

def scramble_word(word):
    """Scrambles the letters of a word, ensuring it's not the original word."""
    if len(word) < 2:
        return word
    
    scrambled = list(word)
    original_word = word
    
    # Keep shuffling until it's different from the original word
    while ''.join(scrambled) == original_word:
        random.shuffle(scrambled)
    
    return ''.join(scrambled)

def play_reverse_scramble_game(word_list):
    """Plays a simple reverse word scramble game."""
    print("Welcome to the Reverse Word Scramble Game!")
    print("I will give you a scrambled word, and you try to guess the original.")
    print("Let's begin!")

    score = 0
    
    # Shuffle the word list to present words in a random order
    random.shuffle(word_list)

    for word in word_list:
        scrambled = scramble_word(word)
        
        print(f"\nYour scrambled word is: {scrambled}")
        guess = input("What is the original word? ").strip().lower()
        
        if guess == word.lower():
            print("Correct! You got it!")
            score += 1
        else:
            print(f"Incorrect. The word was: {word}")

    print(f"\nGame Over! Your final score is: {score}/{len(word_list)}")

if __name__ == "__main__":
    # A sample list of words to use in the game
    # In a real game, this could be loaded from a file or a larger dictionary
    sample_words = ["python", "developer", "algorithm", "programming", "challenge", "cognitive", "reverse", "learning"]
    play_reverse_scramble_game(sample_words)
