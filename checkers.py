"""
Checkers program accompanying the online workshop by RoboTeam Twente.
This program was written by Luc Schoot Uiterkamp
"""
import os # dit is nodig om te checken of je windows, linux of mac gebruikt

def clearconsole():
    """
    Deze functie zorgt er voor dat het oude dambord wordt weggehaald elke keer als we een nieuwe tekenen
    """
    os.system('cls' if os.name=='nt' else 'clear')

class stones():
    """
    Dit is de class voor de stenen, waar we functies definieren die voor zowel de witte als de zwarte stenen van
    toepassing zijn
    """
    def __init__(self, poslist):
        # hier zeggen we dat de posities van de stenen de posities zijn die we vast hebben gesteld
        self.positions = poslist

    def updatePos(self, stone, newpos):
        """
        hier updaten we de posities van een steen
        eerst zoeken we in de lijst met posities (self.positions) waar de steen die we willen veranderen staat
        daarna slaan we de nieuwe positie op die index in de lijst op
        """
        self.positions[self.positions.index(stone)] = newpos

    def removeStone(self, hitpos):
        """
        hier wordt ook eerst opgezocht waar de steen die we willen verwijderen staat in de lijst
        vervolgens wordt deze uit de lijst verwijderd
        """
        self.positions.pop(self.positions.index(hitpos))

def inputToCoordinates(input):
    """
    hier wordt de input zoals a4 of b5 omgezet in coordinaten die we kunnen gebruiken in ons programma
    als dit niet lukt is er iets mis met de input, er is bijvoorbeeld een letter of een cijfer doorgegeven
    die niet op het bord staat
    """
    try:
        ycoord = "abcdefghij".index(input[0])
        xcoord = int(input[1:]) - 1
    except:
        print("Invoer onjuist, druk op enter om door te gaan.")
        return -1
    return [xcoord, ycoord] # xcoord en  ycoord zijn de x en y coordinaten



def checkMove(stonecoords,destcoords):
    """
    Hier moet gecontroleerd gaan worden of een zet geldig is. Aan de hand van de huidige plek van de steen (stonecoords)
    en de plek waar de steen naartoe verzet wordt moeten er drie dingen gecontroleerd gaan worden.
    Dit deel van het programma moet door jullie geprogrammeerd worden! Het doel is om de drie checks te implementeren.
    Als eerste moet gecontroleerd worden of er de plek waar de steen naartoe wordt bewogen in het veld ligt.
    Daarna moet gekeken worden of er op die plek niet al een steen staat.
    Als laatst moet er gekeken worden of de steen precies een rij en een kolom verzet wordt, anders is het geen geldige
    zet.
    Hier onder staat nu een stukje code dat zegt dat de code nog niet af is. Dit moet aangevuld worden tot de drie
    checks werken.
    Je kan aangeven dat een zet geldig is door True te returnen met het commando 'return True'
    Als een slag niet geldig is kun je dat aangeven door 'return False' te gebruiken
    Omdat de controle voor een geldige zet wel wat lijkt op de controle voor een geldige slag kun je hier onder kijken
    naar hoe de slag gecontroleerd wordt. Let er hierbij wel op dat er bij de slag controle een extra variabele wordt
    gebruikt die je hier niet hoeft te returnen. Mocht je er echt niet uit komen dan staat er helemaal onderaan een
    werkend stukje code. Deze kun je hier in plakken, dan werkt het.
    """

    if "not check 1" == True:
        return True
    elif "not check 2" == True:
        return True
    elif 'not check 3' == True:
        return True
    else:
        print("\n\nHet programma is nog niet af! Open de code om de slag controle af te maken.\n\n")
        return True

def checkHit(stonecoords,destcoords, side):
    """
    Hier checken we of een bepaalde zet een slag was
    Hierin gebruiken we bijna dezelfde checks als bij de check of het een goede zet was
    Eerst wordt gecontroleerd of het verschil in rijen en kolommen tussen de steen die verzet is en de plek waar de steen
    naartoe verzet is 2 is. Als dat zo is wordt de plek waar een geslagen steen zou moeten staan berekend (die wordt
    hitpos genoemd) en wordt er gekeken of er een steen van de andere kleur op die plek staat.
    """
    if not destcoords in white.positions or destcoords in black.positions:
        if (stonecoords[0] - destcoords[0] == -2) | (stonecoords[0] - destcoords[0] == 2) & (
                    stonecoords[1] - destcoords[1] == -2) | (stonecoords[1] - destcoords[1] == 2):
            hitpos = [int(stonecoords[0] - ((stonecoords[0] - destcoords[0]) / 2)),
                      int(stonecoords[1] - ((stonecoords[1] - destcoords[1]) / 2))]
            if side:
                if hitpos in white.positions:
                    return True, hitpos
                else:
                    return False, hitpos
            else:
                if hitpos in black.positions:
                    return True, hitpos
                else:
                    return False, None
        else:
            return False, None
    else:
        return False, None

