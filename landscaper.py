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
currentTool = player["toolBag"][0]


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
        "name": "drone mower",
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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to the Tool Shop!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # Make sure array isn't empty because we will be removing items
    if len(toolShop) > 0:
        # Loop through tool shop and print the options
        for i in range(len(toolShop)):
            print(
                f"{i + 1}. {toolShop[i]['name']} - Profit: ${toolShop[i]['profit']} - Cost: ${toolShop[i]['cost']}")
    else:
        print("Sorry, we are sold out!")
        dailyChoice()
    # Convert choice to an int so you can target list elements
    choice = int(input("\nWhat would you like to purchase?: "))

    # Check for funds
    # If they are suffucient
    if toolShop[choice - 1]["cost"] <= player["money"]:
        # Subtract cost from player funds
        player["money"] -= toolShop[choice - 1]["cost"]
        # Put tool in tool bag
        player["toolBag"] += [toolShop[choice - 1]]
        # Remove tool from shop
        del toolShop[choice - 1]
        print(toolShop)
    else:
        print(
            f"\n😭 You are too broke!\nCome back when you have {toolShop[choice - 1]['cost'] - player['money']}\n")


# To mow or not to mow...
def dailyChoice():
    print(f"You have ${player['money']} to your name.")
    choice = input(
        f"What would you like to do today?\n\t1. Mow the lawn with your {player['toolBag'][0]['name']}\n\t2. Go to the tool shop\n\tQ. EXIT: ")
    # Mow the lawn
    if choice == "1":
        player["money"] += currentTool["profit"]
    elif choice == "2":
        goToShop()
    elif choice.lower() == "q":
        # put this into a function later
        print("Thanks for playing!")
        exit()
    # Validate
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
