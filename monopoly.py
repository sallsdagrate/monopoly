import random
import csv
import xlsxwriter
import pandas as pd

count = [0] * 40
# print(count)

# dice = [x + 1 for x in range(6)]
# print(dice)

position = 0


def chance():
    global position

    shuffle = random.randint(1, 16)
    if shuffle == 1:
        # Advance to GO
        position = 0
    elif shuffle == 2:
        # Advance to Trafalgar Square
        position = 24
    elif shuffle == 3:
        # Advance to Pall Mall
        position = 11
    elif shuffle == 4:
        # Advance to nearest utility
        if position <= 28 and position > 12:
            position = 28
        else:
            position = 12
    elif shuffle == 5:
        # Advance to nearest railway station
        if position > 35 or position <= 5:
            position = 5
        elif position > 5 and position <= 15:
            position = 15
        elif position > 15 and position <= 25:
            position = 25
        elif position > 25 and position <= 35:
            position = 35
    elif shuffle == 8:
        # Move 3 places back
        position = position - 3
    elif shuffle == 9:
        # Go to Jail
        position = 10
    elif shuffle == 12:
        position = 5
    elif shuffle == 13:
        position = 39


def communityChest():
    global position

    shuffle = random.randint(1, 16)
    if shuffle == 1:
        # Advance to GO
        position = 0
    elif shuffle == 2:
        # Go back to Old Kent Road
        position = 1
    elif shuffle == 3:
        # Go straight to Jail
        position = 10


def roll():
    global position

# roll both dice
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    total = roll1 + roll2
    position = (position + total) % 40

    if roll1 == roll2:
        roll()

    return


def updateCount():
    global position
    count[position] = count[position] + 1


def main():
    global position
    updateCount()
    for x in range(1000000):
        roll()
        updateCount()

        if position == 30:
            position = 10
            updateCount()
        elif position in [7, 22, 36]:
            chance()
            updateCount()
        elif position in [2, 17, 33]:
            communityChest()
            updateCount()

    print(count)

    df = pd.DataFrame.from_dict({'Results': count})
    df.to_excel('monopoly2.xlsx', header=True, index=(0, 1), index_label=False)


main()
