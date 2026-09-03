import random

Bob = {
    "name": "Bob",
    "age": 1,
    "iq": 10
}

def checkForResponse(responseList, userInput, category):
    for checkInput in responseList["triggers"]:
        if len(checkInput.split()) == 1:
            if checkInput in userInput.lower().split():
                print(random.choice(responseList["responses"]))
                return True
        else:
            if checkInput in userInput.lower():
                if category == "name":
                    print(f"My name is {Bob[responseList['bobName']]}!")
                    return True
                else:
                    print(random.choice(responseList["responses"]))
                    return True

    return False

responseTypes = {
    "greetings": {
        "triggers": ["hello", "hi", "good morning", "good afternoon"],
        "responses": ["Hey there!", "Hello!", "Good morning!", "Hi!"]
    },
    "farewells": {
        "triggers": ["bye", "cya", "goodbye", "later"],
        "responses": ["Goodbye!", "See you later!", "Bye!", "See ya!"]
    },
    "name": {
        "triggers": ["what is your name",
                     "what's your name",
                     "can i get your name"],
        "bobName": "name"
    }
}

print("This is Bob")
print()

while True:
    userInput = input("What would you like to say to Bob? ")

    for category in responseTypes:
        if checkForResponse(responseTypes[category], userInput, category):
            break
    else:
        print("I don't understand.")
    
    
