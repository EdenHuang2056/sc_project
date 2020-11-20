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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    num_lives = NUM_LIVES
    graphics = BreakoutGraphics()

    while True:
        pause(FRAME_RATE)
        if graphics.is_started:
            graphics.move_ball()
            graphics.break_brick()
            if graphics.ball.y >= graphics.window.height:
                num_lives -= 1
                graphics.ball.x = (graphics.window.width - graphics.ball.width)//2
                graphics.ball.y = (graphics.window.height - graphics.ball.height)//2
                graphics.is_started = False
        if graphics.score == 100:
            break
        if num_lives == 0:
            graphics.game_over()
            break


if __name__ == '__main__':
    main()
