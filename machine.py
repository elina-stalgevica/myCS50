emoticon = "v.v"

def main():
    # Make variable global,so you can change emotion and use it
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    # Print phrase with emotion
    print(phrase + " " + emoticon)


main()
