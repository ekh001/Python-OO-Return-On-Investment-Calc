# This original version uses lists for income and expense.

class ROI_Calc():

    """This class will create an ROI calculator that will calculate the ROI on a rental property by:
    -XIncome: allowing user to input INCOME: 
        rental, etc 
    -XExpenses: allowing user to input EXPENSES:
        tax, insurance, utilities, HOA, lawn/snow, vacancy, repairs,
        capital expenses, property management, mortgage
    -Yearly Cash Flow: subtracting user input EXPENSES from INCOME, multiply by 12
    -Inital Investment: allowing user to input INVESTMENT:
        down payment, closing cost, rehab(repairs), misc
    -ROI: divides Yearly Cash Flow by Investment, multiply by 100 to return percentage
    
     with:
        -monthlyIncome
        -monthlyExpenses
        -yearlyCashFlow
        -intialInvestment
        -returnOI
        
        This class will have the following attributes:

        """

    def __init__(self):
        self.income = []
        self.expense = []
        self.cashflow = []
        self.yearlycf = []
        self.investment = []


# A. 
    # create a method to show income and expense lists for troubleshooting.
    def showIncome(self):
        print('\nThis is the income you input:') 
        for spot in self.income:
            print(spot)
    def showExpense(self):
        print('\nThis is the expense you input:') 
        for spot in self.expense:
            print(spot)

# 1. 
    # create a method to input income.
    def monthlyIncome(self):    
        print("Let's get your income in!")    

        rental_income = (input("How much do you intend to charge for monthly rent?: "))
        self.income.append(rental_income)
        misc_income = (input("Will there be any other income from the property besides rent (such as laundry or a gym)? Input that here: "))
        self.income.append(misc_income)

        total = 0
        for ele in range(0, len(self.income)):
            total = total + int(self.income[ele])
        print(f"\nOkay, so your total income is {total}.")
    # Next step options:        
        print("\nMoving on!")
        if self.income and self.expense:
            self.cashflow = int(self.income[0]) - int(self.expense[0])            
            # do something like:
            print(f"\nLooks like your monthly cash flow is {self.cashflow}. Just a second while I figure out your yearly cash flow...")

            yearly_cash_flow = self.cashflow * 12
            self.yearlycf.append(yearly_cash_flow)
            print(f"\nAwesome! Based on your income and expenses, your yearly cash flow is: \n{yearly_cash_flow}. \nYou can skip the 'calculate cash flow' step and move on to record your investment.")
    # Next step options:
            next_step = input("\nType 'investments' or 'back' to access the main menu. If you made a mistake in your income, type 'income' to redo it.")
            if next_step == "investments":
                self.initialInvest()
            elif next_step == 'back':
                print('Okay!')
                return run()
            elif next_step == 'income':
                print('Okay!')
                self.income = []
                self.monthlyIncome()
        else:
            next_step = input("\nLet's input your expenses: type 'expenses' or 'back' to access the main menu. If you made a mistake in your income, type 'income' to redo it.")
            if next_step == "expenses":
                self.monthlyExpenses()
            elif next_step == 'back':
                print('Okay!')
                return run()
            elif next_step == 'income':
                print('Okay!')
                self.income = []
                self.monthlyIncome()

# 2. 
    # create a method to input expenses.
    def monthlyExpenses(self):
        print("\nLet's add your expenses!")

        tax_expense = (input("\nMonthly tax expenses: "))
        self.expense.append(tax_expense)
        ins_expense = (input("Projected monthly insurance expenses: "))
        self.expense.append(ins_expense)
        utility_expense = (input("Projected monthly utility expenses: "))
        self.expense.append(utility_expense)
        hoa_expense = (input("Projected monthly HOA fee: "))
        self.expense.append(hoa_expense)
        yard_expense = (input("Projected monthly lawn care expenses: "))
        self.expense.append(yard_expense)
        vacancy_expense = (input("Always best to be prepared for vacancy! Projected monthly vacancy budget: "))
        self.expense.append(vacancy_expense)
        repair_expense = (input("Everything breaks sometimes. Projected monthly repair budget: "))
        self.expense.append(repair_expense)
        cap_ex_expense = (input("Sometimes the BIG things break. Projected monthly capital expense budget: "))
        self.expense.append(cap_ex_expense)
        property_manager_expense = (input("Projected monthly property management fee: "))
        self.expense.append(property_manager_expense)
        mortgage_expense = (input("Almost done! How much is your monthly mortgage?: "))
        self.expense.append(mortgage_expense)

        total_expense = 0
        for ele in range(0, len(self.expense)):
            total_expense = total_expense + int(self.expense[ele])
        print(f"\nOkay, so your total expenses are {total_expense}.")
    # Automated yearly cash flow
        if self.income and self.expense:
            self.cashflow = int(self.income[0]) - int(self.expense[0])            
            # do something like:
            print(f"\nLooks like your monthly cash flow is {self.cashflow}. Just a second while I figure out your yearly cash flow...")
            yearly_cash_flow = self.cashflow * 12
            self.yearlycf.append(yearly_cash_flow)
            print(f"\nAwesome! Based on your income and expenses, your yearly cash flow is: \n{yearly_cash_flow}. \nYou can skip the 'calculate cash flow' stepand move on to record your investment.")
    # Next step options:
            next_step = input("\nType 'investments' or 'back' to access the main menu. If you made a mistake in your expenses, type 'expenses' to redo it.")
            if next_step == "investments":
                self.initialInvest()
            elif next_step == 'back':
                print('Okay!')
                return run()
            elif next_step == 'expenses':
                print('Okay!')
                self.expense = []
                self.monthlyExpenses()
        else: 
            print("\nPlease enter your income, and then move on to calculate your cash flow.")
            next_step = input("Type 'income' or 'back' to access the main menu. If you made a mistake in your expenses, type 'expenses' to redo it.")
            if next_step == "income":
                self.monthlyIncome()
            elif next_step == 'back':
                print('Okay!')
                return run()
            elif next_step == 'expenses':
                print('Okay!')
                self.expense = []
                self.monthlyExpenses()
    


