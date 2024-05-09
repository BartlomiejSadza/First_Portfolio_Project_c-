import csv

with open('insurance.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        print(row)
        break
    print('\n')

    counter_of_rows = 0
    for row in csv_reader:
        counter_of_rows += 1
    print("In our database there are " + str(counter_of_rows) + " patients who have insurance.")
    csvfile.seek(0)

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

    # Counting an average costs for individual (:
    def average_costs(csvreader):
        list_of_costs = []
        for row in csvreader:
            list_of_costs.append(row[-1])
        list_of_costs.pop(0)

        count_cost = 0
        for cost in list_of_costs:
            count_cost += float(cost)

        avg_cost = count_cost / len(list_of_costs)
        print('The average cost for person carry out: ' + str(round(avg_cost, 2)) + ' dollars.')

    average_costs(csv_reader)