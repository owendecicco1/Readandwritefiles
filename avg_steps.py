def main():
    import csv 

    infile = open("steps.csv","r")
    outfile = open("avg_steps","w")

    csvfile = csv.reader(infile,delimiter=",")

    