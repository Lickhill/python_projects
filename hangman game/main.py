import random
import hangman_art
import hangman_words

print(hangman_art.logo)
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display+="_"
print("".join(display))

count=0

while not chosen_word==''.join(display):
  temp=0
  guess = input("\nGuess a letter: ").lower()
  
  for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
      temp+=1
  if temp==0:
    count+=1
    print(hangman_art.stages[7-count])
  if count==7:
    print("GAME OVER, you lost")
    break

  for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
      display[i]=guess

  for i in display:
    print(i, end=' ')
  print()

if chosen_word==''.join(display):
  print("YOU WON")
  print(f"Chosen word was: {''.join(display)}")  

  
  








  


#Check guessed letter

# for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter


