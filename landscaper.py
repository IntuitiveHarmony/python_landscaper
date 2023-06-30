# ~~~~~~~~~~~~~~~~~~~~~~
# Define Game parameters
# ~~~~~~~~~~~~~~~~~~~~~~

player = {
    "name": "",
    "money": 0,
    "toolBag": [
        {
            "name": "teeth",
            "profit": 1
        }
    ]
}

# ~~~~~~~~~
# Functions
# ~~~~~~~~~


def getName():
    playGame = input("Would you like to play a game? Y or N: ")
    if playGame.lower() == 'y':
        # Get the players name
        player["name"] = input("Please enter your name: ")
    elif playGame.lower() == 'n':
      # Exit conditional
        print("See you later!")
        exit()
    else:
      # Validation
        print("\n!!!\tPlease enter Y or N\t!!!\n")
        getName()


getName()

print(
    f"Hello {player['name']} you are using your {player['toolBag'][0]['name']}")
