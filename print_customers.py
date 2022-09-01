def main():
    import csv

    infile = open("customers.csv","r")

    csvfile = csv.reader(infile, delimiter=",")

    next(csvfile)         #This will skip for row

    for record in csvfile:
        print("ID:",record[0])
        print("First Name:",record[1])
        print("Last Name:",record[2])
        print("City:",record[3])
        print("County:",record[4])
        print("Phone:",record[5])
        
        input("Press enter for next customer:")


main()