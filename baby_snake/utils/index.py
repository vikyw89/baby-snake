import random
from baby_snake.constants.index import CANVAS_HEIGHT, CANVAS_WIDTH, SIZE


def generate_random_coordinate() -> list:
    x = random.randint(0, int((CANVAS_WIDTH - SIZE) / SIZE)) * SIZE
    y = random.randint(0, int((CANVAS_HEIGHT - SIZE) / SIZE)) * SIZE
    return [x, y]
