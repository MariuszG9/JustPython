import turtle as turt
import pandas as pd

screen = turt.Screen()
screen.title("Gra Stany USA")

mapImage = "blank_states_img.gif"
screen.addshape(mapImage)
turt.shape(mapImage)

df_coords = pd.read_csv("50_states.csv")
states_coords = df_coords.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    state = screen.textinput(title=f"{len(states_guessed)}/50",
                            prompt="Jak jest nazwa kolejnego stanu?").title()
    if state == "Escape":
        states_missing = []
        for stat in states_coords:
            if stat not in states_guessed:
                states_missing.append(stat)
        missing_data = pd.DataFrame(states_missing)
        missing_data.to_csv("states_you_missed.csv")
        break

    if state in states_coords:
        states_guessed.append(state)
        mapper = turt.Turtle()
        mapper.hideturtle()
        mapper.penup()
        coord = df_coords[df_coords.state == state]
        mapper.goto(int(coord.x), int(coord.y))
        mapper.write(state)
