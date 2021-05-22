# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Create a list to store these monthly expenses and using that find out,
expense = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(expense[1]-expense[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print(expense[0]+expense[1]+expense[2])
print(sum(expense[:3]))

# 3. Find out if you spent exactly 2000 dollars in any month
for i in expense:
    if i==2000:
        print("You are exactly spent 2000 dollars")
        break
else: print("You did not exactly spent 2000 dollars in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
# based on this
expense[3] = expense[3] - 200
print(expense[3])