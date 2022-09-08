def main():
    import csv 

    infile = open("steps.csv","r")
    outfile = open("avg_steps","w")

    csvfile = csv.reader(infile,delimiter=",")
    infile.readline()

    new_list = []
    month = 1
    for record in csv_file: