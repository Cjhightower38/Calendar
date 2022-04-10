def is_leap(year):
  '''
  This function determines if a year is leap or not and returns a boolean.
  '''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  '''
This function takes the results from the is_leap function and return 29 days if it is a leap year. Becareful with the
months off by 1. A user will not enter off by one so month -1 corrects the problem. Lists start at 0
'''
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)