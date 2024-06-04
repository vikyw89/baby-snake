import random
from baby_snake.constants.index import CANVAS_HEIGHT, CANVAS_WIDTH, GOAL_COLOR, SIZE
from baby_snake.utils.index import generate_random_coordinate
from libs.graphics import Canvas


class Goal:
    def __init__(
        self,
        canvas: Canvas,
        x: int = random.randint(0, int((CANVAS_WIDTH - SIZE) / SIZE)) * SIZE,
        y: int = random.randint(0, int((CANVAS_HEIGHT - SIZE) / SIZE) * SIZE),
    ):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, GOAL_COLOR)

    def random_respawn(self) -> None:
        # generate new location
        coordinate = []

        # check if there's overlap
        while (
            len(coordinate) == 0
            or len(
                self.canvas.find_overlapping(
                    coordinate[0],
                    coordinate[1],
                    coordinate[0] + SIZE,
                    coordinate[1] + SIZE,
                )
            )
            == 0
        ):
            coordinate = generate_random_coordinate()
            self.canvas.moveto(self.id, coordinate[0], coordinate[1])

    def is_captured(self, player_coordinate: list) -> bool:
        # return true if captured
        x = self.canvas.get_left_x(self.id)
        y = self.canvas.get_top_y(self.id)

        if player_coordinate[0] == x and player_coordinate[1] == y:
            return True

        return False
