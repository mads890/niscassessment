def playbingo(called, data):
    # called = [[column, num], [column, num], [column, num], etc]
    # data = [[[card 1 row 1 data], [card 1 row 2 data], [card 1 row 3 data], [card 1 row 4 data], [card 1 row 5 data]], [[card 2 row 1 data], [card 2 row 2 data], [card 2 row 3 data], [card 2 row 4 data], [card 2 row 5 data]]]
    # update card data with -1 when num is called
    winners = []
    for call in called:
        # two cards can win on the same call - check ALL cards for each new call
        # call = [column, num]
        for card in enumerate(data):
            # enumerate to get idx of card for return winner(s)
            # card[1] = [[row 1 data], [row 2 data], [row 3 data], [row 4 data], [row 5 data]]
            for row in card[1]:
                # call[0] = idx of column
                # call[1] = number called
                if row[call[0]] == call[1]:
                    row[call[0]] = -1
                # sets can't have duplicates - if len(set(row)) == 1 then all numbers in that row are the same
                # if row[0] == -1 and all nums in the row are the same then all nums in this row have been called (card is a winner)
                if len(set(row)) == 1 and row[0] == -1:
                    # card[0] = idx of card
                    winners.append(card[0])
                    # no need to check other rows, card is already a winner
                    break
            if card[0] in winners:
                # no need to check columns or diagnoals, card is already a winner
                continue
            if checkcolumns(card[1]):
                winners.append(card[0])
                continue
            if checkdiagonals(card[1]):
                winners.append(card[0])
        # all cards have been checked for this call
        if len(winners) != 0:
            # if winners, do not call the next number
            return winners
        # if no winners, call the next number
       

def checkcolumns(card):
    # card = [[row 1], [row 2], [row 3], [row 4], [row 5]]
    cols = []
    for i in range(5):
        # get nums at idx i in each row
        cols.append([x[i] for x in card])
    for col in cols:
        if len(set(col)) == 1 and col[0] == -1:
            return True
    return False

def checkdiagonals(card):
    # card = [[row 1], [row 2], [row 3], [row 4], [row 5]]
    diagbottom = []
    diagtop = []
    for i in range(5):
        # diag from top left to bottom right column idx same as row idx
        diagtop.append(card[i][i])
        # diag from bottom left to top right column idx inverse of row idx + 1
        diagbottom.append(card[i][-(i + 1)])
    diags = [diagbottom, diagtop]
    for diag in diags:
        if len(set(diag)) == 1 and diag[0] == -1:
            return True
    return False