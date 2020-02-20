# PyBank

# Read budget_data.csv
import os
import csv

csvpath =os.path.join('Documents/Data Science Bootcamp/Python-challenge/PyBank/budget_data.csv')



with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header=next(csvreader)
    print(f'csv_header:{csv_header}')

    # Reference : https://pythonprogramming.net/reading-csv-files-python-3/
    # create variables to store dates and profit/losses
    dates=[]
    profit_loss=[]

    for row in csvreader:
        print(row)
        date=row[0]
        profitloss=row[1]

        dates.append(date)
        profit_loss.append(profitloss)
    
    print(dates)
    print(profit_loss)


# The total number of months included in the dataset
# Each date look like 'Jan-10', 'Feb-10' etc. To count the num of month, save the first 3 letters in a list
months=[]
for x in dates:
    first3 = x[0:3]
    months.append(first3)
print(months)

# count the number of items  in "months" list. Items liik like ['Jan', 'Feb', 'Mar', 'Apr', ....]
# reference : https://thispointer.com/python-get-number-of-elements-in-a-list-lists-of-lists-or-nested-list/
print(len(months))
# answer is 86
# save this answer in a variable, total_months
total_months=(len(months))
print(total_months)

# ----------------------------------

# The net total amount of "Profit/Losses" over the entire period
# all the profit_loss are stored in profit_loss list, but they seems to be string.
# They look like ['867884', '984655', '322013', '-69417',  ....]
tot=0
for y in profit_loss:
    tot= int(y) + tot
print(tot)
# tot is 38382578. Save this in a variable, Total with : and $ f"[{pie_list.index(y)}] {y}")
Total=f"Total : ${tot}"
print(Total)
# This looks like 'Total : $38382578'

# -----------------------------------

# The average of the changes in "Profit/Losses" over the entire period
# reference : http://love-python.blogspot.com/2012/03/get-next-element-from-list-in-python.html
# for loop with range
current_v=[]
for index in range(0 , 86):
    value1=profit_loss[index]
    current_v.append(value1)

next_v=[]
for index2 in range(1 , 86):
    value2=profit_loss[index2]
    next_v.append(value2)
print(next_v)

sum_change=0
for z in range(0,85):
    change=int(next_v[z]) - int(current_v[z])
    #print(change)
    sum_change=sum_change + change
print(sum_change)
# reference round function : https://www.w3schools.com/python/ref_func_round.asp
average_change=round((sum_change / 85), 2) #-2315.1176470588234
print(average_change)

# ------------------------------------ 

# The greatest increase in profits (date and amount) over the entire period
# Use the lists current_v and next_v above

large=0
small=0
for i in range(0,85):
    diff=int(next_v[i]) - int(current_v[i])
    if diff > 0 and diff > large:
        large=diff
        lindex=i+1
        ldate=str(dates[lindex])
        ldate2=ldate[0:4] + str(20) +ldate[4:]
    elif diff < 0 and diff < small :
        small=diff
        sindex=i+1
        sdate=str(dates[sindex])
        sdate2=sdate[0:4] + str(20) +sdate[4:]
print(large, ldate, ldate2)
print(small, sdate, sdate2)

# Write a report to terminal
report=(
    f"Financial Analysis \n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total : ${tot}\n"
    f"Average  Change: ${average_change}\n"
    f"Greatest Increase in Profits: {ldate2} (${large})\n"
    f"Greatest Decrease in Profits: {sdate2} (${small})"
    )
print(report)

# write a report to txt file
output_path = os.path.join("Documents/Data Science Bootcamp/Python-challenge/PyBank/Report.txt")

with open(output_path, "w") as txtfile:
    txtfile.write(    
    f"Financial Analysis \n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total : ${tot}\n"
    f"Average  Change: ${average_change}\n"
    f"Greatest Increase in Profits: {ldate2} (${large})\n"
    f"Greatest Decrease in Profits: {sdate2} (${small})"
    )





