#define a class expense tracker that store the
#expenses and income in a dictionary
#implement a method to
#store transaction
#view transaction
#calc the total expense/income

class expense_tracker:

    def __init__(self):
        self.expenseDict={
            "income": [],
            "expenses": []
        }
    def store_transactions(self,type,amt,category,date,details):
        trans={
            "Amount":amt,
            "Category":category,
            "Date":date,
            "Details":details
            }
        if type=="income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expemses'].append(trans)
    def view_transactions(self):
        print("Your income")
        for item in self.expenseDict['income']:
            print(item)
        for item in self.expenseDict['expense']:
            print(item)
    def calculate_transactions(self):
        total_income=0
        for item in self.expenseDict['income']:
            total_income+=item["Amount"]
        print("Total income\t:\t",total_income)

        total_expense=0
        for item in self.expenseDict['expense']:
            total_expense+=item["Amount"]
        print("Total expenses\t:\t",total_expense)
def collectInput():
    amt=int(input("enter the amount: "))
    category=input("enter category: ")
    date=input("enter the date (DD\MM\YY)")
    details=input("Enter description: ")
    return amt,category,date,details
myexpense=expense_tracker()

def export_to_csv(self,filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames=["Type","Amount","Category","Date","Details"]
        writer= csv.D



while True:
    print(">>>MY EXPENSE TRACKER<<<")
    print("1.Record income")
    print("2.Record Expense")
    print("3.View Records")
    print("4 View my spending")
    print("5. exit")

    choice=int(input("enter a choice: ").strip())
    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")





        