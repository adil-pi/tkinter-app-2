# from tkinter import *
# import os
# import webbrowser


# def open_youtube():
#     webbrowser.open("https://www.youtube.com/")

# def open_paint():
#     os.system("mspaint")

# def open_ts():
#     webbrowser.open("https://www.ts.kg")

# root = Tk()
# root.title("dynomike song tutorial")
# root.geometry("500x400")

# btn = Button(text="открыть youtube", command=open_youtube)
# btn2 = Button(text="открыть paint", command=open_paint)
# btn3 = Button(text="открыть кино", command=open_ts)

 
# btn.pack(padx=10, pady=10)
# btn2.pack(padx=10, pady=10)
# btn3.pack(padx=10, pady=10)

# root.mainloop()



import random

def game():
    number_to_guess = random.randint(1, 100)
    guess = None
    tries = 1

    while guess != number_to_guess:
        guess = int(input("Угадай число от 1 до 100: "))
        tries += 1
        if guess < number_to_guess:
            print("Слишком мало! Попробуй снова.")
        elif guess > number_to_guess:
            print("Слишком много! Попробуй снова.")

    print(f"Поздравляю! Ты угадал число {number_to_guess} за {tries} попыток.")

if __name__ == "__main__":
    game()














