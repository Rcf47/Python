import csv

with open("phonebook.csv", "a") as file: #auto close when code is ended

    name = input("Name: ")
    number = input("Number: ")

    writer = csv.writer(file)
    writer.writerow([name, number])
