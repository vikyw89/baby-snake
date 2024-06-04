from baby_snake.constants.index import PLAYER_COLOR, SIZE
from libs.graphics import Canvas


class SnakeBody:
    def __init__(self, canvas: Canvas, x: int, y: int):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, PLAYER_COLOR)

    def remove(self):
        self.canvas.delete(self.id)

    def coordinate(self):
        x = self.canvas.get_left_x(self.id)
        y = self.canvas.get_top_y(self.id)
        return [x, y]