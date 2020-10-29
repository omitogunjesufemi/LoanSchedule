#User Input
loan_value = float(input("Loan Amount: "))
years = int(input("Number of Years: "))
ann_rate = int(input("Annual Interest Rate: "))

no_payment = years * 12 
monthly_rate = ann_rate / (100 * 12)

monthly_pay = (abs((monthly_rate * (loan_value * (1 + monthly_rate) ** no_payment)) / ((1)*(1-(1+ monthly_rate) ** no_payment))))
total_payment = monthly_pay * 12
count = 0

print(f"Month Pay: {monthly_pay:.2f}")
print(f"Total Pay: {total_payment:.2f}")
print(f"PAYMENT    INTEREST    PRINCIPAL    BALANCE")

while no_payment >= 1:
    monthly_pay = (abs((monthly_rate * (loan_value * (1 + monthly_rate) ** no_payment)) / ((1)*(1-(1+ monthly_rate) ** no_payment))))
    total_payment = monthly_pay * 12
    monthly_interest = (monthly_rate * loan_value)
    principal = (monthly_pay - monthly_interest)
    balance = (loan_value - principal)
    
    loan_value = balance
    no_payment = no_payment - 1
    count += 1
    
    print(f"{count:<10} {monthly_interest:<10.2f}  {principal:<12.2f} {balance:.2f}")