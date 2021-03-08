import random

# Output a welcome message.
print()
print("#############")
print("#           #")
print("# Welcome   #")
print("#           #")
print("#############")

run_feelings = True


while run_feelings: 
            
 print("You can choose from the following list of feelings. Which one best matches your mood right now?")
 print()
 #feelings
 print("A: Im sad")
 print("B: Im anxious")
 print("C: Im mad")
 print("D: Im happy")
 print("Q: To Quit.")
 print()

 #instructions
 print("Enter the letter that corresponds the most closely to how you feel.")
 
 # Creates a variable called feeling that stores the users input.

 feeling = input("Choose a feeling from the options (A,B,C,D,Q): ")
 
 # Process the user input.
 if feeling == "A":
    print()
    print("Sadness flies away on the wings of time.")
    print()
    print("Jean de La Fontaine")
    print()
 if feeling == "B":
    print()
    print("Anxiety was born in the very same moment as mankind. And since we will never be able to master it, we will have to learn to live with it—just as we have learned to live with storms.")
    print()
    print("Paulo Coelho")
    print()
 if feeling == "C":
    print()
    print("For every minute you remain angry, you give up sixty seconds of peace of mind.")
    print()
    print("Ralph Waldo Emerson")
    print()
 if feeling == "D":
    print()
    print("No medicine cures what happiness cannot.")
    print()
    print("Gabriel García Márquez")
    print()

 elif feeling == "Q":
        print("Cya.")

        # Stop the loop
        run_feelings = False
else:
        print("I don't understand.")

