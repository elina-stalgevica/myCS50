name = input("What's your name? ")

match name:
    # How to write if/or in one line
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # A case that is not being mentioned
    case _:
        print("Who?")
