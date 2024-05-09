import csv

with open('insurance.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    counter_of_rows = 0
    for row in csv_reader:
        counter_of_rows += 1
    print("In our database there are " + str(counter_of_rows) + " patients who have insurance.")
    csvfile.seek(0)

    print('\n')

    for row in csv_reader:
        print(row)
        break

    csv_reader = csv.reader(csvfile)

    # Counting an average age of patient  c;
    def average_age(csvreader):

        list_of_age = []
        for row in csvreader:
            list_of_age.append(row[0])
        list_of_age.pop(0)

        counter_of_age = 0
        for age in list_of_age:
            counter_of_age += int(age)

        average_full = counter_of_age / len(list_of_age)
        average = round(average_full, 2)


        print('\nThe average age of insurance patient is ' + str(average) + ' years old.')

    average_age(csv_reader)
    csvfile.seek(0)

    print()

    def average_costs(csvreader):
        list_of_costs = []
        for row in csvreader:
            list_of_costs.append(row[0])

        print(list_of_costs)

    average_costs(csv_reader)
