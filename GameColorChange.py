import tkinter as tkin
import random
import time
# List of colors

colorList = ["Red","Blue","Green","Pink","Orange","Black","White","Yellow","Gray","Purple"]

score = 0
highScore = 0

MAXTIME = 30

countDown = MAXTIME

startIn = 4

def main(event):
    startInCountdown()
    


def startInCountdown():
    global startIn

    if(startIn>0):
        startIn -=1
        colorLabel.config(text = str(startIn))
        colorLabel.after(1000,startInCountdown)
    else:
        if countDown == MAXTIME:
            startCount()
        pickColor()
    
    
def reset():
    global score, highScore
    global countDown
    global startIn

    if(score > highScore):
        highScore = score

    startIn = 4
    score = 0
    countDown = MAXTIME
    timeLabel.config( text = "Press enter to start game",font = ('Helvetica', 25) )
    colorLabel.config( text = " ", fg = 'Black',font=('Helvetica', 70))
    scoreLabel.config( text = "High Score: "+str(highScore))

timeCounter = None
def startCount():
    global countDown
    countDown -=1
    timeLabel.config( text = "Time left: " + str(countDown),font = ('Helvetica', 12) )
    timeCounter = timeLabel.after(1000,startCount)
    if(countDown == 0):
        colorLabel.config(text="GAME OVER", fg = 'Black', font=('Helvetica',50))
    elif(countDown == -1):

        timeLabel.after_cancel(timeCounter)
        timeCounter = None
        root.after(1000,reset())

        


def pickColor():
    global score
    global countDown

    if countDown > 0:
        input.focus_set()

        if(input.get().lower()==colorList[1].lower()):
            score += 5
        input.delete(0,tkin.END)
        random.shuffle(colorList)

        colorLabel.config(text = str(colorList[0]),fg=str(colorList[1]))

        scoreLabel.config(text = "Score: " + str(score), font=('Helvetica',12))



root = tkin.Tk()
root.configure(background='#e3cfb3')

root.title("ColorTyper")

root.geometry("400x300")

howTo = tkin.Label(root, text = "Type the color of the text, not the text!!", font = ('Helvetica', 12),background='#e3cfb3', fg = '#382914')
howTo.pack()

scoreLabel = tkin.Label(root,font = ('Helvatica', 12),background='#e3cfb3',fg = '#382914')
scoreLabel.pack()

timeLabel = tkin.Label(root,text = "Press Space to start game",font = ('Helvetica', 25),background='#e3cfb3',fg = '#382914' )
timeLabel.pack()

colorLabel = tkin.Label(root,font = ('Helvetica', 70),background='#e3cfb3',fg = '#382914')
colorLabel.pack()

input = tkin.Entry(root)
input.bind('<space>',main)
input.bind('<Return>',main)
input.focus_set()
input.pack()

root.mainloop()