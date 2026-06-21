import csv
from datetime import datetime

current_time=datetime.now().strftime('%d-%m-%y %H:%M:%S')

class Transactions:

    def __init__(self,name,salary,food,shopping,travelling,electricity_bill,extra_activities,date_time):
        self.name=name
        self.salary=salary
        self.food=food
        self.shopping=shopping
        self.travelling=travelling
        self.electricity_bill=electricity_bill
        self.extra_activities=extra_activities
        self.datetime=date_time

    def calculating_balance(self):
        self.balance=self.salary-(self.food+self.electricity_bill+self.shopping+self.travelling+self.extra_activities)
 
    def show_balance(self):
        return self.balance
    
    def Monthly_expenses(self):
        total_expenses=self.food+self.electricity_bill+self.shopping+self.travelling+self.extra_activities
        return total_expenses


    def generate_report(self):
        return f'name:{self.name}\nmonthly salary:{self.salary}\n----------------------monthly expenses-------------------\nfood expenses:{self.food}\ntravelling expenses:{self.travelling}\nshopping expenses:{self.shopping}\nElectricity bill Expenses:{self.electricity_bill}\nextra activities:{self.extra_activities}\nafter calculating all expenses the remaining balance:{self.balance}\ndata inserted date and time:{self.datetime}'

    def Export_csv_write(self):
        with open('expense_tracker.csv','w',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(['name','salary','food','shopping','travelling','electricity_bill','extra_activities','remaining_balance','datetime'])
            writer.writerow([self.name,self.salary,self.food,self.shopping,self.travelling,self.electricity_bill,self.extra_activities,self.balance,self.datetime])
            return 'data inserted successfully'
    
    def Export_csv_append(self):
        with open('expense_tracker.csv','a',newline='')as f:
            writer=csv.writer(f)
            writer.writerow([self.name,self.salary,self.food,self.shopping,self.travelling,self.electricity_bill,self.extra_activities,self.balance,self.datetime])
        
def Inputs_From_User():
    name=input('enter name:')
    salary=int(input("enter monthly salary:"))
    with open('expense_tracker.csv','r')as f:
        reader=list(csv.DictReader(f))
        found=False
        for row in reader:
            if row["name"]==name and int(row["salary"])==salary:
                found=True
                break
            
        if found:
            print('Already Exists')

        else:
            if type(salary)==int:
                food=int(input("enter food monthly expenses:"))
                if type(food)==int:
                    shopping=int(input("enter monthly shopping expenses:"))
                    if type(shopping)==int:
                        travelling=int(input("enter monthly travelling expenses:"))
                        if type(travelling)==int:
                            electricity_bill=int(input('enter electricity monthly bill expenses:'))
                            if type(electricity_bill)==int:
                                extra_activities=int(input("enter your extra monthly expenses:"))
                                if type(extra_activities)==int:
                                    date_time=current_time
                                    obj=Transactions(name,salary,food,shopping,travelling,electricity_bill,extra_activities,date_time)
                                    print('details added successfully')
                                    return obj
                                else:
                                    print('invalid expenses')
                            else:
                                print('invalid expenses')    
                        else:
                            print('invalid expenses')
                    else:
                        print('invalid expenses')
                else:
                    print('invalid expenses')
            else:
                print('invalid salary')





Outer=True
while Outer:
    print('---------------------Expense Tracker--------------------------------')
    print('1.Add your Details\n2.Get Existing Details\n3.Exit')
    try:
        x=int(input('Choose an Option:'))
        if x==1:
            obj=(Inputs_From_User())
            # if 
            obj.calculating_balance()
            obj.Export_csv_append()
            inner=True
            while inner:
                print('------------------See Your Expense Division--------------------\n1.Generate Report\n2.Show Total Monthly Expenses\n3.Show Salary After cutting expenses\n4.Exit')
                y=int(input('choose an option:'))
                if y==1:
                    print(obj.generate_report())
                elif y==2:
                    print(obj.Monthly_expenses())
                elif y==3:
                    print(obj.show_balance())
                elif y==4:
                    inner=False
                else:
                    print('Invalid Number')
        elif x==2:
            u_name=input('enter your name:')
            u_sal=int(input('enter your salary:'))
            if type(u_sal)!=int:
                print('invalid salary')
            else:
                inner1=False
                with open('expense_tracker.csv','r')as f:
                    reader=list(csv.DictReader(f))
                    for row in reader:
                        if row["name"]==u_name and int(row["salary"])==u_sal:
                            inner1=True
                            while inner1:
                                print('------------------See Your Expense Division--------------------\n1.Generate Report\n2.Show Total Monthly Expenses\n3.Show Salary After cutting expenses\n4.Change the Expenses\n5.Exit')
                                y1=int(input('choose an option:'))
                                ob = Transactions(
                                        row["name"],
                                        int(row["salary"]),
                                        int(row["food"]),
                                        int(row["shopping"]),
                                        int(row["travelling"]),
                                        int(row["electricity_bill"]),
                                        int(row["extra_activities"]),
                                        row["datetime"])
                                if y1==1:
                                    ob.calculating_balance()
                                    print(ob.generate_report())
                                elif y1==2:
                                    print(ob.Monthly_expenses())
                                elif y1==3:
                                    ob.calculating_balance()
                                    print(ob.show_balance())
                                elif y1==4:
                                    inner2=True
                                    while inner2:
                                        print('-----------------------Add Increased Expense---------------\n1.Add Food Expenses\n2. Add Shopping Expense\n3.Add Travelling Expense\n4.Add Electricity Bill\n5.Add Extra Activity Expense\n6.Update Your Salary\n7.Exit')
                                        z=int(input('Choose an option:'))
                                        with open('expense_tracker.csv', 'w', newline='') as f:
                                            fieldnames = ['name','salary','food','shopping','travelling',
                                                            'electricity_bill','extra_activities',
                                                            'remaining_balance','datetime']
                                            writer = csv.DictWriter(f, fieldnames=fieldnames)
                                            writer.writeheader()
                                            writer.writerows(reader)
                                            if z==1:
                                                add_food=int(input('enter Food Expenses:'))
                                                if add_food:
                                                    row['food']=str(int(row['food'])+add_food)
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print('Invalid Number')
                                            elif z==2:
                                                add_shop=int(input('enter shopping expenses:'))
                                                if add_shop>0:    
                                                    row['shopping']=str(int(row['shopping'])+add_shop)
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print('Invalid Number')
                                            elif z==3:
                                                add_travel=int(input("enter Travelling Expenses:"))
                                                if add_travel>0:
                                                    row['travelling']=str(int(row['travelling'])+add_travel)
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print('Invalid Number')
                                            elif z==4:
                                                add_Ele=int(input("enter Electricity Expenses:"))
                                                if add_Ele>0:
                                                    row['electricity_bill']=str(int(row['electricity_bill'])+add_Ele)
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print('Invalid number')
                                            elif z==5:
                                                add_Act=int(input("enter Extra-Activity Expenses:"))
                                                if add_Act>0:
                                                    row['extra_activities']=str(int(row['extra_activities'])+add_Act)
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print('Invalid number')
                                            elif z==6:
                                                add_sal=int(input("enter your salary:"))
                                                if 0<add_sal:
                                                    row['salary']=add_sal
                                                    row['datetime']=current_time
                                                    print('updated successfully')
                                                else:
                                                    print("invalid number")
                                            elif z==7:
                                                inner2=False
                                            else:
                                                print('Invalid Number')
                                elif y1==5:
                                    inner1=False
                                else:
                                    print('Invalid option')           
                    if not inner1:
                        print('name and salary not present')
        elif x==3:
            Outer=False
        else:
            print('invalid number')
    except TypeError:
        print('Please enter only numbers.')
    except:
        print()

                




