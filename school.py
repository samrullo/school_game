answer = input("Teacher came! To play on smartphone or sit and wait? Type 'play' or 'wait'.")

while answer not in ["play", "wait"]:
    answer = input("Teacher came! To play on smartphone or sit and wait? Type 'play' or 'wait'.")
if answer == "play":
    print(
        "You are playing. Teacher came in one second. You were taken to the principal. You were chased out of school.")
    while answer not in ["home", "movie"]:
        answer = input("What will you do? Go home or go to movies with your friends. Type 'home' or 'movie'")
    if answer == "movie":
        print("Your mom stumbles upon you in movie theater")
        while answer not in ["out", "endure"]:
            answer = input("Get out or endure? Type 'out' or 'endure'")
        if answer == "out":
            print("Well done! But you need to wait 4 hours before going home!")
        elif answer == "endure":
            print("Your mother found you and beat you with a belt. You were accidentally killed")
            while answer not in ["heaven", "hell"]:
                answer = input("Heaven or Hell? Type 'heaven' or 'hell'")
            if answer == "heaven":
                print("Well done! You are Rich!")
            elif answer == "hell":
                print("Game Over!")
    elif answer == "home":
        while answer not in ["escape","police"]:
            answer = input(
                "Your folks are being attacked and they are dieing. What are you gonna do? Escape or call the police? Type 'escape' or 'police'")
        if answer == "police":
            print("You called police. Police is on holidays. You just wasted your time.")
elif answer == "wait":
    print("Well done! First lesson is music! School finished!")
