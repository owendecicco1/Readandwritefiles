def main():
    import csv 

    infile = open("steps.csv","r")
    outfile = open("avg_steps.csv","w")
    csvfile = csv.reader(infile,delimiter=",")

    next(csvfile)
    months = ['Void', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = 1
    steps = 0
    days = 0
    for record in csvfile:

        if record[0] == str(month):
            steps += int(record[1])
            days += 1

        else:
            average_steps = format(steps/days, '.2f')
            outfile.write(months[int(month)] + ', ' + str(average_steps) + '\n')
            month = record[0]
            steps = int(record[1])
            days = 1
    
    average_steps = format(steps/days, '.2f')
    outfile.write(months[int(month)] + ', ' + str(average_steps) + '\n')
    month = record[0]
    steps = int(record[1])
    days = 1

    
    outfile.close()

main()


