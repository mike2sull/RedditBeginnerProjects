'''
Magic 8 ball: https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/
Beginner Reddit Python Projects: https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/edit

Goal:
I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
    Allow the user to enter their question
    Display an in progress message( i.e. "thinking")
    Create 20 responses, and show a random response
    Allow the user to ask another question or quit

Bonus Using whatever module you like, add a gui. Your gui must have:
    A box for users to enter the question
    At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
'''

import random
import time
import tkinter as tk

responses = [
    'Yes',
    'No',
    'Ask again',
    'Absolutely not',
    'Don\'t count on it',
    'Maybe',
    'I\'m tired. come back later',
    'Sources say: No',
    'Sources say: Yes!',
    'Zzzzzzzzz....',
    'Never',
    'Maybe if the stars are properly aligned',
    'Stop shaking me',
    'Seriously, how would you feel if someone just walked up and started shaking you?',
    'I\'m calling the police. Go away',
    'Possibly',
    'IDK, My BFF Jill?',
    'Ask again later',
]

# Code for the 8 ball
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inputQuestion = tk.Entry(self)
        self.inputQuestion.grid(row=0)
        self.shakeButton = tk.Button(self, text='Shake', command=askQuestion(self.inputQuestion.get()))
        self.shakeButton.grid(row=1)


def shake():
    r = random.randrange(0, len(responses))
    print('Shaking....')
    time.sleep(5)
    print(responses[r])
    askQuestion(q)

def askQuestion(q):
    try:
        # non-GUI: question = input('What is the knowledge that you seek?  If none, type "q" to quit.')
        question = q
        if question == 'q':
            quit()
        else:
            shake()
    except():
        quit()


 # Code for the GUI




app = Application()
app.master.title('Magic 8 Ball')
app.mainloop()


# askQuestion()
