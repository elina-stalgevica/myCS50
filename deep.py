def main():
    acceptable_answers = {'42', 'forty two', 'forty-two'}
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if question in acceptable_answers:
        print("Yes")
    else:
        print("No")

main()
