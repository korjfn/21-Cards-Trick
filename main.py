import random
# Generate a deck of 21 unique numbers
deck = random.sample(range(10,100),21)
def showCards(Cards):
    print("\n Here Are The Cards In Three Columns: \n")
    columns = [[],[],[]]
    for i, card in enumerate(Cards):
        columns[i%3].append(card)
    for i in range(7):
        print(f"{columns[0][i]:<5} {columns[1][i]:<5} {columns[2][i]:<5}")
    return columns


def rearrangeCards(columns,chosencolumn):
    # Always place the chosen column in the middle
    if chosencolumn == 0:
        neworder = columns[1] + columns[0] + columns[2]
    elif chosencolumn == 1:
        neworder = columns[0] + columns[1] + columns[2]
    else:
        neworder = columns[0] + columns[2] + columns[1]
    return neworder


cards = deck.copy()
for roundnum in range(3):
    columns = showCards(cards)
    while True:
        try:
            chosen = int(input("\nWhich column is your card in? (0, 1, or 2): "))
            if chosen in [0,1,2]:
                break
            else:
                print("please choose 0,1,2")
        except ValueError:
            print("Enter A Valid Number")
    cards = rearrangeCards(columns,chosen)


print("\n Your Card Is...")
print(f"{cards[10]}")