# imports necessary modules for my code
import os, csv

# sets up a path to the data file
budget_date = os.path.join('python-challenge','PyBank', 'Resources', 'budget_data.csv')

# declared variables for future use
months = []
profit_loss = []
greatest_values_list = []
net_total = 0
first_profit_loss = 0
last_profit_loss = 0
average_change_total = 0
greatest_increase_profit = 0
greatest_decrease_profit = 0
# used the following variables and list in my second For loop to come up with the change between each of the months.
first_val= 0
second_val= 0
change_profit_loss = 0
change_list = []

# Set up a loop that will run through every row and column in my csv file
with open(budget_date) as csvfile:

    # sets up the .csv file data into an array to be manipulated later
    csvreader = csv.reader(csvfile, delimiter=',')

    # skips the header in the .csv file so my code can focus on the data instead
    header = next(csvreader)

    budget_date_list = csvreader

    # loop that will run through my csv file and create new lists for months, profit_loss.  Also a nifty way to sum my total ;3
    for row in budget_date_list:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        net_total += int(row[1])
        greatest_values_list.append(row)

    #The following utilizes the max and min function to pull the maximum and minimum value from the list greatest_values_list.  It does this by taking the second column int(x[1]) making it the key value for the max/min function to search through the greatest_values_list.  The lambda variable just takes whatever value is in the x of the list and makes it the 'key' :3
    greatest_increase_profit = max(greatest_values_list, key = lambda x: int(x[1]))
    greatest_decrease_profit = min(greatest_values_list, key = lambda x: int(x[1]))

    # create a loop that will specifically call the first value, and the second value and take the difference between and add that value to another list called change_list.  The zip() function enables me to take the same list profit_loss twice and then combine them together.  I then took the difference, and added that new value to another list.
    for first_val, second_val in zip(profit_loss[0::], profit_loss[1::]):
        change_list.append(second_val - first_val)

    # convert months varaible to tally up the months after the loop so its populated
    months_len = len(months)

    #Adds up all the values in the change_list to get the change in profit loss
    change_profit_loss = sum(change_list)

    #calculates the average and then applies a round() function to two decimals
    average_change_total = round((change_profit_loss / (months_len - 1)), 2)

print(f"Financial Analysis\n---------------------------------------------------------")
print(f"Total Months: {months_len}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change_total}")
print(f"Greatest Increase in Profits: {greatest_increase_profit[0]} $({greatest_increase_profit[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease_profit[0]} $({greatest_decrease_profit[1]})")

output_file = os.path.join('python-challenge', 'PyBank', 'analysis', 'PyBank')
with open("PyBank_final.txt", "w") as text:
    text.write("Financial Analysis\n")
    text.write("---------------------------------------------------------\n")
    text.write(f"Total Months: {months_len}\n")
    text.write(f"Total: ${net_total}\n"),
    text.write(f"Average Change: ${average_change_total}\n")
    text.write(f"Greatest Increase in Profits: {greatest_increase_profit[0]} (${greatest_increase_profit[1]})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease_profit[0]} (${greatest_decrease_profit[1]})\n")
text.close()


