class Card:
    def __init__(self, rows, idx):
        self.cardindex = idx
        
        # rows and columns
        self.rows = []
        self.columns = []
        rowtoadd = set()
        coltoadd = set()
        for i in range(5):
            rowtoadd.update(tuple((rows[i].index(item), item) for item in rows[i]))
            self.rows.append(rowtoadd)
            rowtoadd = set()
            coltoadd.update(tuple((i, row[i]) for row in rows))
            self.columns.append(coltoadd)
            coltoadd = set()
        
        # diagonals
        diagtop = set()
        diagbottom = set()
        for i in range(5):
            diagtop.add((i, rows[i][i]))
            diagbottom.add((i, rows[4 - i][i]))
        self.diagonals = [diagtop, diagbottom]

    def iswinner(self, called):
        for row in self.rows:
            remainder = row - called
            if len(remainder) == 0:
                return True
        for column in self.columns:
            remainder = column - called
            if len(remainder) == 0:
                return True
        for diagonal in self.diagonals:
            remainder = diagonal - called
            if len(remainder) == 0:
                return True
        return False

def playbingo(called, cards):
    winners = []
    calledset = {(2, -1)} # free space
    cardobjects = [Card(card, cards.index(card)) for card in cards]
    for call in called:
        calledset.add(tuple(call))
        if len(calledset) < 5:
            continue
        for cardobj in cardobjects:
            if cardobj.iswinner(calledset):
                winners.append(cardobj.cardindex)
        if len(winners) != 0:
            return winners

cards = [
    [
        [1, 11, 21, 31, 41],
        [2, 12, 22, 32, 42],
        [3, 13, -1, 33, 43],
        [4, 14, 24, 34, 44],
        [5, 15, 25, 35, 45]
    ],
    [
        [6, 16, 26, 36, 41],
        [7, 17, 27, 37, 47],
        [8, 18, -1, 38, 48],
        [9, 19, 29, 39, 49],
        [10, 20, 30, 40, 50]
    ],
]

horizontalrowwin = [
    [0, 1],
    [1, 11],
    [2, 21],
    [3, 31],
    [4, 41]
]

verticalcolumnwin = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5]
]

diagonalwin = [
    [0, 1],
    [1, 12],
    [2, 23],
    [3, 34],
    [4, 45]
]

twowinners = [
    [0, 1],
    [0, 6],
    [1, 11],
    [1, 16],
    [2, 21],
    [2, 26],
    [3, 31],
    [3, 36],
    [4, 41]
]

cardtwowinhorizontal = [
    [0, 6],
    [1, 16],
    [2, 26],
    [3,36],
    [4, 41]
]

cardtwowinvertical = [
    [0, 6],
    [0, 7],
    [0, 8],
    [0, 9],
    [0, 10]
]

cardtwowindiagonal = [
    [0, 10],
    [1, 19],
    [2, 26],
    [3, 37],
    [4, 41]
]

nowinner = [
    [0, 7],
    [1, 18],
    [2, 22], 
    [3, 34],
    [4, 45]
]

print('card one wins horizontally', playbingo(horizontalrowwin, cards))
print('card one wins vertically', playbingo(verticalcolumnwin, cards))
print('card one wins diagonally', playbingo(diagonalwin, cards))
print('both cards win', playbingo(twowinners, cards))
print('card two wins horizontally', playbingo(cardtwowinhorizontal, cards))
print('card two wins vertically', playbingo(cardtwowinvertical, cards))
print('card two wins diagonally', playbingo(cardtwowindiagonal, cards))
print('no winner', playbingo(nowinner, cards))