
#from API import *




art = {0 : ("  ",
            "  ",
            "  "),
        1: (" o",
            "  ",
            "  "),
           
        2 : (" o",
            " |",
            "  "),

        3: (" o",
            "/|",
            "  "),
           
        4: (" o",
            "/|\\",
            "  "),
           
        5: (" o",
            "/|\\",
             "/"),
        6 : (" o",
            "/|\\",
            "/ \\"),}

# for value in art.values():
#     for line in value:
#         print(line)

def display_man(wrong_gusses,line):
    #print(f"CATAGORY: {catagory}")
    return art[wrong_gusses][line]

    
def display_hints(hint):
    return (" ".join(hint))

def display_answer(answer):
     return (" ".join(answer))

def main():
    
    catagory = Fetch_category()
    answer = Fetch_Word(word)

    while catagory == "Could not fetch word" or word == "Could not fetch word" :
        catagory = Fetch_category()
        answer = Fetch_Word(word).strip()
        print("Could not fetch word")
        continue
    else:
        hint = ["_"]* len(answer)
        wrong_guesses= 0
        guesses = set()
        is_running = True 


    while is_running:
        display_man(wrong_guesses,catagory)
        print("*"*40)
        print(f"you have {6-wrong_gusses} guesses left")
        display_hints(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha:
            print("invalid input")
            continue

        if guess  in guesses:
            print(f'{guess} already guessed')
            continue
            
        guesses.add(guess)

        if guess in answer:
          for i in range(len(answer)) :
              if answer[i]==guess:
                  hint[i] = guess

        else:
            wrong_guesses +=1


        if "_" not in hint:
            display_man(wrong_guesses,catagory)
            display_answer(answer)
            print("you win")
            break
        elif wrong_guesses >= len(art)-1:
            display_man(wrong_guesses,catagory)
            display_answer(answer)
            print("you lose")
            break

        
       


if __name__=="__main__":
  main()