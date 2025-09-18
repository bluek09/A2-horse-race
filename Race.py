from graphics import *
from Dice import Dice
import time


class Horse:
    def __init__(self, speed, y, image, window):
        self.x_pos = 0
        self.y_pos = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self):
        step = self.dice.roll()
        self.x_pos += step

    def draw(self):
        self.image.draw_at_pos(self.window, self.x_pos, self.y_pos)

    def crossed_finish_line(self, finish_x):
        return self.x_pos >= finish_x




def main():
    win_width, win_height = 700, 350
    win = GraphWin("Horse Race", win_width, win_height)

    horse1_img = Image(Point(0, 0), "Knight.gif")
    horse2_img = Image(Point(0, 0), "Wizard.gif")

    horse1 = Horse(speed=6, y=100, image=horse1_img, window=win)
    horse2 = Horse(speed=6, y=200, image=horse2_img, window=win)

    finish_x = 600
    finish_line = Line(Point(finish_x, 0), Point(finish_x, win_height))
    finish_line.draw(win)

    horse1.draw()
    horse2.draw()

    win.getMouse()

    race_over = False
    while not race_over:
        horse1.undraw()
        horse2.undraw()

        horse1.move()
        horse2.move()

        horse1.draw()
        horse2.draw()

        race_over = horse1.crossed_finish_line(finish_x) or horse2.crossed_finish_line(finish_x)
        time.sleep(0.2)

    if horse1.crossed_finish_line(finish_x) and horse2.crossed_finish_line(finish_x):
        print("Tie")
    elif horse1.crossed_finish_line(finish_x):
        print("Horse 1 is the winner")
    else:
        print("Horse 2 is the winner")

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
