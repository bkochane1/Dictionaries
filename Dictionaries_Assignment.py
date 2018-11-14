employees = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

name = []  # create list
number = []
hourly = []
for employee in employees: # sort based upon a type of data
    if(type(employee) == int): 
        number.append(employee)
    elif (type(employee) == str):
        name.append(employee)
    elif(type(employee)  == float):
        hourly.append(employee)

name = list(set(name)) # remove duplicate names
number = list(set(number))
hourly = list(set(hourly))

total_hourly_rates = [] # copy the original list to the new list 
for hour in hourly:     # mulitply each hour by 1.3 
    hour = hour * 1.3
    total_hourly_rates.append(hour) 

max_hourly = max(total_hourly_rates) # find max salary (4)
if max_hourly > 37.30:
    print("This rate is budgetary concern.") # print warning message

underpaid_salaries = [] # 5  create a list
for total_hourly_rate in total_hourly_rates: # loop through total hourly rate list
    if (total_hourly_rate >= 28.15) and (total_hourly_rate <= 30.65) : # check the salary if is under or above
        underpaid_salaries.append(total_hourly_rate) # check the salaries and the ones that meet condition put in undepaid

company_raises = [] # 6 copy of original hourly list
for hour_rate in hourly: # 6
    if (hour_rate >= 22) and (hour_rate <= 24) :
        hour_rate = hour_rate * 1.05 # if hour rate is within the range mulitply by 5 %
    elif (hour_rate >= 24) and (hour_rate <= 26) :
        hour_rate = hour_rate * 1.04 # if hour rate is within the range mulitply by 4 % raise
    elif (hour_rate >= 26) and (hour_rate <= 28) :
        hour_rate = hour_rate * 1.03 # if houur rate is within the range mulitply by 3 % raise
    else:
        hour_rate = hour_rate * 1.02 #  All other salary ranges should get a standard 2% raise to the current rate.
    company_raises.append(hour_rate)

randomBool = True
date = 22
month = 11
day = "Thursday"
if((date == 22) and (month == 11) and (day == "Thursday") and (randomBool == True)):
    print("This is Thanksgiving Day!")

employee_dict = [] # creating empty list to hold dictionaries
counter = 0

for temp_name in name:
    employee_dict.append({'name': temp_name, 'number': number[counter], 'hourly': hourly[counter], 'total_hourly_rate': total_hourly_rates[counter], 'company_raise': company_raises[counter]})
    counter = counter + 1

counter = 0
print_str = ""

for employee in employee_dict:
    print_str = print_str + "Index: " + str(counter)
    print_str = print_str + " | Name: " + employee["name"]
    print_str = print_str + " | Number: " + str(employee["number"])
    print_str = print_str + " | Hourly: " + str(employee["hourly"])
    print_str = print_str + " | Total Hourly: " + str(employee["total_hourly_rate"])
    print_str = print_str + " | Company Raise: " + str(employee["company_raise"]) + "\n"

    counter = counter + 1

print(print_str)