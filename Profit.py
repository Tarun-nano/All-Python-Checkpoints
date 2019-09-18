#you have beem supplied with two list : monthly revenue and monthly expense for the financial year in question
#calculate
#profit for each month , profit after tax for each month (tax rate is 30 percnt) , profit margin for each month equals to profit after divided by revenue 
#good month == profit after tax was greater than mean for the year
#bad month == profit after tax was less than the mean for the year
#in best month== profit after tax was max
#wrost month== profit after tax was min
import statistics
revenue= [14574.49,7606.49,8611.41,9175.41,8058.65,8105.44,11496.28,9766.09,10305.32,14379.96,10713.97,15433.50]
expenses= [12051.81,5695.01,12319.20,12089.72,8658.59,840.20,3285.07,5821.12,6976.93,16618.61,10054.37,3803.96]
profit=[]
x=len(revenue)
print(x)
for i in range(0,x):
    p=revenue[i]-expenses[i]
    profit.append(p)
print("Profit before tax : ")
print()
print(profit)
print()
profit_tax=[]

for i in range(0,x):
    z=profit[i]-profit[i]*0.30
    profit_tax.append(z)
print("profit after tax : ")
print()
print(profit_tax)
mean_profit=statistics.mean(profit_tax)
print()
print()
print("mean profit : ")
print(mean_profit)
print()
print()
for i in range(0,x):
    if profit_tax[i]>mean_profit:
        print("good for : ",i+1," month ",profit_tax[i])
        print()
        print()
    if profit_tax[i]<mean_profit:
        print("bad for : ",i+1,"th month ",profit_tax[i])
        print()
        print()
    if profit_tax[i]==max(profit_tax):
        print("best for : ",i+1,"th month ",profit_tax[i])
        print()
        print()
    if profit_tax[i]==min(profit_tax):
        print("wrost for : ",i+1,"th month ",profit_tax[i])
        
