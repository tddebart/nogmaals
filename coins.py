# name of student: Thomas
# number of student:
# purpose of program: Wisselgeld berekenen
# structure of program: 

toPay = int(float(input('Amount to pay: ')) * 100) # vraag hoeveel het kost
payed = int(float(input('Payed amount: ')) * 100) # vraag hoeveel je betaalt hebt
change = payed - toPay
betaalt = []

if change > 0: # kijk if er wat terugbetaalt moet worden
    coinValue = 500 # zet de eerste munt waar die voor vraagt

    while change > 0 and coinValue > 0: # blijf muntjes vragen zolang niet alles is betaalt
        nrCoins = change // coinValue # doe een floor division

        if nrCoins > 0:
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!') # print hoeveel ze van deze munt moeten terugbetalen
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? ')) # vraag hoeveel je er wil terugbetalen
            change -= nrCoinsReturned * coinValue # bereken hoeveel er nu betaalt moet worden

            betaalt.append("Je hebt {} muntjes van {} betaald".format(nrCoinsReturned, coinValue))

        # comment on code below:
        if coinValue == 500:
            coinValue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

if change > 0:  # als de change hoger is dan null zeg hoeveel er terug moet betaalt worden
    print('Change not returned: ', str(change) + ' cents')
else:
    print('done')
    for x in betaalt:
      print(x)
