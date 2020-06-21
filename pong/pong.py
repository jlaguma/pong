import turtle
import os
import sys
import time
import winsound


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f'Player(name={self.name}, color={self.color})'


class Pong:
    def __init__(self,
                 player_1_name='Player 1',
                 player_1_color='white',
                 player_2_name='Player 2',
                 player_2_color='white'):
        self.ball_speed = 0.4
        self.max_speed = 0.6
        self.speed_increment = 30
        self.score_1 = 0
        self.score_2 = 0
        self.time_checkin = time.time()

        # setup players
        self.player_1 = Player(name=player_1_name, color=player_1_color)
        self.player_2 = Player(name=player_2_name, color=player_2_color)

        # setup screen
        self.win = self.screen()
        self.pen = self.draw_score()

        # setup paddles and ball
        self.paddle_1 = self.paddle(color=self.player_1.color, x=-350, y=0)
        self.paddle_2 = self.paddle(color=self.player_2.color, x=350, y=0)

        # setup ball
        self.ball = self.ball(color='white', x=0, y=0)

        # setup keyboard
        self.win.listen()
        self.win.onkeypress(self.paddle_1_up, 'w')
        self.win.onkeypress(self.paddle_1_down, 's')
        self.win.onkeypress(self.paddle_2_up, 'Up')
        self.win.onkeypress(self.paddle_2_down, 'Down')

    def play(self):
        """Game logic."""
        while True:
            self.win.update()
            # move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # bounce off the roof
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                # change the direction of the ball
                self.ball.dy *= -1
                self.play_sound('windows', 'bounce.wav')

            # bounce off the floor
            if self.ball.ycor() < -290:
                self.ball.sety(-290)
                # change the direction of the ball
                self.ball.dy *= -1
                self.play_sound('windows', 'bounce.wav')

            # bounce off the player 2 paddle
            if self.ball.xcor() > 330 and self.ball.xcor(
            ) < 340 and self.paddle_2.ycor() - 50 <= self.ball.ycor(
            ) <= self.paddle_2.ycor() + 50:
                self.ball.setx(330)
                self.ball.dx *= -1
                self.play_sound('windows', 'pong2.wav')

            # bounce off the player 1 paddle
            if self.ball.xcor() < -330 and self.ball.xcor(
            ) > -340 and self.paddle_1.ycor() - 50 <= self.ball.ycor(
            ) <= self.paddle_1.ycor() + 50:
                self.ball.setx(-330)
                self.ball.dx *= -1
                self.play_sound('windows', 'pong1.wav')

            if self.ball.xcor() > 390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_1 += 1
                self.pen.clear()
                self.pen.write(
                    f'{self.player_1.name}: {self.score_1}  {self.player_2.name}: {self.score_2}',
                    align='center',
                    font=('Courier', 24, 'bold'))
                self.play_sound('windows', 'miss.wav')
                self.pause = False

            if self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_2 += 1
                self.pen.clear()
                self.pen.write(
                    f'{self.player_1.name}: {self.score_1}  {self.player_2.name}: {self.score_2}',
                    align='center',
                    font=('Courier', 24, 'bold'))
                self.play_sound('windows', 'miss.wav')

    def screen(self):
        """Setup a game screen."""
        win = turtle.Screen()
        win.title('Pong by James La Guma')
        win.bgcolor('black')
        win.setup(width=800, height=600)
        # prevent window from updating so game is faster
        win.tracer(0)
        return win

    def draw_score(self):
        """Use a pen to draw a score on the screen."""
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write(f'{self.player_1.name}: 0  {self.player_2.name}: 0',
                  align='center',
                  font=('Courier', 24, 'bold'))
        return pen

    def paddle(self, color, x, y):
        """Setup a paddle."""
        paddle = turtle.Turtle()
        # speed of animation set to max speed
        paddle.speed(0)
        # default size is 20x20
        paddle.shape('square')
        paddle.color(color)
        # 5 times wider, with original length
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(x, y)
        return paddle

    def ball(self, color, x, y):
        """Setup a ball."""
        ball = turtle.Turtle()
        # speed of animation set to max speed
        ball.speed(0)
        # default size is 20x20
        ball.shape('circle')
        ball.color(color)
        ball.penup()
        ball.goto(x, y)
        # this defined by how many pixels ball will move by
        ball.dx = self.ball_speed
        ball.dy = self.ball_speed
        return ball

    def play_sound(self, opsys, sound):
        """Play a sound file."""
        if opsys == 'linux':
            os.system(f'aplay pong/sound/{sound} &')
        elif opsys == 'mac':
            os.system(f'afplay pong/sound/{sound} &')
        elif opsys == 'windows':
            winsound.PlaySound(f'pong/sound/{sound}', winsound.SND_ASYNC)

    def paddle_1_up(self):
        """Paddle 1 up movement."""
        y = self.paddle_1.ycor()
        if y < 250:
            y += 20
            self.paddle_1.sety(y)

    def paddle_1_down(self):
        """Paddle 1 down movement."""
        y = self.paddle_1.ycor()
        if y > -250:
            y -= 20
            self.paddle_1.sety(y)

    def paddle_2_up(self):
        """Paddle 2 up movement."""
        y = self.paddle_2.ycor()
        if y < 250:
            y += 20
            self.paddle_2.sety(y)

    def paddle_2_down(self):
        """Paddle 2 down movement."""
        y = self.paddle_2.ycor()
        if y > -250:
            y -= 20
            self.paddle_2.sety(y)
