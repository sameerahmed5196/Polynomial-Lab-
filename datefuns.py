from date import Date

def weekend_dates(m,y):
    d = Date(m,1,y)
    while d.month() == m:
        if d.day_of_week() == "Saturday" or d.day_of_week() =="Sunday":
            print (d)
        d = d.nextday() 


def first_mondays(y):
    for x in range(12):
        d = Date(x+1,1,y)
        while d.day_of_week() != "Monday":
           d = d.nextday()
        print(d)




def interval_schedule(start_date,end_date, interval):
    L = []

    #d = Date(start_date.m,start_date.d,start_date.y)
    #e = Date(end_date.m,end_date.d,end_date.y)
    z = Date(start_date.month(),start_date.day(),start_date.year())
    for x in range(0,end_date.daycount()- start_date.daycount(),interval):
        L.append(z)
        z = z + interval
    return L

l1 = interval_schedule(Date(9,6,2016),Date(10,31,2016),12)
for e in l1:
    print(e)
        
        
               
        
        
        
        
        
    
