# Imports
import tkinter as tk
from tkinter import *
import random

# create the GUI
root = Tk()
root.title('Type Speed Test')
root.geometry('1000x700')

# # Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "arial 30")
root.option_add("*Button.Font", "courier 30")


# functions
def keyPress(event=None):
    try:
        if event.char.lower() == label_right.cget('text')[0].lower():
            # Deleting one from the right side.
            label_right.configure(text=label_right.cget('text')[1:])
            # Deleting one from the right side.
            label_left.configure(text=label_left.cget('text') + event.char.lower())
            # set the next Letter Label
            current_letter_label.configure(text=label_right.cget('text')[0])
    except tk.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'Kenya is my favorite country; in fact, I plan to spend two weeks there next year.On a scale from one to ten, what is your favorite flavor of random grammar? Dan took the deep dive down the rabbit hole. It was the first time he had ever seen someone cook dinner on an elephant. Strawberries must be the one food that does not go well with this brand of paint. There are few things better in life than a slice of pie. You will see the rainbow bridge after it rains cats and dogs. Cats are good pets, for they are clean and are not noisy. He had reached the point where he was paranoid about being paranoid. I do not respect anybody who can not tell the difference between Pepsi and Coke. He embraced his new life as an eggplant.',
        'He found the chocolate covered roaches quite tasty. She thought there would be sufficient time if she hid her watch.Too many prisons have become early coffins. There is a reason that roses have thorns. The doll spun around in circles in hopes of coming alive. Two more days and all his problems would be solved. David proudly graduated from high school top of his class at age 97. He found a leprechaun in his walnut shell. Excitement replaced fear until the final moment.',
        'The quick brown fox jumped over the lazy dog, the dog then woke up in shock, skittled around and saw the fox running into the distance. The dog then barked three times and lied down. A one eyed cat pounced on the lazy dog, smacked its face the dog then started to whimper. The dog was indeed very lazy and a wuss. The wussiest laziest dog in the whole wide world. This story was not thought of at all, I just typed it in,to have a random paragrah. This is taking longer than i thought. Lazy dogs are not fun.'
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()
    # defining where the text is split
    splitPoint = 0
    # This is where the text is that is already written
    global label_left
    label_left = Label(root, text=text[0:splitPoint], fg='grey')
    label_left.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global label_right
    label_right = Label(root, text=text[splitPoint:])
    label_right.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global current_letter_label
    current_letter_label = Label(root, text=text[splitPoint], fg='grey')
    current_letter_label.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global time_left_label
    time_left_label = Label(root, text=f'0 Seconds', fg='grey')
    time_left_label.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passed_seconds
    passed_seconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(label_left.cget('text').split(' '))

    # Destroy all unwanted widgets.
    time_left_label.destroy()
    current_letter_label.destroy()
    label_right.destroy()
    label_left.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    # Destroy result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()


def addSecond():
    # Add a second to the counter.

    global passed_seconds
    passed_seconds += 1
    time_left_label.configure(text=f'{passed_seconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)


# start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()