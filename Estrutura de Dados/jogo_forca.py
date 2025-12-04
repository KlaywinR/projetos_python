name =  input("Whats your name?")

print("\n-------------------------------------------")
print(f"\Olá {name}!,welcome to the game of hangman.")
print("\n-------------------------------------------")

secret_word = 'Paula'
#lista com placeholders - underscores 
corrected_letters = ['_', '_', '_', '_', '_']

erros  = 0
acertou = "_" not in corrected_letters
enforcou = erros == 6


while(not acertou and not enforcou):
    kick = input("Guess the letter you think it is?  ")
    hit = False
    position = 0 
    for letter in secret_word:
        if (kick.upper() == letter.upper()):
            corrected_letters[position] = letter
            hit = True
        position += 1
        
    if not hit:
        erros += 1
        print(f"Ops, letter not found!\n Erros: {erros}/6")
        
    print("".join(corrected_letters))
    
    acertou = "_" not in corrected_letters
    enforcou = erros == 6
    
if acertou:
    print("-----------------------------------------------------------------------")
    print(f"Congratulations, {name}! you guessed the word for the game correctly..")
    print(f"The word was: {secret_word}")
    print("-----------------------------------------------------------------------")
    
else:
    print(f"Oh, {name}, yoou lost the game!...\n The word was: {secret_word}")
    

    
        
     
   
    
        
        
    
        

