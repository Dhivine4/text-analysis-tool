from random_username.generate import generate_username

# welcome user 
def welcomeUser () :
    print("Welcome to my text analyis tool. I will mine and analyse a body of text from a file you give me")

#  get username

def getUserName():
    # Maximum attempts before assigning a random username
    attempts = 0
    maximumAttempts = 3

    while attempts < maximumAttempts:
        inputPrompt = ""
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your username: "
        else:
            inputPrompt = "\ntry again: "
        nameFromInput = input(inputPrompt)

        # validate username
        if len(nameFromInput) > 4 and nameFromInput.isidentifier():
            return nameFromInput

        else:
            print(
                "Your username must be at least 5 characters long, "
                "alphanumeric only (a-z/A-Z/0-9/_), have no space, "
                "and cannot start with a number"
            )

            attempts += 1

    # Assign a random username after 3 failed attempts
    nameFromInput = generate_username()[0]
    print("you have exhausted " + str(attempts) + " attempts at creating a username so, \nAssigning new username: " + nameFromInput)

    return nameFromInput

# print welcome message 
def welcomeMessage (name) :
    print("hello, ", name)

welcomeUser()
userName = getUserName()
welcomeMessage(userName)

