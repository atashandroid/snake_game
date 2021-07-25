from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.snake_make()
        self.snake[0].color('red')
        self.head = self.snake[0]

    def snake_make(self):
        for i in range(3):
            self.snake.append(Turtle("circle"))
            self.snake[i].penup()
            self.snake[i].color("brown")
            self.snake[i].goto(i * 20 * -1, 0)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.snake_make()
        self.snake[0].color('red')
        self.head = self.snake[0]

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def add(self):
        tmp = len(self.snake) - 1
        cor_x = self.snake[tmp].xcor()
        cor_y = self.snake[tmp].ycor()
        self.snake.append(Turtle("circle"))
        tmp = len(self.snake) - 1
        self.snake[tmp].goto(cor_x, cor_y)
        self.snake[tmp].color("brown")
        self.snake[tmp].penup()
