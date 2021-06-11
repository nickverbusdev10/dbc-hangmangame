"""
Be sure to set a wins and a losses txt file, import a dictionary in json, and have the pyfiglet library installed for the ascii art
"""
import json
import random
import pyfiglet as p




def Fill_Position_Bool (A_list,Bool_list):

    length=len(A_list)

    Bool_list= [None] * length

    for i in range(length):

        Bool_list[i] = False

    return Bool_list



def Rand_Word_Into_List (A_Word):

    return [char for char in A_Word]



def Letter_Check(A_list, Bool_list,input):

    length = len(A_list)

    for i in range(length):

        if input == A_list[i]:

            Bool_list[i] = True

    return Bool_list

    
    
#this needs work

def Word_Check(A_Word, Guess):

    Return_Value=False

    if A_Word == Guess:

      Return_Value = True

    return Return_Value
    

       




def Guess_Display (A_list, Bool_list, Show_List):

    length = len(A_list)

    for i in range(length):

        if Bool_list[i] == True:

            Show_List[i] = A_list[i]

        else:

            Show_List[i] = "_"

    return Show_List



def True_Counter_For_Letters(Bool_List):

    length = len(Bool_List)

    Number_Of_Trues=0

    for i in range(length):

        if Bool_List[i] == True:

            Number_Of_Trues += 1

    return Number_Of_Trues


def Game_Restart():

    Value_To_Return = False

    answer = False

    x = ""

    while answer == False:

        x = input("Would you like to play again? Y or N?\n")

        if x == "y" or x == "Y" or x == "n" or x == "N":

            answer = True
        
        else:
            
            print("Please give a valid response.\n")

            x = ""

    
    if x == "Y" or x == "y":

        Value_To_Return = True
    
    else:

        Value_To_Return = False

    return Value_To_Return 

def Remaining_Alphabet(A_list, Bool_list, Show_List):

    length = len(A_list)

    for i in range(length):

        if Bool_list[i] == True:

            Show_List[i] = "_"

        else:

            Show_List[i] = A_list[i]

    return Show_List


#This will load in your prefered dictionary into the file

def Word_Import(Path):


    f = open(f"{Path}","r")

    Word_Dictionary = json.load(f)

    f.close()

    return Word_Dictionary

def Record(Result):

    Wins_Losses = [-1,-1]

    f1 = open(r"insert path to wins.txt here")
    f2 = open(r"insert path to losses.txt here")

    wins = f1.read()

    losses = f2.read()

    Wins_Losses[0] = int(wins)

    Wins_Losses[1] = int(losses)

    f1.close()
    f2.close()

    #if win

    if Result == False:

        Wins_Losses[0]+=1

        print(f"You are victorious. Your record is now {Wins_Losses[0]} wins and {Wins_Losses[1]} losses\n\n")

        f1_2 = open(r"insert path to wins.txt here", "w")

        f1_2.write(f"{Wins_Losses[0]}")

        f1_2.close()
    
    #if loss

    else:

        Wins_Losses[1]+=1

        print(f"You have failed. Your record is now {Wins_Losses[0]} wins and {Wins_Losses[1]} losses\n\n")

        f2_2 = open(r"insert path to losses.txt here", "w")

        f2_2.write(f"{Wins_Losses[1]}")

        f2_2.close()





The_Dictionary = {}

Alphabet_As_Set = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#read only

The_Dictionary = Word_Import(r"insert path to dictionary here")

game=True

"""

TO DO:

Import Dictionary (x)

Random Word (x)

Record wins/losses (x)

ASCII? (x)

"""

