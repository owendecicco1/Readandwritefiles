def main ():
    import csv

    infile = open("EmployeePay.csv","r")

    csvfile = csv.reader(infile, delimiter=",")

    next(csvfile)         #This will skip for row


    for record in csvfile:

        Salary = int(record[3])
        Bonus = float(record[4])
        Total_Pay= Salary + (Salary*Bonus)
        print("ID:",record[0])
        print("First Name:",record[1])
        print("Last Name:",record[2])
        print("Salary: $",format(Salary, ",2f"),record[3])
        print("Bonus:",record[4])
        print("Total Pay: $",Total_Pay, sep="")
        
        input("Press enter for next customer:")


main()