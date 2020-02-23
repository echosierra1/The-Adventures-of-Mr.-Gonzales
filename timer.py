from tkinter import *
global count
count=0
class timer():
    
    def reset(self):
        global count
        if self.option == 0:
            self.t.set('00:00:00')
        elif self.option == 1:
            self.t.set('00:01:00')
        count=1
        
    def start(self):
        global count
        if self.option == 1:
            count=2
        elif self.option == 0:
            count = 0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
        
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(930,self.start_timer)
        elif count == 2:
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            h = int(h)
            m=int(m)
            s= int(s)
            if(m == 1):
                s = 60
                m = 00
            if(s<=60):
                s-=1
            if int(s) <= 0:
                self.stop()
            s=str(s) 
            h=str(h) + str(0)
            m=str(m) + str(0)
            
            if int(s) <= 9:
                self.d=h+":"+m+":0"+s
            else:
                self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==2):
                self.root.after(930,self.start_timer)
        
    def __init__(self, root, option):
        self.root=root
        self.t = StringVar()
        self.option = option
        if self.option == 0:#increments until stopped
            self.t.set("00:00:00")
        elif self.option == 1:#decrements starting at one minute
            self.t.set("00:01:00")
            
