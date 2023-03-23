from tkinter import *
from random import randint

#Размер окна
sqreen_X = 1000
sqreen_Y = 1000

class Ball():

    def __init__(self):
        self.R = randint(20,50)
        self.x = randint(10, sqreen_X-self.R)
        self.y = self.x
        self.dx,self.dy = (randint(5,15),randint(5,15))
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill = "green")

    def move(self):
        self.x +=self.dx
        self.y +=self.dy

        if (self.x+self.R >=sqreen_X) or (self.x-self.R <=0):
           self.dx = - self.dx
        if (self.y+self.R >=sqreen_Y) or (self.y-self.R <=0):
            self.dy = - self.dy
        step = 0
        for ball in balls:
            if step == 0:
                 ball_1 = ball
            else:
                ball_2 = ball
                if ((ball_1.x+ball_1.R)-(ball_2.x+ball_2.R)<0) and ((ball_1.y+ball_1.R)-(ball_2.y+ball_2.R)<0):
                    ball_1.dx, ball_1.dy = -ball_1.dx, -ball_1.dy
                    ball_2.dx, ball_2.dy = -ball_2.dx, -ball_2.dy
        step += 1




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


