antwoord = ""
keerfout = 1
while antwoord != "quit":
    print("Dit is je {}st attempt".format(keerfout))
    antwoord = input("Wat is het woord ")
    keerfout +=1