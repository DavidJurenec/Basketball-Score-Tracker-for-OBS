import tkinter as tk

def update_score(team, points):
    file_name = f"{team.lower()}.txt"
    try:
        with open(file_name, 'r') as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    new_score = current_score + points

    with open(file_name, 'w') as file:
        file.write(str(new_score))

    return new_score

def get_initial_score(team):
    file_name = f"{team.lower()}.txt"
    try:
        with open(file_name, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def reset_scores():
    global current_home_score, current_guest_score
    current_home_score = 0
    current_guest_score = 0

    update_score_display()

    with open("home.txt", 'w') as home_file:
        home_file.write("0")

    with open("guest.txt", 'w') as guest_file:
        guest_file.write("0")

def on_button_click(team, points):
    global current_home_score, current_guest_score
    current_score = update_score(team, points)

    if team == home_team:
        current_home_score = current_score
    elif team == guest_team:
        current_guest_score = current_score

    update_score_display()

def update_score_display():
    score_label_var.set(f"{home_team}: {current_home_score}  :  {guest_team}: {current_guest_score}")

root = tk.Tk()
root.title("Basketball Score Tracker")
root.geometry("500x400") 

home_team = "HOME"
guest_team = "GUEST"
current_home_score = get_initial_score(home_team)
current_guest_score = get_initial_score(guest_team)

score_label_var = tk.StringVar()
score_label_var.set(f"{home_team}: {current_home_score}  :  {guest_team}: {current_guest_score}")
score_label = tk.Label(root, textvariable=score_label_var, font=('Helvetica', 16))
score_label.pack(pady=10)

home_buttons_frame = tk.Frame(root)
home_buttons_frame.pack(side=tk.LEFT, padx=10)

home_buttons = [
    ("+3", 3), ("+2", 2), ("+1", 1),
    ("-1", -1), ("-2", -2), ("-3", -3)
]

for text, points in home_buttons:
    button = tk.Button(home_buttons_frame, text=text, command=lambda p=points, t=home_team: on_button_click(t, p), height=2, width=5)
    button.pack(pady=5)

guest_buttons_frame = tk.Frame(root)
guest_buttons_frame.pack(side=tk.RIGHT, padx=10)

guest_buttons = [
    ("+3", 3), ("+2", 2), ("+1", 1),
    ("-1", -1), ("-2", -2), ("-3", -3)
]

for text, points in guest_buttons:
    button = tk.Button(guest_buttons_frame, text=text, command=lambda p=points, t=guest_team: on_button_click(t, p), height=2, width=5)
    button.pack(pady=5)

reset_button = tk.Button(root, text="RESET", command=reset_scores)
reset_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()