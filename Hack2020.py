# Simple enough, just import everything from tkinter.
from tkinter import *
from random import random
from timer import *



#download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)


class Window(Frame):

    
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
        self.timer=timer(self,1)
        self.timer.start()



    #Creation of init_window
    def init_window(self):
        self.clicks=0
        
        

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu, tearoff=0)

        # adds a command to the menu option for level selection
        file.add_command(label="All you can Eat", command=lambda: self.eat(lChoice, rChoice, img, text))
        file.add_command(label="Lost at Sea", command=lambda: self.ownPath(lChoice, rChoice, img, text))
        file.add_command(label="Elf Overboard", command=lambda: self.overboard(lChoice, rChoice, img, text))
        file.add_command(label="Sharkboait ooo aha", command=lambda: self.sharkBait(lChoice, rChoice, img, text))
        file.add_command(label="Sticky Business", command=lambda: self.sticky(lChoice, rChoice, img, text))
        file.add_command(label="Bad Day Bidet", command=lambda: self.badDay(lChoice, rChoice, img, text))
        file.add_command(label="Choked Up", command=lambda: self.kareoke(lChoice, rChoice, img, text))
        file.add_command(label="Coldfeet", command= lambda: self.coldfeet(lChoice, rChoice, img, text))
        file.add_command(label="The End", command=lambda: self.theEnd(lChoice, rChoice, img, text))
        file.add_command(label="The Bunny!", command=lambda: self.runAway2(lChoice, rChoice, img, text))
        file.add_command(label="Exit Game", command=self.client_exit)


        #added "Level Select" to our menu
        menu.add_cascade(label="Level Select", menu=file)


        # create the file object)
        edit = Menu(menu, tearoff=0)

        # adds a command to the menu option for games
        edit.add_command(label="Wabbits", command=lambda: self.wabbits(lChoice, rChoice, img, text))

        #added "GAmes" to our menu
        menu.add_cascade(label="Games", menu=edit)


        img=self.showImg("MainTitle.png")
        text = Label(self, text="The Many Adventures of Mr. Gonzales", font=('Sans Serif', 25))
        text.pack()
        text.place(x=45, y=0)
        lChoice = Button(self, text="BEGIN", command=lambda: self.how(lChoice, rChoice, img, text), font=('Sans Serif', 25))
        rChoice = Button(self, text="RUN AWAY", command=self.client_exit, font=('Sans Serif', 25))
        lChoice.place(x=50, y=500)
        rChoice.place(x= 400, y=500)
        
    def start(self,button1,img):
        self.dB3(button1, img)
        img=self.showImg("MainTitle.png")
        text = Label(self, text="The Many Adventures of Mr. Gonzales", font=('Sans Serif', 25))
        text.pack()
        text.place(x=45, y=0)
        lChoice = Button(self, text="BEGIN", command=lambda: self.how(lChoice, rChoice, img, text), font=('Sans Serif', 25))
        rChoice = Button(self, text="RUN AWAY", command=self.client_exit, font=('Sans Serif', 25))
        lChoice.place(x=50, y=500)
        rChoice.place(x= 400, y=500)
        
    def start2(self,button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("MainTitle.png")
        text = Label(self, text="The Many Adventures of Mr. Gonzales", font=('Sans Serif', 25))
        text.pack()
        text.place(x=45, y=0)
        lChoice = Button(self, text="BEGIN", command=lambda: self.how(lChoice, rChoice, img, text), font=('Sans Serif', 25))
        rChoice = Button(self, text="RUN AWAY", command=self.client_exit, font=('Sans Serif', 25))
        lChoice.place(x=50, y=500)
        rChoice.place(x= 400, y=500)
        
    def start3(self,button1, button2, button3, img,text):
        self.dB2(button1, button2, button3, img, text)
        img=self.showImg("MainTitle.png")
        text = Label(self, text="The Many Adventures of Mr. Gonzales", font=('Sans Serif', 25))
        text.pack()
        text.place(x=45, y=0)
        lChoice = Button(self, text="BEGIN", command=lambda: self.how(lChoice, rChoice, img, text), font=('Sans Serif', 25))
        rChoice = Button(self, text="RUN AWAY", command=self.client_exit, font=('Sans Serif', 25))
        lChoice.place(x=50, y=500)
        rChoice.place(x= 400, y=500)

    def how(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Scene1.png")
        text=self.showText("Dad asks you to go on a cruise with him. \n Do you go?")
        lChoice = self.lButton("Go with Dad.", lambda: self.eat(lChoice, rChoice, img, text))
        rChoice = self.rButton("Don't go with Dad", lambda: self.die(lChoice, rChoice, img, text))

        
    def eat(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Hallway Scene.png")
        text=self.showText("When you and Dad get on the cruise, he smells a delicious breakfast buffet. \n Dad decides to go to the buffet. Do you go?")
        lChoice = self.lButton("Follow Dad", lambda: self.die(lChoice, rChoice, img, text))
        rChoice = self.rButton("Go your own path.", lambda: self.ownPath(lChoice, rChoice, img, text))

    def ownPath(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Hallway Scene.png")
        text=self.showText("You decided to go your own path. Do you ...")
        lChoice = self.lButton("Go Left.", lambda: self.left(lChoice, rChoice, img, text))
        rChoice = self.rButton("Go Right.", lambda: self.right(lChoice, rChoice, img, text))
        
        
    def left(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Hallway Scene.png")
        text=self.showText("After going left. Do you ... ")
        lChoice = self.lButton("Go Left.", lambda: self.overboard(lChoice, rChoice, img, text))
        rChoice = self.rButton("Go Right.", lambda: self.die(lChoice, rChoice, img, text))
       
        
    def right(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Hallway Scene.png")
        text=self.showText("After going Right. Do you...")
        lChoice = self.lButton("Go Left.", lambda: self.overboard(lChoice, rChoice, img, text))
        rChoice = self.rButton("Go Right.", lambda: self.die(lChoice, rChoice, img, text))
  


    def overboard(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("ocean.png")
        text=self.showText(" You decide that you need to relax a bit after walking around for a bit. \n Do you want to relax by the pool or look out over the sea?")
        lChoice = self.lButton("Look out over the sea", lambda: self.die(lChoice, rChoice, img, text))
        rChoice = self.rButton("Relax by the pool", lambda: self.sharkBait(lChoice, rChoice, img, text))
        

    def sharkBait(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Pool Scene1.png")
        text=self.showText("Good choice to decide to relax by the pool. \n While relaxing, you see a hammerhead shark. \n Do you decide to…")
        lChoice = self.lButton("Run Away", lambda: self.die(lChoice, rChoice, img, text))
        rChoice = self.rButton("Freeze", lambda: self.sticky(lChoice, rChoice, img, text))
      


    def sticky(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Pool Scene 2.png")
        text=self.showText("The hammerhead shark sees that you are scared and comes up to you. \n He introduces himself as Ceasar and you become best friends. \nAs your wingman, he spots a pretty lady across the pool. Do you…")
        lChoice = self.lButton("Buy her a drink", lambda: self.badDay(lChoice, rChoice, img, text))
        rChoice = self.rButton("Spill your drink on yourself", lambda: self.die(lChoice, rChoice, img, text))
        

    def badDay(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("BadDayBide.png")
        text=self.showText("After having a few drinks, you start feeling sick. Do you..")
        lChoice = self.lButton("Go to the bathroom", lambda: self.die(lChoice, rChoice, img, text))
        rChoice = self.rButton("Get over yourself", lambda: self.kareoke(lChoice, rChoice, img, text))
       
        
        
    def kareoke(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Kareoke.png")
        text=self.showText("To thank you for her a drink, Auntie Jemima invites you to a karaoke contest. \n Do you..")
        lChoice = self.lButton("Sing Hymn #602", lambda: self.die(lChoice, rChoice, img, text))
        rChoice = self.rButton("Sing a Backstreet Boys song", lambda: self.coldfeet(lChoice, rChoice, img, text))
       
        
    def coldfeet(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Wedding.png")
        text=self.showText("You wooed Auntie Jemima with your incredible singing skills and propose to her. \n She says yes! Later that night, you are getting ready for the wedding. \n Do you…")
        lChoice = self.lButton("Get there on time.", lambda: self.theEnd(lChoice, rChoice, img, text))
        rChoice = self.rButton("Show up Late", lambda: self.die(lChoice, rChoice, img, text))
        

    def theEnd(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("Wedding.png")
        secret=Button(self,text= "Congratulations!", command=lambda: self.runAway(lChoice, rChoice, secret, img, text), font=('Sans Serif', 25), width= 54)
        secret.place(x=100, y=610)
        text=self.showText(" \n You and Auntie Jemima got married and had Ceasar as your best man. \n Do you want to..")
        lChoice = self.lButton("Exit the Game", lambda: self.client_exit())
        rChoice = self.rButton("Play Again", lambda: self.start3(lChoice, rChoice, secret, img, text))
        

    def runAway(self, button1, button2,button,img,text):
        self.dB2(button1, button2, button, img, text)
        img=self.showImg("RUN AWAY.png")
        text=self.showText("You go outside to sunbathe and you see a bunny in the corner of your yard. Do you..")
        lChoice = self.lButton("MURDER", lambda: self.win(lChoice, rChoice, img, text))
        rChoice = self.rButton("murder", lambda: self.die(lChoice, rChoice, img, text))
    def runAway2(self, button1, button2,img,text):
        self.dB(button1, button2, img, text)
        img=self.showImg("RUN AWAY.png")
        text=self.showText("You go outside to sunbathe and you see a bunny in the corner of your yard. Do you..")
        lChoice = self.lButton("MURDER", lambda: self.win(lChoice, rChoice, img, text))
        rChoice = self.rButton("murder", lambda: self.die(lChoice, rChoice, img, text))

    def die2(self, button1, button2, button, img, text):
        self.dB2(button1, button2, button3, img, text) 
        img=self.showImg("GameOver.png")
        new= Button(self, text="Restart", command=lambda: self.start1(new,img),font=('Sans Serif', 30))
        new.place(x= 300, y= 200)

    def die(self, button1, button2, img, text):
        self.dB(button1, button2, img, text) 
        img=self.showImg("GameOver.png")
        new= Button(self, text="Restart", command=lambda: self.start(new,img),font=('Sans Serif', 30))
        new.place(x= 300, y= 200)
        
    def win(self, button1, button2, img, text):
        self.dB(button1, button2, img, text) 
        img=self.showImg("RUN AWAY.png")
        text = Label(self, text="YOU WIN- \n THE PINK BELT IS YOURS FOR THE TAKING", font=('Sans Serif', 50))
        text.pack()
        text.place(x=0, y=300)
        buttonQuit = Button(self,text="Quit", command=self.client_exit, font=('Sans Serif', 30))
        buttonQuit.place(x=100, y=500)
        game= Button(self, text="Restart", command=lambda: self.start2(game, buttonQuit, img, text),font=('Sans Serif', 30))
        game.place(x= 700, y= 500)

    def dB3(self, button1, img):
        button1.destroy()
        img.destroy()
        
    def dB2(self, button1, button2, button3, img, text):
        button1.destroy()
        button2.destroy()
        button3.destroy()
        img.destroy()
        text.destroy()
        
    def dB(self, button1, button2, img, text):
        button1.destroy()
        button2.destroy()
        img.destroy()
        text.destroy()
        
    def rButton(self, text2, command2):
        Choice = Button(self, text=text2, command=command2,font=('Sans Serif', 30))
        Choice.place(x=650, y=0)
        return Choice

    def lButton(self, text2, command2):
        Choice = Button(self, text=text2, command=command2, font=('Sans Serif', 30))
        Choice.place(x=100, y=0)
        return Choice
        
    def showImg(self, pic):
        load = Image.open(pic)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        return img


    def showText(self,word):
        text = Label(self, text=word, font=('Sans Serif', 25))
        text.pack()
        text.place(x=100, y=675)
        return text

        

    def client_exit(self):
        exit()



    def wabbits(self, button1, button2, img, text):
        self.timer.reset()
        self.timer.start()
        timer = self.showText(self.timer.t.get())
        timer.place(x=0,y=0)
        self.clicks=0
        self.dB(button1, button2, img, text)
        Choice = Button(self, text="wabbits", command=lambda: self.wabbits2(Choice), font=('Sans Serif', 30))
        x=random()*500
        y=random()*500
        Choice.place(x=x, y=y)
        self.showText(str(self.clicks))
        
    def wabbits2(self,Choice):
        timer = self.showText(self.timer.t.get())
        timer.place(x=0,y=0)
        self.clicks= self.clicks +1
        self.dR(Choice)
        Choice = Button(self, text="wabbits", command=lambda: self.wabbits2(Choice), font=('Sans Serif', 30))
        x=random()*500
        y=random()*500
        Choice.place(x=x, y=y)
        self.showText(str(self.clicks))


    def dR(self, button1):
        button1.destroy()

 


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
