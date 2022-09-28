from tkinter import *
import csv
import random


def get_quote():


    with open("thomas_sowell_quotes_short.csv", "r",encoding="utf8") as t_s_quotes:
        csv_reader = csv.reader(t_s_quotes)
        # This skips over the first line in the .csv (author, text)
        next(csv_reader)
        # print(random.choice([f"{line[0]} (Thomas Sowell)" for line in csv_reader]))

        quote = random.choice([f"{line[0]} (Thomas Sowell)" for line in csv_reader])

    canvas.itemconfig(quote_text,text=quote)
    

window = Tk()
window.title("Thomas Sowell Says...")
window.config(padx=10, pady=10)

canvas = Canvas(width=800, height=414)
background_img = PhotoImage(file="background1.png")
canvas.create_image(400, 207, image=background_img)
quote_text = canvas.create_text(400, 207, text="Thomas Sowell Quote Goes HERE", width=700, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

tsowell_img = PhotoImage(file="thomas_sowell_min.png")
quote_button = Button(image=tsowell_img, highlightthickness=0, command=get_quote)

quote_button.grid(row=1, column=0)



window.mainloop()