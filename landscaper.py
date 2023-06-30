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

toolShop = [
    {
        "name": "rusty scissors",
        "cost": 5,
        "profit": 5
    },
    {
        "name": "push lawnmower",
        "cost": 25,
        "profit": 25
    },
    {
        "name": "fancy lawnmower",
        "cost": 50,
        "profit": 50
    },
    {
        "name": "riding mower",
        "cost": 200,
        "profit": 100
    },
    {
        "name": "team of students",
        "cost": 500,
        "profit": 250
    },
]

# ~~~~~~~~~~~~~~~~
# Define Functions
# ~~~~~~~~~~~~~~~~


def getName():
    playGame = input("Would you like to play a game? Y or N: ")
    if playGame.lower() == 'y':
        # Get the players name set it to our dictionary key value
        player["name"] = input("Please enter your name: ")
    elif playGame.lower() == 'n':
      # Exit conditional
        print("See you later!")
        exit()
    else:
      # Validation
        print("\n!!!\tPlease enter Y or N\t!!!\n")
        getName()


def goToShop():
    # I want an index so I use the range method along with the len method
    for i in range(len(toolShop)):
        print(toolShop[i])


def dailyChoice():
    print(f"You have ${player['money']} to your name.")
    choice = input(
        f"What would you like to do today?\n\t1. Mow the lawn with your {player['toolBag'][0]['name']}\n\t2. Go to the tool shop\n\tQ. EXIT: ")

    if choice == "1":
        player["money"] += player["toolBag"][0]["profit"]
    elif choice == "2":
        goToShop()
    elif choice.lower() == "q":
        # put this into a function later
        print("Thanks for playing!")
        exit()
    else:
        print("\n!!!\tPlease enter 1, 2, 3 or Q\t!!!\n")


# ~~~~~~~~~~~~~~
# Call Functions
# ~~~~~~~~~~~~~~
getName()

while player["money"] <= 20:
    dailyChoice()
    # print(
    #     f"Hello {player['name']} you are using your {player['toolBag'][0]['name']}")
