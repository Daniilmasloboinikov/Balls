from tkinter import *
from random import randint
from math import fabs

#Размер окна
sqreen_X = 500
sqreen_Y = 500

class Ball():

    def __init__(self):
        self.R = randint(20,30)
        self.x = randint(10, sqreen_X-self.R)
        self.y = self.x
        self.dx,self.dy = (randint(-10,10),randint(-10,10))
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill = "green")

    def move(self):
        for ball in balls:
            if self != ball:
                distance = fabs((pow(self.x,2)+pow(self.y,2))**(0.5)-(pow(ball.x,2)+pow(ball.y,2))**(0.5))
                if (distance<(self.R+ball.R)):
                    self.dx, self.dy = -self.dx, -self.dy
                    ball.dx, ball.dy = -ball.dx, -ball.dy

        self.x +=self.dx
        self.y +=self.dy

        if (self.x+self.R >=sqreen_X) or (self.x-self.R <=0):
           self.dx = - self.dx
        if (self.y+self.R >=sqreen_Y) or (self.y-self.R <=0):
            self.dy = - self.dy







    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


# ------------------------------------------------------------


def tick():
     for ball in balls:
        ball.move()
        ball.show()
     root.after(50, tick)


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

# --------------------------------------------------------------
def main():
    global root, canvas, balls, couple

    root = Tk()
    root.geometry("300x250")
    root.attributes("-fullscreen", True)



    canvas = Canvas(bg="white", width=sqreen_X, height=sqreen_Y)
    canvas.pack(anchor=CENTER, expand=1)

    # label = Label(text = "My balls")
    # label.pack(padx=50, pady=50)
    couple = randint(2,10)
    balls = [Ball() for i in range(couple)]
    tick()

    root.title("Hello METANIT.COM")
    root.protocol("WM_DELETE_WINDOW", finish)



    root.mainloop()

if __name__ == "__main__":
    main()


