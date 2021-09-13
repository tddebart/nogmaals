dagen = "ma", "di", "wo", "vr", "za", "zo"
keuze = input("Welke dag van de week?{} ".format(dagen))
i= 0
while i < dagen.index(keuze)+1:
    print(dagen[i])
    i+=1