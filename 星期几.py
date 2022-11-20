def whatDay(year,month,date):
    answer=(date+year-int((14-year)/2)+int(31*(month+12*int((14-year)/2)-2)/12)+int((year-int((14-year)/2))/4)-int((year-int((14-year)/2))/100)+int((year-int((14-year)/2))/400))%7
    if answer==0:answer=7
    return answer
print(whatDay(2022,6,14))