def daysBetweenDates( date1: str, date2: str) -> int:
    d1 = map(int, date1.split('-'))
    d2 = map(int, date2.split('-'))
    y1,m1,d1 = d1
    y2,m2,d2 = d2

    total_days = abs(y1-y2) * 365
    
    return total_days
    
print(daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))