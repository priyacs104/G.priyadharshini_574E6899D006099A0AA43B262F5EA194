year=2020

if (year % 400 == 0) and (year % 100 == 0):
  print(format(year)," is a leap year")
  
elif(year % 4 == 0) and (year % 100 != 0):
  print(format(year)," is a leap year")

else:
  print( format(year),"is not a leap year")