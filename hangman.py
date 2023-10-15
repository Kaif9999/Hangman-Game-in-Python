import random as r
from hangmanword import word_list
from hangmanpic import stages
from hangmanpic import logo


chosen_word = r.choice(word_list)
lives = 6

print(logo)                                                           
display = []

for letter in chosen_word:
   display += "-"
print(display)
  
end_of_game =False

while not end_of_game:
   guess = input("Enter a guess letter:").lower()
   
   if guess in display:
      print(f"You already guessed{guess}")
   
   for p in range(len(chosen_word)):
      letter = chosen_word[p]
      if letter == guess:
         display[p] = letter
   if guess not in chosen_word:
           print(f"You guessed {guess}, that's not in the word. You lose a life.")
           
           lives-=1
           if lives == 0:
              end_of_game = True
              print("You Lose")
              
   print(f"{' '.join(display)}")
              
   if "-" not in display:
      end_of_game = True
      print("You Win")
    
   print(stages[lives])   