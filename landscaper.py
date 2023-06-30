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


def swapTools():
    # Access variable outside this scope
    global currentTool
    print("\n~~~~~~~~~~~TOOLBAG~~~~~~~~~~~~~~~")
    # Loop through toolbag
    for i in range(len(player["toolBag"])):
        print(
            f"{i + 1}. {player['toolBag'][i]['name']} - Profit ${player['toolBag'][i]['profit']}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Change choce from string to int
    choice = int(input("\nPick a tool from your kit: "))
    # Swap the current tool with the players choice
    currentTool = player['toolBag'][choice - 1]


def goToShop():
    # Access variable outside this scope
    global currentTool
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
    print("0. EXIT SHOP")
    # Convert choice to an int so you can target list elements
    choice = int(input("\nWhat would you like to purchase?: "))

    # Check for funds
    # If they are suffucient
    if toolShop[choice - 1]["cost"] <= player["money"]:
        # Subtract cost from player funds
        player["money"] -= toolShop[choice - 1]["cost"]
        # Put tool in tool bag
        player["toolBag"] += [toolShop[choice - 1]]
        # Update Current tool
        currentTool = toolShop[choice - 1]
        # Remove tool from shop
        del toolShop[choice - 1]
    # Exit the shop
    elif choice == 0:
        dailyChoice()
    # If they do not have enough money
    else:
        print(
            f"\n😭 You are too broke!\nCome back when you have {toolShop[choice - 1]['cost'] - player['money']}\n")


# To mow or not to mow...
def dailyChoice():
    print(f"\nYou have ${player['money']} to your name.")
    choice = input(
        f"What would you like to do today?\n\t1. Mow the lawn with your {currentTool['name']}\n\t2. Go to the tool shop\n\tQ. EXIT: ")
    # Mow the lawn
    if choice == "1":
        player["money"] += currentTool["profit"]
    elif choice == "2":
        goToShop()
    elif choice == "3":
        swapTools()
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

while player["money"] <= 1000:
    dailyChoice()