def doTurn(side):
    """
    Hier verwerken we de zet. Het begint met zeggen tegen de gebruiker dat zwart of wit aan de beurt is en een vraag
    welke steen er verzet moet worden. Dan vraagt het programma waar de steen heen moet.
    Als er een slag of een zet is gemaakt in deze beurt worden de posities van de betrokken stenen geüpdate.
    Als dit niet gelukt is moet de gebruiker opnieuw aangeven welke steen er verzet moet worden en waarheen.
    """
    movestone = input("{} is aan de beurt. Geef steen om te zetten aan:".format("wit" if side == 0 else "zwart"))
    destination = input("{} is aan de beurt. Geef aan waar steen {} heen moet:".format("wit" if side == 0 else "zwart", movestone))
    stonecoords = inputToCoordinates("{}".format(movestone))
    destcoords = inputToCoordinates("{}".format(destination))
    isHit, hitpos = checkHit(stonecoords, destcoords, side)
    if isHit:
        if side:
            black.updatePos(stonecoords, destcoords)
            white.removeStone(hitpos)
        else:
            white.updatePos(stonecoords, destcoords)
            black.removeStone(hitpos)
    elif checkMove(stonecoords,destcoords):
        if side:
            black.updatePos(stonecoords, destcoords)
        else:
            white.updatePos(stonecoords, destcoords)
    else:
        input("Invoer ongeldig, druk op enter om door te gaan.")
        doTurn(side)


def drawfield(posWhite, posBlack):
    """
    Als eerst bij elke beurt wordt het veld getekend. Eerst wordt het vorige veld verwijderd, dan wordt er een nieuw
    leeg veld gemaakt en worden de posities van zowel de witte als de zwarte stenen ingevuld
    """
    clearconsole()
    field = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
             ]
    for stone in posWhite:
        field[stone[0]][stone[1]] = chr(9711)
    for stone in posBlack:
        field[stone[0]][stone[1]] = chr(9673)
    """
    Vanaf hier volgen een aantal gekke print statements. Hier wordt het veld daadwerkelijk getekend.
    Alles wat begint met u" is een teken, bijvoorbeeld een streepje van het veld of een rondje van een damsteen
    """
    print(u"\u2501" * 23)
    i=0
    for row in field:
        i+=1
        if i<10:
            j= "0{}".format(i)
        else:
            j=str(i)
        print(j+"\u2502"+"\u2502".join(row)+"\u2502")
    print(u"\u2501"*23+'\n'+"   A B C D E F G H I J")

def gamewon():
    """
    Hier wordt gekeken of een van de twee partijen gewonnen heeft door te kijken of de ander nog stenen heeft
    """
    if not white.positions:
        print("Black has won!")
        return True
    if not black.positions:
        print("White has won!")
        return True
    return False


if __name__ == "__main__":
    """
    Hier beginnen we het spel. Het 'if __name__ == "__main__":' gedeelde dat hier staat betekent dat het programma hier 
    begint als het geopend wordt. 
    We maken eerst een variabele side om aan te geven welke kant aan de beurt is. Gedurende het spel is deze 0 als wit
    aan de beurt is en 1 als zwart aan de beurt is. 
    We definieren hierna de startcoordinaten voor de beide sets stenen
    Dan zeggen we voor zowel de witte als zwarte stenen dat ze bij de class 'stones' horen
    Als laatst beginnen we het spel totdat een van de kanten gewonnen heeft
    Het spel bestaat telkens uit het tekenen van het veld en het doen van een zet daarna is de andere kant aan de beurt
    """
    side = 0
    posWhite = [[0, 1], [0, 3], [0, 5], [0, 7], [0, 9],
                [1, 0], [1, 2], [1, 4], [1, 6], [1, 8],
                [2, 1], [2, 3], [2, 5], [2, 7], [2, 9],
                [3, 0], [3, 2], [3, 4], [3, 6], [3, 8]
                ]
    white = stones(posWhite)
    posBlack = [[6, 1], [6, 3], [6, 5], [6, 7], [6, 9],
                [7, 0], [7, 2], [7, 4], [7, 6], [7, 8],
                [8, 1], [8, 3], [8, 5], [8, 7], [8, 9],
                [9, 0], [9, 2], [9, 4], [9, 6], [9, 8]
                ]
    black = stones(posBlack)
    while not gamewon():
        drawfield(white.positions, black.positions)
        doTurn(side)
        side = not side


"""
Hieronder staat werkende code voor de slag check, voor als je er niet uit komt. 


    if destcoords in white.positions or destcoords in black.positions:
        return False
    elif destcoords[0] < 0 | destcoords[0] > 10 | destcoords[1] < 0 | destcoords[1] > 10:
        return False
    elif not (stonecoords[0]-destcoords[0]==-1) | (stonecoords[0]-destcoords[0]==1) & (
            stonecoords[1]-destcoords[1]==-1) | (stonecoords[1]-destcoords[1]==1):
        return False
    else:
        return True


"""


