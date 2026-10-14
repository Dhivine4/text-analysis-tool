from random_username.generate import generate_username

# welcome user 
def welcomeUser () :
    print("Welcome to my text analyis tool. I will mine and analyse a body of text from a file you give me")

#  get username
def getUserName (): 
    #  get imput from user into the terminal 
    nameFromInput = input("\nTo begin, please enter your username:\n")
    # \n prints a new line in command line 

    # check if userName is valid and meeets criteria;
    # 1. not less than 5 characters 
    # 2. doenst start with a number and contains no spaces 
    # 3. can incluse alphabets numbers and underscore
    if len(nameFromInput) > 4 and nameFromInput.isidentifier():
        # identifier() is used to validate a string input on specific terms
        return nameFromInput
    else:
        print("your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9/_), have no space, and cannot start with a number")
        nameFromInput = generate_username()[0]
        print("assigning new username: " + nameFromInput)
        return nameFromInput

# print welcome message 
def welcomeMessage (name) :
    print("hello, ", name)

welcomeUser()
userName = getUserName()
welcomeMessage(userName)

