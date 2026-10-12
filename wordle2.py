import random 

# player information goes here (poom)


word_length = 5  
max_attempts = 6 
answer_words = [  
	"atlas",
	"crown",
	"egypt",
	"hades",
	"hydra",
	"mummy",
	"oasis",
	"ruins",
	"sages",
	"stone",
	"sword",
	"titan",
	"torch",
	"tower",
]



def score_guess(secret_word, guess):
	feedback = ["_"] * word_length 
	remaining_letters = []  

	for index in range(word_length):  
		letter = secret_word[index]  
		if guess[index] == letter:
			feedback[index] = "G" 
		else:
			remaining_letters.append(letter)  


	for index in range(word_length):  
		letter = guess[index]  
		if feedback[index] != "G" and letter in remaining_letters:
			feedback[index] = "Y" 
			remaining_letters.remove(letter) 

	return feedback  



def play_game():
	secret_word = random.choice(answer_words) 

	print("=" * 34)
	print("       ANCIENT WORDLE GATE")
	print("=" * 34)
	print("Welcome, traveler, to THE ANCIENT !") 
	print("=" * 34) 
	print("")
	print("Your mission is to Guess a 5-letter English word in 6 attempts.") 
	print("Correct letter in the correct position: G")
	print("Correct letter in the wrong position: Y")
	print("Letter not in the word: _")
	print("")
	print("Good luck in this stage!")
	

#game loop for the player to guess the word


if __name__ == "__main__":
	play_game() 
