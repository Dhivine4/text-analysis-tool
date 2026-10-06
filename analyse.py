# welcome user 
def welcomeUser () :
    print("Welcome to my text analyis tool. I will mine and analyse a body of text from a file you give me")

#  get username
def getUserName (): 
    #  get imput from user into the terminal 
    nameFromInput = input("\nTo begin, please enter your username:\n")
    # \n prints a new line in command line 
    return nameFromInput

# print welcome message 
def welcomeMessage (name) :
    print("hello, ", name)

welcomeUser()
userName = getUserName()
welcomeMessage(userName)

