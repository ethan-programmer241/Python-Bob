import random

Bob = {
    "name": "Bob",
    "age": 10,
    "iq": 10
}

userInfo = {
    "name": "",
}

def rememberUserInfo(userInput):
    for nameTriggers in userInput.lower():
        for index, word in enumerate(userInput.lower().split()):
            if word == "is":
                break
        name  = userInput.lower().split()[index + 1:]
        userInfo["name"] = " ".join(name)

def checkForResponse(responseList, userInput):
    for checkInput in responseList["triggers"]:
        if len(checkInput.split()) == 1:
            if checkInput in userInput.lower().split():
                print(random.choice(responseList["responses"]))
                return True
        else:
            if checkInput in userInput.lower():
                if "data" in responseList:
                    print(responseList['response'].format(data=Bob[responseList["data"]]))
                    return True
                else:
                    print(random.choice(responseList["responses"]))
                    return True
    return False

nameTriggers = [
    "my name is"
]

responseTypes = {
    "greetings": {
        "triggers": ["hello", "hi", "good morning", "good afternoon"],
        "responses": ["Hey there!", "Hello!", "Howdy!", "Hi!"]
    },
    "farewells": {
        "triggers": ["bye", "cya", "goodbye", "later"],
        "responses": ["Goodbye!", "See you later!", "Bye!", "See ya!"]
    },
    "name": {
        "triggers": ["what is your name",
                     "what's your name",
                     "can i get your name"],
        "response": "My name is {data}!",
        "data": "name"
    },
    "age": {
        "triggers": ["how old are you",
                     "what is your age"],
        "response": "I am {data} years old!",
        "data": "age"
    },
    "iq": {
        "triggers": ["how smart are you",
                     "what is your iq"],
        "response": "I have {data} IQ!",
        "data": "iq"
    }
}

print("This is Bob")
print()

while True:
    userInput = input("What would you like to say? ")

    rememberUserInfo(userInput)

    for category in responseTypes:
        if checkForResponse(responseTypes[category], userInput):
            break
    else:
        print("I don't understand.")

    print(userInfo["name"])
