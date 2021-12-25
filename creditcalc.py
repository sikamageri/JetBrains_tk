import math
import argparse

parser = argparse.ArgumentParser(description="Hello! This is the Loan Calculator.")
parser.add_argument('--type', choices=["annuity", "diff"], 
                    help='Type of payment: "annuity" or "diff" (differentiated)')
parser.add_argument('--principal', type=int,
                    help='principal')
parser.add_argument('--periods', type=int,
                    help='periods')
parser.add_argument('--interest', type=float,
                    help='interest')
parser.add_argument('--payment', type=int,
                    help='payment')
args = parser.parse_args()

input_values = [args.type, args.principal, args.periods, args.interest, args.payment]

# print(['type', 'principal', 'periods', 'interest', 'payment'])
# print('input_values:', input_values)

# Func date_response return final message 'It will take ... month to repay the loan'
def date_response(payment_period):
    if (payment_period / 12) < 1:
        if payment_period == 1:
            text = f'It will take {payment_period} month to repay the loan!'
            return text
        else:
            text = f'It will take {payment_period} months to repay the loan!'
            return text
    else:
        years = payment_period // 12
        month = payment_period % 12
        if years == 1:
            if month == 1:
                text = f'It will take {years} year {month} month to repay the loan!'
                return text
            else:
                text = f'It will take {years} year {month} months to repay the loan!'
                return text
        else:
            if month == 1:
                text = f'It will take {years} years {month} month to repay the loan!'
                return text
            elif month == 0:
                text = f'It will take {years} years to repay the loan!'
                return text
            else:
                text = f'It will take {years} years {month} months to repay the loan!'
                return text

def number_of_month(loan_interest, monthly_payment, loan_principal):
    nominal_interest_rate = (loan_interest / (12 * 100))
    number_of_month = math.log((monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal)), 1 + nominal_interest_rate)
    return math.ceil(number_of_month)

# Errors check:
# --type
if args.type == 'diff':
    # --payment == None
    if args.payment == None:
        if args.principal == None:
            print ('Incorrect parameters.')
        elif args.periods == None:
            print ('Incorrect parameters.')
        elif args.interest == None:
            print ('Incorrect parameters.')
        else: 
            # write code for Diff payment here
            loan_principal = int(args.principal)
            loan_period = int(args.periods)
            loan_interest = float(args.interest)
            nominal_interest_rate = (loan_interest / (12 * 100))
            overpayment = - loan_principal
            for m in range(1, int(loan_period) + 1):
                if overpayment < 0:
                    diff_payment = loan_principal / loan_period + nominal_interest_rate * (loan_principal - loan_principal * (m - 1) / loan_period)
                    text = f'Month {m}: = payment is {math.ceil(diff_payment)}' 
                    print(text)
                    overpayment += math.ceil(diff_payment)
            print(f'Overpayment {m} =', overpayment)
                    
#             print(text)
#             print('Overpayment =', overpayment)
            
    else:
        print ('Incorrect parameters.')
    
elif args.type == 'annuity':
    if args.principal == None:
        # Check for 'periods, interest, payment'
        if args.payment == None:
            print ('Incorrect parameters.')
        elif args.periods == None:
            print ('Incorrect parameters.')
        elif args.interest == None:
            print ('Incorrect parameters.')
        else: 
            # write code for annuity 'periods, interest, payment'
            # loan principal
            annuity_monthly_payment = float(args.payment)
            loan_period = int(args.periods)
            loan_interest = float(args.interest)
            nominal_interest_rate = (loan_interest / (12 * 100))
            loan_principal = annuity_monthly_payment / ((nominal_interest_rate * math.pow((1 + nominal_interest_rate), loan_period))/(math.pow((1 + nominal_interest_rate), loan_period) - 1))
            text = f'Your loan principal = {int(loan_principal)}!'
            overpayment = math.ceil(math.ceil(annuity_monthly_payment) * loan_period - loan_principal)
            print(text)
            print('Overpayment =', overpayment)
            
            
    elif args.periods == None:
        # Check for 'principal, interest, payment'
        if args.principal == None:
            print ('Incorrect parameters.')
        elif args.interest == None:
            print ('Incorrect parameters.')
        elif args.payment == None:
            print ('Incorrect parameters.')
        else: 
            # write code for annuity 'principal, interest, payment'
            # number of monthly payments
            loan_principal = int(args.principal)
            monthly_payment = int(args.payment)
            loan_interest = float(args.interest)
            payment_period = number_of_month(loan_interest, monthly_payment, loan_principal)
            print(date_response(payment_period))
            overpayment = math.ceil(math.ceil(monthly_payment) * payment_period - loan_principal)
            print('Overpayment =', overpayment)
        
    elif args.payment == None:
        # Check for 'principal, interest, periods'
        if args.principal == None:
            print ('Incorrect parameters.')
        elif args.interest == None:
            print ('Incorrect parameters.')
        elif args.periods == None:
            print ('Incorrect parameters.')
        else: 
            # write code for annuity 'principal, interest, periods'
            # annuity monthly payment amount
            loan_principal = int(args.principal)
            loan_period = int(args.periods)
            loan_interest = float(args.interest)
            nominal_interest_rate = (loan_interest / (12 * 100))
            annuity_monthly_payment = loan_principal * nominal_interest_rate * math.pow((1 + nominal_interest_rate), loan_period) / (math.pow((1 + nominal_interest_rate), loan_period) - 1)
            text = f'Your annuity payment = {math.ceil(annuity_monthly_payment)}!'
            overpayment = math.ceil(math.ceil(annuity_monthly_payment) * loan_period - loan_principal)
            print(text)
            print('Overpayment =', overpayment)
            
