def main ():
    import csv

    infile = open("EmployeePay.csv","r")

    csvfile = csv.reader(infile, delimiter=",")
    infile.readline()

    for record in csvfile:

        Salary = int(record[3])
        Bonus = float(record[4])
        Total_Pay= Salary + (Salary*Bonus)
        print("ID:",record[0])
        print("First Name:",record[1])
        print("Last Name:",record[2])
        print("Salary: $",format(Salary, ",.2f"),sep="")
        print("Bonus:",record[4])
        print("Total Pay: $",format(Total_Pay, ",.2f"),sep="")
        
        input("Press enter for next customer:")


main()