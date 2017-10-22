balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
month=0
mir=annualInterestRate/12
ubem=balance
#def fun(balance, annualInterestRate, monthlyPaymentRate):
while month<12:
    mmp=monthlyPaymentRate*ubem
    mub=ubem-mmp
    ubem=mub+mir*mub
    month=month+1
print('Remaining Balance: '+str(round(ubem,2)))