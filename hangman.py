## MY FIRST PERSONAL PROJECT
## HANGMAN
import random
 
def printGuess(guessArr,word_list,guess): #takes in word list and prints the guess array. updates guess array.
    for i in range(len(word_list)):
            if word_list[i]==guess:
                guessArr[i] = guess
    for i in range(len(guessArr)):
        print(guessArr[i], end="")
    

def userGuessChar(word_list):
    guess = input("What alphabet would you like to guess? ")
    while (guess.isalpha()!=1 and len(guess)!=1):
        print("Please input a single alphabet")
        guess = input("What alphabet would you like to guess? ")
        
    if (guess in word_list):
        printGuess(guessArr,word_list,guess)
        print()
        return 1
    else:
        print(f"There is no '{guess.upper()}' in the word")
        return 0

def userGuessWord(word):
    guess = input("Make your guess: ")
    if ((guess.upper())==(word.upper())):
        return 1
    return 0

#main function:
hangman_words = [
    "apple", "banana", "carrot", "dog", "cat", "bird", "house", "tree", "sun", "moon",
    "star", "fish", "ball", "book", "chair", "table", "clock", "pen", "pencil", "door",
    "window", "flower", "grass", "cloud", "rain", "snow", "river", "lake", "mountain", "road",
    "bridge", "phone", "computer", "desk", "lamp", "shirt", "pants", "shoes", "hat", "glove",
    "sock", "jacket", "guitar", "piano", "drum", "bike", "car", "bus", "train", "plane",
    "ship", "rocket", "robot", "doll", "bear", "toy", "baby", "child", "man", "woman",
    "boy", "girl", "teacher", "student", "doctor", "nurse", "chef", "artist", "singer", "actor",
    "dancer", "writer", "poet", "scientist", "engineer", "athlete", "captain", "king", "queen", "prince",
    "princess", "castle", "palace", "home", "village", "city", "country", "planet", "universe", "earth",
    "galaxy", "astronaut", "alien", "monster", "ghost", "fire", "water", "air", "earthquake", "volcano",
    "tornado", "hurricane", "storm", "lightning", "thunder", "rainbow", "clouds", "fog", "smoke", "mirror",
    "glass", "rock", "stone", "sand", "dirt", "wood", "metal", "gold", "silver", "copper", "iron",
    "plastic", "rubber", "paper", "cardboard", "cloth", "fabric", "thread", "needle", "button", "zipper",
    "velcro", "snap", "lace", "ribbon", "lace", "string", "yarn", "chain", "wire", "cord", "rope",
    "twine", "strap", "band", "belt", "bracelet", "necklace", "ring", "earring", "watch", "glasses",
    "sunglasses", "hat", "scarf", "glove", "mitten", "mitt", "boot", "shoe", "sandal", "slipper",
    "sneaker", "heel", "wedge", "platform", "sole", "heel", "arch", "toe", "ankle", "calf",
    "knee", "thigh", "hip", "waist", "belly", "abdomen", "chest", "breast", "back", "shoulder",
    "arm", "elbow", "wrist", "hand", "finger", "thumb", "palm", "nail", "finger", "knuckle",
    "bone", "spine", "rib", "hip", "leg", "thigh", "knee", "calf", "ankle", "heel",
    "toe", "foot", "sole", "toenail", "eyebrow", "eyelash", "eyelid", "eye", "iris", "pupil",
    "cornea", "sclera", "lens", "retina", "optic", "nerve", "ear", "earlobe", "ear", "canal",
    "eardrum", "malleus", "incus", "stapes", "tongue", "taste", "bud", "mouth", "lip", "teeth",
    "gum", "jaw", "chin", "cheek", "throat", "neck", "voice", "box", "larynx", "adam's",
    "apple", "windpipe", "trachea", "bronchus", "bronchiole", "alveoli", "lung", "diaphragm", "heart", "artery",
    "vein", "capillary", "blood", "aorta", "ventricle", "atrium", "valve", "pulse", "blood", "pressure",
    "circulation", "plasma", "platelet", "red", "blood", "cell", "white", "blood", "cell", "immune",
    "system", "lymph", "node", "tonsil", "spleen", "thymus", "bone", "marrow", "joint", "cartilage",
    "tendon", "ligament", "muscle", "nervous", "system", "brain", "spinal", "cord", "nervous", "tissue",
    "neuron", "nerve", "cell", "dendrite", "axon", "synapse", "cerebrum", "cerebellum", "brainstem", "thalamus",
    "hypothalamus", "cerebral", "cortex", "cerebral", "hemisphere", "lobes", "frontal", "lobe", "parietal", "lobe"]

word = random.choice(hangman_words)
word_list = list(word)
num_strike = 0
guessArr = []
for i in range(len(word_list)):
    guessArr.append("_")

print("You lose if you make a wrong guess 9 times")
print(f"It is a {len(word_list)} letter word")
print("------------------------------------------")
print("Let's get started:")
print("Option 1: Guess an alphabet")
print("Option 2: Guess the word")
print("Option 3: End")

while (num_strike<9):
    userChoice = int(input("Choose 1/2/3: "))
    if (userChoice==1):
        result = userGuessChar(word_list)
        if (result==1):
            if ("_" not in guessArr):
                print("Congrats, you win!")
                break
            continue
        else:
            num_strike += 1
            print("Wrong guess.")
            print(f"Strike {num_strike}")
            continue
    if (userChoice==2):
        result = userGuessWord(word)
        if (result==1):
            print("Congrats, you win!")
            break
        else:
            num_strike += 1
            print("Wrong guess.")
            print(f"Strike {num_strike}")
            continue
    if (userChoice==3):
        break
    else:
        print("Not a valid input!\n")
        userChoice = int(input("Choose 1/2/3"))
        
        
if (num_strike==9):
    print("You lose. Better luck next time.")


