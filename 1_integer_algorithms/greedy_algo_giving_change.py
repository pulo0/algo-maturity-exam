# Time complexity: O(n)
def change(amount: int):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    index = 0
    # if amount is greater than 0
    # so it goes until there will be no value to look into
    while amount > 0:
        # if the amount is greater or equal to first denomination and if the amount doesn't match the for example 500
        # then it goes to 200 and 100, 50, 20 and so on
        # until the amount will be zero
        if amount >= denominations[index]:
            # prints out the amount of denominations it can be in this value and the denomination itself
            print(f'{amount//denominations[index]}x{denominations[index]} ')
            # and then modulo to receive what is left to check
            amount %= denominations[index]
        # if the denomination doesn't fit to amount then index goes to another
        index += 1

amount_of_money = int(input('Enter the amount of money you have (integer values): '))
change(amount_of_money)