#! /usr/bin/env python3


def story(poopy):
    print(poopy)
    poop = ("the color brown")
    flush = ("removes the color brown")
    print(("I hate " + poop + " because it reminds me of poop."))
    print(("I like to flush it down because it " + flush + " for me. "))
    question = eval(input("Do you like to flush yourself?"))
    print(question)
    if(question == "yes"):
        print("Good, it's gross not to!")
    else:
        print("You're an idiot.")

story("Story Time!")





