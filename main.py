from tkinter import *
import tkinter.messagebox

# Constants
FONT_NAME = "Arial"
current_text = []
after_text = []
# UI
window = Tk()
window.title('Disappearing Text Game')
window.geometry("705x500")
window.config(padx=70, pady=30)


# Instruction Button
def instructions():
    tkinter.messagebox.showinfo(title='Instructions', message="When you click start, you can begin typing a prompt but "
                                                              "if you stop typing for 5 seconds, your message will be "
                                                              "lost forever. Take a chance!")


# Start Button

def initial_check():
    global current_text
    current_text = word_check()
    window.after(5000, after_check)


def word_check():
    text = prompt_text.get('1.0', END).replace(".", "").split(" ")
    return text


def after_check():
    global current_text
    global after_text
    after_text = word_check()

    if len(current_text) == len(after_text):
        prompt_text.delete(1.0, END)
        tkinter.messagebox.showinfo(title='Instructions', message=f"Sorry you've stopped more than 5 seconds! You typed"
                                                                  f" {len(after_text)-1} words.")
    else:
        initial_check()


# prompt display
prompt_text = Text(width=80, height=20, font=(FONT_NAME, 10, "bold"), wrap=WORD)
prompt_text.grid(column=0, row=0)

# start button
start = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=initial_check)
start.grid(column=0, row=1, pady=10)

# instructions
instructions = Button(text='Instructions', font=(FONT_NAME, 12, "bold"), command=instructions)
instructions.grid(column=0, row=2, pady=10)

window.mainloop()
