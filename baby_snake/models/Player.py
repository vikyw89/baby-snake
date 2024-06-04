from baby_snake.constants.index import CANVAS_HEIGHT, CANVAS_WIDTH, PLAYER_COLOR, SIZE
from baby_snake.models.SnakeBody import SnakeBody
from libs.graphics import Canvas


class Player:
    def __init__(self, canvas: Canvas, x: int = 0, y: int = 0):
        self.canvas = canvas
        # TODO: use queue, for O1
        self.body: list[SnakeBody] = []
        self.id = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, PLAYER_COLOR)
        self.length = 0
        self.direction = "right"

    def move(self) -> None:
        direction = self.get_input()
        DIRECTION_MAP = {
            "right": [1 * SIZE, 0],
            "left": [-1 * SIZE, 0],
            "down": [0, 1 * SIZE],
            "up": [0, -1 * SIZE],
        }
        delta_move = DIRECTION_MAP[direction]
        current_coordinate = self.coordinate()

        # move body
        # add current position to body
        self.body.append(
            SnakeBody(self.canvas, x=current_coordinate[0], y=current_coordinate[1])
        )

        # resize body
        body_to_trim = len(self.body) - self.length
        if body_to_trim > 0:
            # cleanup snake body
            body = self.body[0]
            body.remove()
            self.body.pop(0)

        # append current position
        self.canvas.move(self.id, delta_move[0], delta_move[1])

    def is_out_of_bound(self):
        x, y = self.coordinate()

        if x < 0 or y < 0 or x >= CANVAS_WIDTH or y >= CANVAS_HEIGHT:
            return True

        return False

    def coordinate(self):
        x = self.canvas.get_left_x(self.id)
        y = self.canvas.get_top_y(self.id)
        return [x, y]

    def grow(self):
        self.length += 1

    def is_hitting_self(self) -> bool:
        # skip if body is 0
        if self.length == 0:
            return False

        x, y = self.coordinate()

        collisions = self.canvas.find_overlapping(x, y, x + SIZE, y + SIZE)

        if len(collisions) > 1:
            # do a check on body
            for body in self.body:
                body: SnakeBody
                body_x, body_y = body.coordinate()
                if body_x == x and body_y == y:
                    return True

        return False

    def get_input(self):
        key = self.canvas.get_new_key_presses()
        if len(key) == 0:
            key = None
        else:
            key = key[-1]
        # prevent 180 degree moves
        if key == "ArrowLeft" and self.direction != "right":
            self.direction = "left"
        if key == "ArrowRight" and self.direction != "left":
            self.direction = "right"
        if key == "ArrowUp" and self.direction != "down":
            self.direction = "up"
        if key == "ArrowDown" and self.direction != "up":
            self.direction = "down"
        return self.direction
