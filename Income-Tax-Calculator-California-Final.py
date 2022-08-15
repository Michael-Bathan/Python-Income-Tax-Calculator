# Michael Bathan's Income Calculator
# This is for California residents

grossIncome = input("Your income is: ")
grossIncome = float(grossIncome)

if 0 < grossIncome <= 9325:
    stateTax = grossIncome*0.01
if 9326 <= grossIncome <= 22107:
    stateTax = 93.25+((grossIncome-9325)*0.02)
if 22108 <= grossIncome <= 34892:
    stateTax = 348.89+((grossIncome-22107)*0.04)
if 34893 <= grossIncome <= 48435:
    stateTax = 860.29+((grossIncome-34892)*0.06)
if 48436 <= grossIncome <= 61214:
    stateTax = 1672.87+((grossIncome-48435)*0.08)
if 61215 <= grossIncome <= 312686:
    stateTax = 2695.19+((grossIncome-61214)*0.093)
if 312687 <= grossIncome <= 375221:
    stateTax = 26082+((grossIncome-312686)*0.103)
if 375222 <= grossIncome <= 625369:
    stateTax = 32523.2+((grossIncome-375221)*0.113)
if 625370 <= grossIncome:
    stateTax = 60789.92+((grossIncome-625369)*0.123)

if 0 <= grossIncome <= 9950:
    federalTax = grossIncome*0.1
if 9951 <= grossIncome <= 40525:
    federalTax = 995+((grossIncome-9950)*0.12)
if 40526 <= grossIncome <= 86375:
    federalTax = 4664+((grossIncome-40525)*0.22)
if 86376 <= grossIncome <= 164925:
    federalTax = 14751+((grossIncome-86375)*0.24)
if 164926 <= grossIncome <= 209425:
    federalTax = 33603+((grossIncome-164925)*0.32)
if 209426 <= grossIncome <= 523600:
    federalTax = 47843+((grossIncome-209425)*0.35)
if 523601 <= grossIncome:
    federalTax = 157804+((grossIncome-523600)*0.37)

StateTax = "Your State Tax is: "
stateTax = str(stateTax)
print(StateTax+stateTax)
FederalTax = "Your Federal Tax is: "
federalTax = str(federalTax)
print(FederalTax+federalTax)

stateTax = float(stateTax)
federalTax = float(federalTax)

netIncome = grossIncome-stateTax-federalTax

NetIncome = str(netIncome)
netIncome = "Your net income is: "
print(netIncome+NetIncome)

NetIncome = float(NetIncome)

hourly = "Your net hourly income is: "
Hourly = NetIncome/2000
Hourly = str(Hourly)
print(hourly+Hourly)

monthly = "Your net monthly income is: "
Monthly = NetIncome/12
Monthly = str(Monthly)
print(monthly+Monthly)