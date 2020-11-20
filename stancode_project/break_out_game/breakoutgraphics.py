"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program plays a game called
"break out" in which players
moving the paddle to make the ball bounce
and break all bricks!
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-paddle_width)//2, self.window.height - paddle_offset - brick_height)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-self.ball.width)//2, (self.window.height-self.ball.height)//2)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy

        # score board
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.window.add(self.score_label, 0, self.window.height-self.score_label.height)

        self.game_over_label = GLabel('GAME OVER')
        self.game_over_label.font = ('-60')

        # Initialize our mouse listeners.
        onmousemoved(self.move_mouse)

        onmouseclicked(self.click_mouse)

        # The switch for mouse click
        self.is_started = False

        # Draw bricks.
        for i in range(brick_rows//2):
            for j in range(brick_rows//5, 0, -1):
                for k in range(0, self.window_width, (brick_spacing + brick_width)):
                    brick = GRect(brick_width, brick_height)
                    brick.filled = True
                    if i == 0:
                        brick.fill_color = 'red'
                        brick.color = 'red'
                    elif i == 1:
                        brick.fill_color = 'orange'
                        brick.color = 'orange'
                    elif i == 2:
                        brick.fill_color = 'yellow'
                        brick.color = 'yellow'
                    elif i == 3:
                        brick.fill_color = 'green'
                        brick.color = 'green'
                    elif i == 4:
                        brick.fill_color = 'blue'
                        brick.color = 'blue'
                    self.window.add(brick, k, brick_offset + (brick_height + brick_spacing)*((i*2)-j))

    def game_over(self):
        self.window.add(self.game_over_label, (self.window_width - self.game_over_label.width) // 2,
                        (self.window.height - self.game_over_label.height) // 2 - 20)

    def move_mouse(self, move_paddle):
        """
        The function of onmousemove.
        """
        if 0 + self.paddle.width//2 < move_paddle.x < self.window.width - self.paddle.width//2:
            self.paddle.x = move_paddle.x - self.paddle.width//2

        # We need to fix paddle on the left side.
        if move_paddle.x <= self.paddle.width//2:
            self.paddle.x == 0

        # We need to fix paddle on the right side.
        if move_paddle.x >= self.window.width - self.paddle.width:
            self.paddle.x == self.window.width - self.paddle.width//2

    def click_mouse(self, move_ball):
        """
        The function of onmouseclick.
        """

        # the ball on the original place and turn on the switch
        if self.ball.x == (self.window.width-self.ball.width)//2 and \
                self.ball.y == (self.window_height - self.ball.height)//2:
            self.is_started = True

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

        # Rebound from left and right side
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx

        # Rebound from top side
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def break_brick(self):

        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        right_up = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_down = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # Left up side get object
        if left_up is not None and left_up is not self.paddle and left_up is not self.score_label:
            self.window.remove(left_up)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

        # Right up side get object
        if right_up is not None and right_up is not self.paddle and right_up is not self.score_label:
            self.window.remove(right_up)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

            # While left up and right up get the same object , we just get one point
            if left_up is right_up:
                self.score -= 1
                self.score_label.text = 'Score: ' + str(self.score)

        # Left down side get object
        if left_down is not None and left_down is not self.paddle and left_down is not self.score_label:
            self.window.remove(left_down)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

        # Right down side get object
        if right_down is not None and right_down is not self.paddle and right_down is not self.score_label:
            self.window.remove(right_down)
            self.score += 1
            self.score_label.text = 'Score: ' + str(self.score)

            # while left down and right down get the same object , we just get one point
            if left_down is right_down:
                self.score -= 1
                self.score_label.text = 'Score: ' + str(self.score)

        # When ball hit brick or paddle , it will rebound
        if left_up is not None or right_up is not None or left_down is not None or right_down is not None:
            self.__dy = -self.__dy
            if left_up is self.score_label or right_up is self.score_label or left_down is self.score_label or \
                    right_down is self.score_label:
                self.__dy = -self.__dy

        if left_down is self.paddle or right_down is self.paddle:
            if self.__dy > 0:
                self.__dy = -self.__dy