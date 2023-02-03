import anawedding.responses as responses 

greeting = input("What is your name: ")
new_greeting = greeting + ","

print(" \n" +\
    "Hey", new_greeting.capitalize(),"Thanks for dropping in. \n" +\
        " \n" +\
        "You're invited to Ana and Jacobie's Wedding!")

if __name__ == '__main__':
    responses.get_responses()