else:
    print ('Incorrect parameters.')

    ### CheckLines ###
# Example 1:
# python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Example 2:
# python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Example 3:
# python creditcalc.py --type=diff --principal=1000000 --payment=104000
# Example 4:
# python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Example 5:
# python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Example 6:
# python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8


# print('What do you want to calculate?')
# print('type "n" for number of monthly payments,')
# print('type "a" for annuity monthly payment amount,')
# print('type "p" for loan principal:')
# type_of_calc = input()
# 
# Func date_response return final message 'It will take ... month to repay the loan'
# def date_response(payment_period):
#     if (payment_period / 12) < 1:
#         if payment_period == 1:
#             text = f'It will take {payment_period} month to repay the loan'
#             return text
#         else:
#             text = f'It will take {payment_period} months to repay the loan'
#             return text
#     else:
#         years = payment_period // 12
#         month = payment_period % 12
#         if years == 1:
#             if month == 1:
#                 text = f'It will take {years} year {month} month to repay the loan'
#                 return text
#             else:
#                 text = f'It will take {years} year {month} months to repay the loan'
#                 return text
#         else:
#             if month == 1:
#                 text = f'It will take {years} years {month} month to repay the loan'
#                 return text
#             else:
#                 text = f'It will take {years} years {month} months to repay the loan'
#                 return text
# 
# def number_of_month(loan_interest, monthly_payment, loan_principal):
#     nominal_interest_rate = (loan_interest / (12 * 100))
#     number_of_month = math.log((monthly_payment / (monthly_payment - nominal_interest_rate * loan_principal)), 1 + nominal_interest_rate)
#     return math.ceil(number_of_month)
# 
# if type_of_calc == 'n':
#     # number of monthly payments
#     loan_principal = int(input('Enter the loan principal:'))
#     monthly_payment = int(input('Enter the monthly payment:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     
#     payment_period = number_of_month(loan_interest, monthly_payment, loan_principal)
#     print(date_response(payment_period))
#     
# elif type_of_calc == 'a':
#     # annuity monthly payment amount
#     loan_principal = int(input('Enter the loan principal:'))
#     loan_period = int(input('Enter the number of periods:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     nominal_interest_rate = (loan_interest / (12 * 100))
#     annuity_monthly_payment = loan_principal * nominal_interest_rate * math.pow((1 + nominal_interest_rate), loan_period) / (math.pow((1 + nominal_interest_rate), loan_period) - 1)
#     text = f'Your monthly payment = {math.ceil(annuity_monthly_payment)}!'
#     print(text)
# 
# elif type_of_calc == 'p':
#     # loan principal
#     annuity_monthly_payment = float(input('Enter the annuity payment:'))
#     loan_period = int(input('Enter the number of periods:'))
#     loan_interest = float(input('Enter the loan interest:'))
#     nominal_interest_rate = (loan_interest / (12 * 100))
#     loan_principal = annuity_monthly_payment / ((nominal_interest_rate * math.pow((1 + nominal_interest_rate), loan_period))/(math.pow((1 + nominal_interest_rate), loan_period) - 1))
#     text = f'Your loan principal = {int(loan_principal)}!'
#     print(text)