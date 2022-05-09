import time
import colorama as cll
from os import system
cll.init()
def main():
    L=[]
    print('======================Welcome====================')
    print('You are going to enter the main menu in 5 seconds')
    print(cll.Fore.RED+'Notice: There is a shortage of busses due the Corona Outbreak'+cll.Style.RESET_ALL)
    print('But we are doing our best to serve you the best facility')
    print(cll.Back.GREEN+'Important Advisory: Wear your masks and maintain proper distance'+cll.Style.RESET_ALL)
        
    time.sleep(5)
    system('cls')
    journeys=[['T','Delhi              Agra','            Yamuna Expy             233',500],
              ['T','Agra               Delhi','           Yamuna Expy             233',500],
              ['G','Delhi             Lucknow','        Yamuna Expy+Agra          554',1200],
              ['G','Lucknow            Delhi','         Yamuna Expy+Agra          554',1200],
              ['G','Delhi             Amritsar','     Jammu-Delhi rd.+NH 44       449',1000],
              ['G','Amritsar           Delhi','       Jammu-Delhi rd.+NH 44       449',1000],
              ['T','Delhi             Dehradun','    Upper Ganga Canal Road       256',700],
              ['T','Dehradun           Delhi','      Upper Ganga Canal Road       256',700]]
              
    i=1
    while i:
        def proceed():
            system('cls')
            print('This is the booking window')
            print('Select your journey type from below:')
            print('1. General Route Busses')
            print('2. Tourism Busses')
            print('3. Exit')
            
            try:
                b=int(input('Enter your Choice'))
                if b==1:
                    print('Choose your comfort zone:')
                    print('1. AC+Sleeper')
                    print('2. Non AC+Sleeper')
                    print('3. AC+Non Sleeper')
                    print('4. Non AC+Non Sleeper')
                    print('5. Exit')
                    
                    try:
                        c=int(input('Enter your Choice'))
                        if c in [1,2,3,4]:
                            L.append(c)
                        
                            if c==1:
                                print('Select your origin and destination:')
                                print('Origin          Destination             Via               Distance       Fair')
                                        
                                for i in range(len(journeys)):
                                    if journeys[i][0]=='G':
                                        print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.3)
                                    else:
                                        pass
                                try:
                                    d=int(input('Enter your Choice'))
                                    L.append(d)
                                    print('This is to finalize your Ticket Booking')
                                    try:
                                        e=int(input('Enter the number of tickets you want to book: '))
                                        f=input('Enter the date of journey in the format DDMMYYYY:')
                                        L.append(f)
                                        li={}
                                        if len(f)==8:
                                            if f.isdigit():                                            
                                                for i in range(e):                                                
                                                    g=input("Enter Passenger's Name:")
                                                    h=input("Enter Passenger's Age:")
                                                    li[i]=[g,h]
                                                try:
                                                    j=int(input('Press 1 to Confirm Booking: '))
                                                    if j==1:
                                                        L.append(li)
                                                        print('Following are the detailes of your booked ticket(s):')
                                                        pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                        loc=['Delhi             Lucknow',
                                                             'Lucknow            Delhi',
                                                             'Delhi             Amritsar',
                                                             'Amritsar           Delhi']
                                                        fa=[1200,1200,1000,1000]
                                                        if L[0]==1:
                                                            y=fa[L[1]-1]*1.3
                                                        elif L[0]==2 or L[0]==3:
                                                            y=fa[L[1]-1]*1.15
                                                        else:
                                                            y=fa[L[1]-1]
                                                        print('Origin          Destination            Seat Preference          Fair          Date')
                                                        print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                        print('Following are the passenger details:')
                                                        print('Name',' '*15,'Age')
                                                        for i in L[3]:
                                                            print(i,L[3][i])
                                                except ValueError:
                                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                                            
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            elif c==2:
                                print('Select your origin and destination:')
                                print('Origin          Destination             Via               Distance       Fair')
                                        
                                for i in range(len(journeys)):
                                    if journeys[i][0]=='G':
                                        print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.15)
                                    else:
                                        pass
                                try:
                                    d=int(input('Enter your Choice'))
                                    L.append(d)
                                    print('This is to finalize your Ticket Booking')
                                    try:
                                        e=int(input('Enter the number of tickets you want to book: '))
                                        f=input('Enter the date of journey in the format DDMMYYYY:')
                                        L.append(f)
                                        li={}
                                        if len(f)==8:
                                            if f.isdigit():                                            
                                                for i in range(e):                                                
                                                    g=input("Enter Passenger's Name:")
                                                    h=input("Enter Passenger's Age:")
                                                    li[i]=[g,h]
                                                try:
                                                    j=int(input('Press 1 to Confirm Booking: '))
                                                    if j==1:
                                                        L.append(li)
                                                        print('Following are the detailes of your booked ticket(s):')
                                                        pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                        loc=['Delhi             Lucknow',
                                                             'Lucknow            Delhi',
                                                             'Delhi             Amritsar',
                                                             'Amritsar           Delhi']
                                                        fa=[1200,1200,1000,1000]
                                                        if L[0]==1:
                                                            y=fa[L[1]-1]*1.3
                                                        elif L[0]==2 or L[0]==3:
                                                            y=fa[L[1]-1]*1.15
                                                        else:
                                                            y=fa[L[1]-1]
                                                        print('Origin          Destination            Seat Preference          Fair          Date')
                                                        print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                        print('Following are the passenger details:')
                                                        print('Name',' '*15,'Age')
                                                        for i in L[3]:
                                                            print(i,L[3][i])
                                                except ValueError:
                                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                                            
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                            elif c==3:
                                print('Select your origin and destination:')
                                print('Origin          Destination             Via               Distance       Fair')
                                        
                                for i in range(len(journeys)):
                                    if journeys[i][0]=='G':
                                        print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.15)
                                    else:
                                        pass
                                try:
                                    d=int(input('Enter your Choice'))
                                    L.append(d)
                                    print('This is to finalize your Ticket Booking')
                                    try:
                                        e=int(input('Enter the number of tickets you want to book: '))
                                        f=input('Enter the date of journey in the format DDMMYYYY:')
                                        L.append(f)
                                        li={}
                                        if len(f)==8:
                                            if f.isdigit():                                            
                                                for i in range(e):                                                
                                                    g=input("Enter Passenger's Name:")
                                                    h=input("Enter Passenger's Age:")
                                                    li[i]=[g,h]
                                                try:
                                                    j=int(input('Press 1 to Confirm Booking: '))
                                                    if j==1:
                                                        L.append(li)
                                                        print('Following are the detailes of your booked ticket(s):')
                                                        pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                        loc=['Delhi             Lucknow',
                                                             'Lucknow            Delhi',
                                                             'Delhi             Amritsar',
                                                             'Amritsar           Delhi']
                                                        fa=[1200,1200,1000,1000]
                                                        if L[0]==1:
                                                            y=fa[L[1]-1]*1.3
                                                        elif L[0]==2 or L[0]==3:
                                                            y=fa[L[1]-1]*1.15
                                                        else:
                                                            y=fa[L[1]-1]
                                                        print('Origin          Destination            Seat Preference          Fair          Date')
                                                        print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                        print('Following are the passenger details:')
                                                        print('Name',' '*15,'Age')
                                                        for i in L[3]:
                                                            print(i,L[3][i])
                                                except ValueError:
                                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                                            
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                            elif c==4:
                                print('Select your origin and destination:')
                                print('Origin          Destination             Via               Distance       Fair')
                                        
                                for i in range(len(journeys)):
                                    if journeys[i][0]=='G':
                                        print(i-1,'.',journeys[i][1],journeys[i][2],'       ',journeys[i][3])
                                    else:
                                        pass
                                try:
                                    d=int(input('Enter your Choice'))
                                    L.append(d)
                                    print('This is to finalize your Ticket Booking')
                                    try:
                                        e=int(input('Enter the number of tickets you want to book: '))
                                        f=input('Enter the date of journey in the format DDMMYYYY:')
                                        L.append(f)
                                        li={}
                                        if len(f)==8:
                                            
                                            if f.isdigit():                                            
                                                for i in range(e):                                                
                                                    g=input("Enter Passenger's Name:")
                                                    h=input("Enter Passenger's Age:")
                                                    li[i]=[g,h]
                                                try:
                                                    j=int(input('Press 1 to Confirm Booking: '))
                                                    if j==1:
                                                        L.append(li)
                                                        print('Following are the detailes of your booked ticket(s):')
                                                        pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                        loc=['Delhi             Lucknow',
                                                             'Lucknow            Delhi',
                                                             'Delhi             Amritsar',
                                                             'Amritsar           Delhi']
                                                        fa=[1200,1200,1000,1000]
                                                        if L[0]==1:
                                                            y=fa[L[1]-1]*1.3
                                                        elif L[0]==2 or L[0]==3:
                                                            y=fa[L[1]-1]*1.15
                                                        else:
                                                            y=fa[L[1]-1]
                                                        print('Origin          Destination            Seat Preference          Fair          Date')
                                                        print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                        print('Following are the passenger details:')
                                                        print('Name',' '*15,'Age')
                                                        for i in L[3]:
                                                            print(i,L[3][i])
                                                except ValueError:
                                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                                            
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                     
                    except ValueError:
                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                if b==2:
                        
                    print('Choose your comfort zone:')
                    print('1. AC+Sleeper')
                    print('2. Non AC+Sleeper')
                    print('3. AC+Non Sleeper')
                    print('4. Non AC+Non Sleeper')
                    print('5. Exit')
                    try:
                        c=int(input('Enter your Choice: '))
                        if c==1:
                            print('Select your origin and destination:')
                            print('Origin          Destination             Via               Distance       Fair')
                                    
                            for i in range(len(journeys)):
                                if journeys[i][0]=='T':
                                    print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.3)
                                else:
                                    pass
                            try:
                                d=int(input('Enter your Choice:'))
                                print('This is to finalize your Ticket Booking')
                                try:
                                    d=int(input('Enter the number of tickets you want to book: '))
                                    L.append(d)
                                    print('This is to finalize your Ticket Booking')
                                    try:
                                        e=int(input('Enter the number of tickets you want to book: '))
                                        f=input('Enter the date of journey in the format DDMMYYYY:')
                                        L.append(f)
                                        li={}
                                        if len(f)==8:
                                           
                                            if f.isdigit():                                            
                                                for i in range(e):                                                
                                                    g=input("Enter Passenger's Name:")
                                                    h=input("Enter Passenger's Age:")
                                                    li[i]=[g,h]
                                                try:
                                                    j=int(input('Press 1 to Confirm Booking: '))
                                                    if j==1:
                                                        L.append(li)
                                                        print('Following are the detailes of your booked ticket(s):')
                                                        pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                        loc=['Delhi              Agra',
                                                             'Agra               Delhi',
                                                             'Delhi             Dehradun',
                                                             'Dehradun           Delhi']
                                                        fa=[500,500,700,700]
                                                        if L[0]==1:
                                                            y=fa[L[1]-1]*1.3
                                                        elif L[0]==2 or L[0]==3:
                                                            y=fa[L[1]-1]*1.15
                                                        else:
                                                            y=fa[L[1]-1]
                                                        print('Origin          Destination            Seat Preference          Fair          Date')
                                                        print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                        print('Following are the passenger details:')
                                                        print('Name',' '*15,'Age')
                                                        for i in L[3]:
                                                            print(i,L[3][i])
                                                except ValueError:
                                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                             
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                            except ValueError:
                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                             
                        elif c==2:
                            print('Select your origin and destination:')
                            print('Origin          Destination             Via               Distance       Fair')
                                    
                            for i in range(len(journeys)):
                                if journeys[i][0]=='T':
                                    print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.15)
                                else:
                                    pass
                            try:
                                d=int(input('Enter your Choice'))
                                L.append(d)
                                print('This is to finalize your Ticket Booking')
                                try:
                                    e=int(input('Enter the number of tickets you want to book: '))
                                    f=input('Enter the date of journey in the format DDMMYYYY:')
                                    L.append(f)
                                    li={}
                                    if len(f)==8:
                                    
                                        if f.isdigit():                                            
                                            for i in range(e):                                                
                                                g=input("Enter Passenger's Name:")
                                                h=input("Enter Passenger's Age:")
                                                li[i]=[g,h]
                                            try:
                                                j=int(input('Press 1 to Confirm Booking: '))
                                                if j==1:
                                                    L.append(li)
                                                    print('Following are the detailes of your booked ticket(s):')
                                                    pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                    loc=['Delhi              Agra',
                                                         'Agra               Delhi',
                                                         'Delhi             Dehradun',
                                                         'Dehradun           Delhi']
                                                    fa=[500,500,700,700]
                                                    if L[0]==1:
                                                        y=fa[L[1]-1]*1.3
                                                    elif L[0]==2 or L[0]==3:
                                                        y=fa[L[1]-1]*1.15
                                                    else:
                                                        y=fa[L[1]-1]
                                                    print('Origin          Destination            Seat Preference          Fair          Date')
                                                    print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                    print('Following are the passenger details:')
                                                    print('Name',' '*15,'Age')
                                                    for i in L[3]:
                                                        print(i,L[3][i])
                                            except ValueError:
                                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                        
                                        
                            except ValueError:
                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                        
                        elif c==3:
                            print('Select your origin and destination:')
                            print('Origin          Destination             Via               Distance       Fair')
                                    
                            for i in range(len(journeys)):
                                if journeys[i][0]=='T':
                                    print(i-1,'.',journeys[i][1],journeys[i][2],'       ',(journeys[i][3])*1.15)
                                else:
                                    pass
                            try:
                                d=int(input('Enter your Choice'))
                                L.append(d)
                                print('This is to finalize your Ticket Booking')
                                try:
                                    e=int(input('Enter the number of tickets you want to book: '))
                                    f=input('Enter the date of journey in the format DDMMYYYY:')
                                    L.append(f)
                                    li={}
                                    if len(f)==8:
                                        
                                        if f.isdigit():                                            
                                            for i in range(e):                                                
                                                g=input("Enter Passenger's Name:")
                                                h=input("Enter Passenger's Age:")
                                                li[i]=[g,h]
                                            try:
                                                j=int(input('Press 1 to Confirm Booking: '))
                                                if j==1:
                                                    L.append(li)
                                                    print('Following are the detailes of your booked ticket(s):')
                                                    pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                    loc=['Delhi              Agra',
                                                         'Agra               Delhi',
                                                         'Delhi             Dehradun',
                                                         'Dehradun           Delhi']
                                                    fa=[500,500,700,700]
                                                    if L[0]==1:
                                                        y=fa[L[1]-1]*1.3
                                                    elif L[0]==2 or L[0]==3:
                                                        y=fa[L[1]-1]*1.15
                                                    else:
                                                        y=fa[L[1]-1]
                                                    print('Origin          Destination            Seat Preference          Fair          Date')
                                                    print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                    print('Following are the passenger details:')
                                                    print('Name',' '*15,'Age')
                                                    for i in L[3]:
                                                        print(i,L[3][i])
                                            except ValueError:
                                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                except ValueError:
                                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                        
                                        
                            except ValueError:
                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                        
                        elif c==4:
                            print('Select your origin and destination:')
                            print('Origin          Destination             Via               Distance       Fair')
                            k=1    
                            for p in range(len(journeys)):
                                
                                if journeys[p][0]=='T':
                                    print(k,'.',journeys[p][1],journeys[p][2],'       ',journeys[p][3])
                                    k+=1
                                else:
                                    pass
                            try:
                                d=int(input('Enter your Choice'))
                                L.append(d)
                                print('This is to finalize your Ticket Booking')
                                try:
                                    e=int(input('Enter the number of tickets you want to book: '))
                                    f=input('Enter the date of journey in the format DDMMYYYY:')
                                    L.append(f)
                                    li={}
                                    if len(f)==8:
                                        if f.isdigit():                                            
                                            for i in range(e):                                                
                                                g=input("Enter Passenger's Name:")
                                                h=input("Enter Passenger's Age:")
                                                li[i]=[g,h]
                                            try:
                                                j=int(input('Press 1 to Confirm Booking: '))
                                                if j==1:
                                                    L.append(li)
                                                    print('Following are the detailes of your booked ticket(s):')
                                                    pref=["AC+Sleeper","Non AC+Sleeper","AC+Non Sleeper","Non AC+Non Sleeper"]
                                                    loc=['Delhi              Agra',
                                                         'Agra               Delhi',
                                                         'Delhi             Dehradun',
                                                         'Dehradun           Delhi']
                                                    fa=[500,500,700,700]
                                                        
                                                    if L[0]==1:
                                                        y=fa[L[1]-1]*1.3
                                                    elif L[0]==2 or L[0]==3:
                                                        y=fa[L[1]-1]*1.15
                                                    else:
                                                        y=fa[L[1]-1]
                                                    
                                                    print('Origin          Destination            Seat Preference          Fair          Date')
                                                    print(loc[L[1]-1],' '*11,pref[(L[0])],' '*10,y,' '*10,L[2])
                                                    print('Following are the passenger details:')
                                                    print('Name',' '*15,'Age')
                                                    for i in L[3]:
                                                        print(i,L[3][i])
                                            except ValueError:
                                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                except ValueError:
                                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                            
                                            
                            except ValueError:
                                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                     
                    except ValueError:
                        print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                                    
                                    
                                        
                elif b==3:
                    main()
                else:
                    print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
                    
                
            except ValueError:
                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
        
        
                    
            
        print()
        print('Busses are available for the following journeys:')
        print()
        print('Origin          Destination             Via               Distance')
        for i in range(len(journeys)):
            print(journeys[i][1],journeys[i][2])
        print('Choose from the options given below:')
        print('1. Proceed to Booking')
        print('2. Exit')
        try:
            a=int(input('Enter your choice:'))
            if a==1:
                proceed()
            elif a==2:
                break
            else:
                print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
        except ValueError:
            print(cll.Fore.RED+'Please Enter your choice Carefully!!!'+cll.Style.RESET_ALL)
main()
    
    
