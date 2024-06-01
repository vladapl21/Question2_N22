class Card:

    #PRIVATE Number : INTEGER
    #PRIVATE Colour : STRING

    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
Card1 = Card(1, "red")
Card2 = Card(2, "red")
Card3 = Card(3, "red")
Card4 = Card(4, "red")
Card5 = Card(5, "red")
Card6 = Card(1, "blue")
Card7 = Card(2, "blue")
Card8 = Card(3, "blue")
Card9 = Card(4, "blue")
Card10 = Card(5, "blue")
Card11 = Card(1, "yellow")
Card12 = Card(2, "yellow")
Card13 = Card(3, "yellow")
Card14 = Card(4, "yellow")
Card15 = Card(5, "yellow")


class Hand:

    #PRIVATE Cards : ARRAY[0:9] OF Card
    #PRIVATE FirstCard : INTEGER
    #PRIVATE NumberCards : INTEGER
    Cards = []
    FirstCard = 0
    NumberCards = 5

    def __init__(self, Cards, Card1, Card2, Card3, Card4, Card5, FirstCard, NumberCards):
        self.__Cards = Cards
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = FirstCard
        self.__NumberCards = NumberCards

    def GetCard(self, index):
        return self.__Cards[index]
    
Player1 = Hand([], Card(1, "red"), Card(2, "red"), Card(3, "red"), Card(4, "red"), Card(1, "yellow"), 0, 5)
Player2 = Hand([], Card(2, "yellow"), Card(3, "yellow"), Card(4, "yellow"), Card(5, "yellow"), Card(1, "blue"), 0, 5)

def CalculateValue(Hand):
    points = 0
    for i in range(5):
        Card = Hand.GetCard(i)
        if Card.GetColour() == "red":
            points += 5
        elif Card.GetColour() == "blue":
            points += 10
        elif Card.GetColour() == "yellow":
            points += 15  
        points += Card.GetNumber()
        return points

if CalculateValue(Player1) > CalculateValue(Player2):
    print("Player 1 wins")
elif CalculateValue(Player2) > CalculateValue(Player1):
    print("Player 2 wins")
else:
    print("It is a draw")
