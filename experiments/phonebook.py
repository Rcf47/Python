import csv

with open("phonebook.csv", "a") as file: #auto close when code is ended

    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name":name, "number":number})
