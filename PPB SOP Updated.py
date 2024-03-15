# Creating values
try:
    GivQ = "Give quantity (qty) for "
    GivP = "Give price ($) for "
    Press = "Input value and press enter..."
    print(Press)
    MfgDate = input("Give Manufacturing date in DD/MM/YYYY: ")
    ExpDate = input("Give Expiry date in DD/MM/YYYY: ")
    Actual = float(input(GivQ + "'No Flavor Add 250g': "))
    CaSO4 = float(input(GivQ + "'Calcium Sulphate': "))
    PackMat = float(input(GivQ + "'Packaging Material': "))
    Carton = float(input(GivP + "'Ctn Box Charges': "))
    Labour = float(input(GivP + "'Laborer charge': "))
    Deliv = float(input(GivP + "'Delivery charge': "))
    Cool = float(input(GivP + "'Cool room Storage charge': "))
except:
    print("Not a valid number. Rerun the program and insert a valid number")

def round_to_multiple(number, multiple):
    """
    This function rounds an integer to the nearest multiple
    :param number: integer
            Unrounded number
    :param multiple: integer
            Multiple of the number to be rounded to
    :return: rounded_num: integer
            Rounded number to nearest multiple of multiple
    """
    rounded_num = multiple * round(number/multiple)
    return rounded_num

def getBatchName():
    """This function gets the Batch Name from manufacturing date"""
    BatchNameLst = ExpDate.split("/")
    BatchName = "".join(BatchNameLst)
    return BatchName

def getBatchSize():
    """This function gets the Batch Size"""
    BatchSize = round_to_multiple(Actual, 166)
    return BatchSize

def getUnderweights():
    """This function gets the number of Underweights"""
    Underweights = PackMat - Actual
    return Underweights

def getMiscPrice():
    """This function gets the total of the Miscellaneous price"""
    Misc = CaSO4 * 1.30 + Carton + Labour + Deliv + Cool
    return "$" + str(Misc)

def getDiscrepancies():
    """This function prints the number of extra or deficient blocks"""
    disc = getBatchSize() - Actual
    if disc > 0:
        return str(disc), "Extra blocks, Use Source (Consumption)"
    if disc < 0:
        return str(disc), "Deficient blocks, Use Destination (Production)"
    if disc == 0:
        return str(disc) + " No extra blocks"

def main():
    # Printing values
    print("\n----------\nInput these details:\n")
    print("Name of product: HerbYvore Plant Protein Block")
    print("Name of BOM: Plant Protein Block")
    print("Godown: Fluetis 3PL")
    print("Qty:", str(getBatchSize()))
    print("Batch name:", getBatchName())
    print("Mfg date:", MfgDate)
    print("Expiry date:", ExpDate)

    # Instruction to input BOM quantity
    print("\n")
    print("Input quantity of items as stated in 'Quantity as per BOM'\n")

    # Co-Product
    print("Co-product:")
    print("'HerbYvore Plant Protein Block - UW:'", str(getUnderweights()), "\n")

    # Additional Cost
    print("Additional Cost:")
    print("'Miscellaneous:'", str(getMiscPrice()),"\n")

    # Additional steps
    print("Additional Steps:")
    print(getDiscrepancies())

if __name__ == "__main__":
    main()