while game ==True:



    ##Game reset stage: resets variables for new game



    Word_As_List_Position_Check = []

    Display_List = []

    Alphabet_Position_Check = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    Play_Time = False

    Fail_Count = 0

    Rand_Word_True_Counter = 0

    Rand_Word = random.choice(list(The_Dictionary.keys()))

    The_Dictionary.pop(Rand_Word)

    Word_As_List = Rand_Word_Into_List(Rand_Word)

    Word_As_List_Position_Check = Fill_Position_Bool(Word_As_List,Word_As_List_Position_Check)

    Display_List = Fill_Position_Bool(Word_As_List, Display_List)
    # I just need to get this to the right size with something

    ASCII_URDEAD = [p.figlet_format("U",font="Doh"),p.figlet_format("R",font="Doh"),p.figlet_format("D",font="Doh"),p.figlet_format("E",font="Doh"),p.figlet_format("A",font="Doh"),p.figlet_format("D",font="Doh")]

    Loss = False

    Char_Subset={""}

    The_Guess_Memory = ""

    print("Welcome to the word guessing game!\nThis program will select a random word and you will have to guess it.\n\nYou have six wrong attempts to select every letter or the whole word.\n")

    while Play_Time == False:

        Rand_Word_True_Counter = True_Counter_For_Letters(Word_As_List_Position_Check)
        # we need to keep count of the amount of letters correctly guessed to compare with functions later in the program

        The_Guess = input("Select a letter or word\n")

        print("")

        The_Guess_Length = len(The_Guess)

        The_Guess = The_Guess.lower()

        ## checking phase



        # word checking

        if The_Guess_Length > 1:
            
            #The Play_Time True value will go to the win check section

            Play_Time = Word_Check(Rand_Word, The_Guess)

            if Play_Time == False:

                Fail_Count+=1

                print("You guessed the wrong word. Try again.\n")
        
        #letter checking, and I suppose if the player is stupid enough, "" checking as well

        else:
            
            #in the alphabet check

            Char_Subset.discard(The_Guess_Memory)

            Char_Subset.add(The_Guess)

            The_Guess_Memory = The_Guess

            if Char_Subset.issubset(Alphabet_As_Set) == False:

                print("Choose an English letter\n")

                continue


            #This is used to check if the letter has been guessed

            Letter_Place_Check=-1

            for i in range(26):

                if The_Guess == Alphabet[i]:

                    Letter_Place_Check = i

                    break
            
            if Alphabet_Position_Check[Letter_Place_Check] == True:

                print("This letter has already been guessed, please try again.\n")

                continue

            # update Alphabet, checking if the letter is in the word

            else:

                Alphabet_Position_Check[Letter_Place_Check] = True
                
                Temp_True_Counter = 0

                # checking the guess and updating our verification list

                Word_As_List_Position_Check = Letter_Check(Word_As_List,Word_As_List_Position_Check,The_Guess)

                # now to compare the truth values from before and after, if they differ then no lives will be deducted

                Temp_True_Counter = True_Counter_For_Letters(Word_As_List_Position_Check)

                if Temp_True_Counter == Rand_Word_True_Counter:

                    Fail_Count+=1

                    for i in range(Fail_Count):
                            
                        print(ASCII_URDEAD[i])
    
                        print("\n")

                    print(f"Unfortunately, this guess is incorrect.\n")

                else:

                    # I know this is being calculated twice in a loop but it'll do for now until polishing

                    Rand_Word_True_Counter = Temp_True_Counter

                    print(f'Congratulations, the letter {The_Guess} is in the word\n')



        ## win/lose check phase



        if Rand_Word_True_Counter == len(Word_As_List):
            
            Play_Time=True


        if Play_Time == True:

            continue

        if Fail_Count == 6:
            
            Loss=True

            Play_Time=True

            continue



        ## display phase



        Display_List= Guess_Display(Word_As_List, Word_As_List_Position_Check, Display_List)

        print(f"You have {6-Fail_Count} lives remaining.\n\nThis is how your word looks now.\n")

        print(' , '.join([f'{char}' for char in Display_List]))

        print("\nThese are the letters available to guess\n")

        Temp_List = [None] * 26

        Temp_List = Remaining_Alphabet(Alphabet,Alphabet_Position_Check,Temp_List)

        print(' , '.join(Temp_List))

        print("\n")



    ## end phase



    Record(Loss)

    if Loss == True:

        print("YOU LOSE\n")

        print(f"\"{Rand_Word}\" was the word that you failed to guess\n")

        game = Game_Restart()
        

    else:

        print(f"Congratulations, you correctly guessed the word \"{Rand_Word}\" correctly.\n")

        game = Game_Restart()
