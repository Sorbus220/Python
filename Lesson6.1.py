import turtle

wn = turtle.Screen()
wn.title('TrafficLight')
wn.bgcolor('black')


class Trafficlight:
    __color = ['grey', 'red', 'yellow', 'green']

    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color('grey')
        self.pen.width(4)
        self.pen.hideturtle()
        self.pen.goto(-30, 60)
        self.pen.down()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)

        self.color = ""

        self.red_light = turtle.Turtle()
        self.green_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()

        self.red_light.speed(0)
        self.green_light.speed(0)
        self.yellow_light.speed(0)

        self.red_light.color(Trafficlight.__color[0])
        self.green_light.color(Trafficlight.__color[0])
        self.yellow_light.color(Trafficlight.__color[0])

        self.red_light.shape('circle')
        self.green_light.shape('circle')
        self.yellow_light.shape('circle')

        self.red_light.penup()
        self.green_light.penup()
        self.yellow_light.penup()

        self.red_light.goto(0, 40)
        self.yellow_light.goto(0, 0)
        self.green_light.goto(0, -40)

    def change_color(self, color):
        self.red_light.color(Trafficlight.__color[0])
        self.yellow_light.color(Trafficlight.__color[0])
        self.green_light.color(Trafficlight.__color[0])
        if color == 'red':
            self.red_light.color(Trafficlight.__color[1])
            self.color = Trafficlight.__color[1]
        elif color == 'yellow':
            self.yellow_light.color(Trafficlight.__color[2])
            self.color = Trafficlight.__color[2]
        elif color == 'green':
            self.green_light.color(Trafficlight.__color[3])
            self.color = Trafficlight.__color[3]

    def timer(self):
        if self.color == 'red':
            self.change_color(Trafficlight.__color[3])
            wn.ontimer(self.timer, 7000)
        elif self.color == 'yellow':
            self.change_color(Trafficlight.__color[1])
            wn.ontimer(self.timer, 5000)
        elif self.color == 'green':
            self.change_color(Trafficlight.__color[2])
            wn.ontimer(self.timer, 2000)


trafficlight = Trafficlight()
trafficlight.change_color("red")
trafficlight.timer()

wn.mainloop()
