# Hackos : 10
import calendar

day, month, year = input().split()
week = calendar.weekday(int(year), int(day), int(month))
print (calendar.day_name[week].upper())
