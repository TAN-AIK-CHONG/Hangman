import tkinter as tk
import random
import os

def choose_word():
    with open("assets\HangmanList.txt", "r") as HangmanList:
        wordsAll = HangmanList.readlines()
        return random.choice(wordsAll).strip()
    
def updateHangman(): ##if button pressed, update button and hangman
    return

def checkFinal(): ##if submit pressed, check final.
    return

def hangman():
    answer = choose_word()
    for i in range (len(answer)):
       guessed_answer = f"{i * '_ ' }"
    
    ##create tk interface
    root = tk.Tk()
    root.title("HANGMAN!")
    root.geometry("1000x900")
    
    ##create frames 
    frm_hangman_img = tk.Frame(master=root)
    frm_guess = tk.Frame(master=root)
    frm_buttons_top = tk.Frame(master=root)
    frm_buttons_bot = tk.Frame(master=root)
    frm_final_guess = tk.Frame(master=root)
    
    ##create hangman image and user's guess. NOT packing yet.
    hangman_img = tk.PhotoImage(file="assets\strike0.png")
    hangman_lbl = tk.Label(master=frm_hangman_img, image=hangman_img)
    hangman_lbl.pack()
    guess_lbl = tk.Label(master=frm_guess, text=guessed_answer, font=("Arial", 90))
    guess_lbl.pack()
    
    # Create dictionary to store button PhotoImages
    button_imgs = {}
    file_paths_btn = [
        r"assets\A.png", r"assets\B.png", r"assets\C.png", r"assets\D.png",
        r"assets\E.png", r"assets\F.png", r"assets\G.png", r"assets\H.png",
        r"assets\I.png", r"assets\J.png", r"assets\K.png", r"assets\L.png",
        r"assets\M.png", r"assets\N.png", r"assets\O.png", r"assets\P.png",
        r"assets\Q.png", r"assets\R.png", r"assets\S.png", r"assets\T.png",
        r"assets\U.png", r"assets\V.png", r"assets\W.png", r"assets\X.png",
        r"assets\Y.png", r"assets\Z.png"]

    for item in file_paths_btn:
        key = os.path.basename(item).split(".")[0]
        button_imgs[key] = tk.PhotoImage(file=item)
   
    # Create the buttons
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
             "Q","R","S","T","U","V","W","X","Y","Z"]
    

    for alphabet in alphabets:
        if (alphabet<="M"):
            button = tk.Button(frm_buttons_top, image=button_imgs[alphabet])
            button.pack(side=tk.LEFT)
        else:
            button = tk.Button(frm_buttons_bot, image=button_imgs[alphabet])
            button.pack(side=tk.LEFT)
    
    
    ##create guess full word frame
    explanation_text_lbl = tk.Label(master=frm_final_guess, text="Guess the word:", font=("Arial", 15))
    explanation_text_lbl.pack(side=tk.LEFT)
    user_entry = tk.Entry(master=frm_final_guess, width=50, font=("Arial",15))
    user_entry.pack(side=tk.LEFT)
    submit_img = tk.PhotoImage(file="assets\submit_button.png")
    submit_btn = tk.Button(master=frm_final_guess, image=submit_img)
    submit_btn.pack(side=tk.LEFT)
    
    ##pack all frames
    frm_hangman_img.pack()
    frm_guess.pack(pady=50)
    frm_buttons_top.pack()
    frm_buttons_bot.pack()
    frm_final_guess.pack()
    
    root.mainloop()
    
hangman()

    
    
    
    