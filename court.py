from turtle import Turtle
STARTING_POSITIONS = [(0, 240), (0, 120), (0, 0), (0, -120), (0, -240)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.goto(0, 275)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.p1_score}    |    Score:  {self.p2_score}", False, "center", ("Arial", 16, "normal"))


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.setup_net()

    def setup_net(self):
        for position in STARTING_POSITIONS:
            net = Turtle("square")
            net.color("white")
            net.penup()
            net.resizemode("user")
            net.shapesize(stretch_wid=1, stretch_len=0.2, outline=1)
            net.goto(position)
            self.segments.append(net)
