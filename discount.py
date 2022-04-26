
def discountBook(oldPrice):

    #Calculate a new Price 11 - 0.9 = 10.1    100 = 10 + 100 - 9
    newPrice = ((oldPrice * 0.1) + oldPrice) - (0.09 * oldPrice)
    return newPrice