# 3.
    # create a method to calculate cash flow.
    def yearlyCashFlow(self):
        if self.income == [] or self.expense == []:
            print("You really should try entering your income and expenses first, but okay.")
        elif self.income and self.expense:
            self.cashflow = int(self.income[0]) - int(self.expense[0])            
            # do something like:
            print(self.cashflow)
        yearly_cash_flow = self.cashflow * 12
        self.yearlycf.append(yearly_cash_flow)
        print(f"Your yearly cash flow is: \n{yearly_cash_flow}")


# 4.
    # Method to input the inital investment.
    def initialInvest(self):
        print("Let's add your initial investment into the equation.")
        down_payment = input("\nPlease enter your initial down payment: ")
        self.investment.append(down_payment)
        closing_costs = (input("Please insert your closing costs: "))
        self.investment.append(closing_costs)
        rehab_budget = (input("Please insert your rehab budget: "))
        self.investment.append(rehab_budget)
        misc_other_cost = (input("Please insert any other initial investment costs: "))
        self.investment.append(misc_other_cost)
        total_investment = 0
        for ele in range(0, len(self.investment)):
            total_investment = total_investment + int(self.investment[ele])
        print(f"\nJust to confirm, your initial investment is: \n{total_investment}")
    # Automated ROI:
        if self.yearlycf and self.investment:
            print("\nNow that you've input that absolutely bananas amount of information, let's get your projected return on investment!")
            final_cashflow = 0
            final_investment = 0
            for ele in range(0, len(self.yearlycf)):
                final_cashflow = final_cashflow + int(self.yearlycf[ele])
            for ele in range(0, len(self.investment)):
                final_investment = final_investment + int(self.investment[ele])
            ROI = (final_cashflow / final_investment) *100
            print(f"\nAll done! Your projected ROI is: \n{ROI}%. Do with that information what you will.")
        else: 
            print("\nHmmm, I think something is missing.")
            next_step = input("Type 'back' to access the main menu. If you made a mistake in your investments record, type 'investment' to redo it.")
            if next_step == 'back':
                print('Okay!')
                return run()
            elif next_step == 'investment':
                print('Okay!')
                self.investment = []
                self.initialInvest()

# 5. 
    # create a method to calculate the ROI by dividing cashflow/investment, and returning result * 100 for a percentage.
    def ROI(self):
        if self.yearlycf == [] or self.investment == []:
            print("Can't do math if the input isn't there! Input your income/expenses, calculate your cash flow, and input your investment first.")
        if self.yearlycf and self.investment:
            print("Now that you've input that absolutely bananas amount of information, let's get your projected return on investment!")
            final_cashflow = 0
            final_investment = 0
            for ele in range(0, len(self.yearlycf)):
                final_cashflow = final_cashflow + int(self.yearlycf[ele])
            for ele in range(0, len(self.investment)):
                final_investment = final_investment + int(self.investment[ele])
            ROI = (final_cashflow / final_investment) *100
            print(f"All done! Your projected ROI is: \n{ROI}%. Do with that information what you will.")

# Turn the dream into a reality. 
my_ROIC = ROI_Calc()


def run():
    print('\nWelcome to the greatest ROI Calculator in the great state of Exaggeration!')
    print("Math is hard, so please make sure to input your income, expenses, investments, and calculate your cash flow before hitting that letter E!")
    while True:
        print('\nThese are your options:')
        response = input('\nType: \n- "A" to report your property income, \n- "B" to input your property expense, \n- "C" to calculate cash flow, \n- "D" to report your initial investment, \n- "E" to get your total projected ROI, or \n- "quit" to quit the program:\n ')
        
        if response.lower() == 'quit':            
            print('Out the door dinosaur!')
            break
        elif response.lower() == 'a':
            my_ROIC.monthlyIncome()
        elif response.lower() == 'b':
            my_ROIC.monthlyExpenses()
        elif response.lower() == 'c':
            my_ROIC.yearlyCashFlow()
        elif response.lower() == 'd':
            my_ROIC.initialInvest()
        elif response.lower() == 'e':
            my_ROIC.ROI()
# -------------FOR PROGRAMMER--------------------
        # elif response.lower() == 'showincome':
        #     my_ROIC.showIncome()
        # elif response.lower() == 'showexpense':
        #     my_ROIC.showExpense()
        else: 
            print("Try something else, please. Look closely at the options.")

# Call it!
run()