import time
from baby_snake.constants.index import CANVAS_HEIGHT, CANVAS_WIDTH, DELAY
from baby_snake.models.Goal import Goal
from baby_snake.models.Player import Player
from libs.graphics import Canvas


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    game_state = {
        "player": Player(canvas=canvas),
        "goals": [Goal(canvas=canvas)],
        "delay": DELAY,
        "score": 0,
        "obstacles": [],
    }

    score = None

    while True:
        # render score
        if score:
            canvas.delete(score)
        score = canvas.create_text(
            5,
            CANVAS_HEIGHT - 20,
            text=f"""Score: {str(game_state["score"])}""",
            font="Roboto",
            font_size=str(20),
            color="grey",
        )

        # move player
        game_state["player"].move()

        # check collision
        if game_state["player"].is_out_of_bound():
            break

        if game_state["player"].is_hitting_self():
            break

        # check captured
        for goal in game_state["goals"]:
            if goal.is_captured(player_coordinate=game_state["player"].coordinate()):
                # move the goal
                goal.random_respawn()

                # increase speed
                game_state["delay"] -= 0.01

                # add score
                game_state["score"] += 1

                # add length
                game_state["player"].grow()

        time.sleep(game_state["delay"])
    canvas.clear()
    canvas.create_text(
        CANVAS_WIDTH / 8,
        CANVAS_HEIGHT / 3,
        text=f"GAME OVER",
        font="Roboto",
        font_size=str(50),
        color="red",
    )
    canvas.create_text(
        CANVAS_WIDTH / 7,
        CANVAS_HEIGHT / 2,
        text=f"Your score is {game_state['score']}",
        font_size=str(30),
        color="RED",
    )


if __name__ == "__main__":
    main()
