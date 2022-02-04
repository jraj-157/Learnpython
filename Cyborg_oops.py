class Bus:
    def __init__(self,Conductor_Name,Maximum_speed_limit_in_kmph,maxcap,i1):
        self.name = Conductor_Name
        self.maxsp = Maximum_speed_limit_in_kmph
        self.maxcap = maxcap
        self.income = i1
      # il = ticket fare per km in rs
# assuming all passenger will stop at station '0' 20km away from n station
# assuming the bus will take 30 minutes to reach a station 
Bus1 = Bus("Shyam",60,103,20)
# a
a = int(input("Enter no. of passengers in station A:"))

class station_A(Bus):
    t1_mints = 30
    def BusBroad(a):
        
        if ( a <= 103 ):
               print(f"Passengers picked up from A " + str(a))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if(103-a>0):
         Bus1.maxcap = 103 - a
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(t1_mints*1)+" mints for the bus filled")
    else:
            print(str(t1_mints*1)+" mints for the bus has no seat")
    if(103-a>0):
     i1 = a * 14 * 20 * 20
    else:
     i1 = 103*14*20*20
    def Who_cant_seat(a):
        if (a>103):
            print(str(a-103)+" passenger cannot get seat")
        else:
            pass

    print("The income till now  "+str(i1))
    

station_A.Who_cant_seat(a)       
station_A.BusBroad(a)
print("The remaining Seats are  " + str(Bus1.maxcap))

# b

b = int(input("Enter no. of passengers in station B:"))

class station_B(station_A):
    
    
    def BusBroad(b):
        if ((a+b) <= 103):
            print(f"Passengers picked up from B " + str(b))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if(103-(a+b)>0):
         Bus1.maxcap = 103 - (a+b)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*2)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*2)+" mintsfor the bus has no seat")
    if(103-(a+b)>=0):
        i1 = station_A.i1 + b * 13 * 20 * 20
    elif(a>=103):
        i1= station_A.i1 
    else:
        i1 = station_A.i1 + (103-a) * 13 * 20 * 20
    def Who_cant_seat(b):
         if((a+b)>103):
            print(str((a+b)-103)+" passenger cannot get seat")
         else:
            pass
        


        
    print("The income till now  "+str(i1))
    

station_B.Who_cant_seat(b)     
station_B.BusBroad(b)
print("The remaining Seats are  " + str(Bus1.maxcap))

# c
c = int(input("Enter no. of passengers in station C:"))

class station_C(station_B):
    
    t1_mints=station_A.t1_mints*3
    def BusBroad(c):
        if ((a+b+c) <= 103):
             print(f"Passengers picked up from c " + str(c))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c)<103):
         Bus1.maxcap = 103 - (a+b+c)
        else:
            Bus1.maxcap = 0 
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*3)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*3)+" mints for the bus has no seat")
    if(103-(a+b+c)>=0) :
        i1 = station_B.i1 + c * 12 * 20 * 20
    elif((a+b)>=103):
        i1= station_B.i1
    else:
        i1 = station_B.i1 + (103-a-b) * 12 * 20 * 20
    def Who_cant_seat(c):
        if (a+b+c)>103:
            print(str((a+b+c)-103)+" passenger cannot get seat")
        else:
            pass
        
    print("The income till now  "+str(i1))
    

        
    
station_C.Who_cant_seat(c)
station_C.BusBroad(c)
print("The remaining Seats are  " + str(Bus1.maxcap))
# d
d = int(input("Enter no. of passengers in station D:"))

class station_D(station_C):
    t1_mints=station_A.t1_mints*4
    def BusBroad(d):
        if ((a+b+c+d) <= 103):
             print(f"Passengers picked up from c " + str(d))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d)<103):
         Bus1.maxcap = 103 - (a+b+c+d)
        else:
            Bus1.maxcap = 0 
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*4)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*4)+" mints for the bus has no seat")
    if(103-(a+b+c+d)>=0):
         i1 = station_C.i1 + d * 11 * 20 * 20
    elif((a+b+c)>=103):
         i1= station_C.i1
    else:
        i1 = station_C.i1 + (103-(a+b+c))*11*20*20
    def Who_cant_seat(c):
        if (a+b+c+d)>103:
            print(str((a+b+c+d)-103)+" passenger cannot get seat")
        else:
            pass
    
    print("The income till now  "+str(i1))
    
        
    
station_D.Who_cant_seat(d)
station_D.BusBroad(d)
print("The remaining Seats are  " + str(Bus1.maxcap))
# e
e = int(input("Enter no. of passengers in station E:"))

class station_E(station_D):
    t1_mints=station_A.t1_mints*5
    def BusBroad(e):
        if ((a+b+c+d+e) <= 103):
             print(f"Passengers picked up from c " + str(e))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e)
        else:
            Bus1.maxcap = 0 
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*5)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*5)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e)>=0) :
         i1 = station_D.i1 + e * 10 * 20 * 20
    elif((a+b+c+d)>=103):
         i1= station_D.i1
    else:
        i1 = station_D.i1 + (103-(a+b+c+d))*10*20*20
    def Who_cant_seat(e):
        if (a+b+c+d+e)>103:
            print(str((a+b+c+d+e)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_E.Who_cant_seat(e)
station_E.BusBroad(e)
print("The remaining Seats are  " + str(Bus1.maxcap))
# f

f = int(input("Enter no. of passengers in station F:"))

class station_F(station_E):
    t1_mints=station_A.t1_mints*6
    def BusBroad(f):
        if ((a+b+c+d+e+f) <= 103):
             print(f"Passengers picked up from c " + str(e))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*6)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*6)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f)>=0) :
         i1 = station_E.i1 + f * 9 * 20 * 20
    elif((a+b+c+d+e)>=103):
         i1= station_E.i1
    else:
        i1 = station_E.i1 + (103-(a+b+c+d+e))* 9 * 20 * 20
    def Who_cant_seat(f):
        if (a+b+c+d+e+f)>103:
            print(str((a+b+c+d+e+f)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_F.Who_cant_seat(f)
station_F.BusBroad(f)
print("The remaining Seats are  " + str(Bus1.maxcap))

# g

g = int(input("Enter no. of passengers in station G:"))

class station_G(station_F):
    
    t1_mints=station_A.t1_mints*7
    def BusBroad(g):
        if ((a+b+c+d+e+f+g) <= 103):
             print(f"Passengers picked up from c " + str(e))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*7)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*7)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g)>=0) :
         i1 = station_F.i1 + g * 8 * 20 * 20
    elif((a+b+c+d+e+f)>=103):
         i1= station_F.i1
    else:
        i1 = station_F.i1 + (103-(a+b+c+d+e+f))*8*20*20
    def Who_cant_seat(g):
        if (a+b+c+d+e+f+g)>103:
            print(str((a+b+c+d+e+f+g)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_G.Who_cant_seat(g)
station_G.BusBroad(g)
print("The remaining Seats are  " + str(Bus1.maxcap))

# h

h = int(input("Enter no. of passengers in station H:"))

class station_H(station_G):
    t1_mints=station_A.t1_mints*8
    def BusBroad(h):
        if ((a+b+c+d+e+f+g+h) <= 103):
             print(f"Passengers picked up from c " + str(e))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*8)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*8)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h)>=0) :
         i1 = station_G.i1 + h * 7 * 20 * 20
    elif((a+b+c+d+e+f+g)>=103):
         i1= station_G.i1
    else:
        i1 = station_G.i1 + (103-(a+b+c+d+e+f+g))*7*20*20
    def Who_cant_seat(h):
        if (a+b+c+d+e+f+g+h)>103:
            print(str((a+b+c+d+e+f+g+h)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_H.Who_cant_seat(h)
station_H.BusBroad(h)
print("The remaining Seats are  " + str(Bus1.maxcap))

# i

i = int(input("Enter no. of passengers in station I:"))

class station_I(station_H):
    t1_mints=station_A.t1_mints*9
    def BusBroad(i):
        if ((a+b+c+d+e+f+g+h+i) <= 103):
             print(f"Passengers picked up from c " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*9)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*9)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i)>=0) :
         i1 = station_H.i1 + i * 6 * 20 * 20
    elif((a+b+c+d+e+f+g)>=103):
         i1= station_H.i1
    else:
        i1 = station_H.i1 + (103-(a+b+c+d+e+f+g+h))*6*20*20
    def Who_cant_seat(i):
        if (a+b+c+d+e+f+g+h+i)>103:
            print(str((a+b+c+d+e+f+g+h+i)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_I.Who_cant_seat(i)
station_I.BusBroad(i)
print("The remaining Seats are  " + str(Bus1.maxcap))

# j

j = int(input("Enter no. of passengers in station J:"))

class station_J(station_I):
    t1_mints=station_A.t1_mints*10
    def BusBroad(i):
        if ((a+b+c+d+e+f+g+h+i) <= 103):
             print(f"Passengers picked up from c " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i+j)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i+j)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*10)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*10)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i+j)>=0) :
         i1 = station_I.i1 + j * 5 * 20 * 20
    elif((a+b+c+d+e+f+g+i)>=103):
         i1= station_I.i1
    else:
        i1 = station_I.i1 + (103-(a+b+c+d+e+f+g+h+i))*5*20*20
    def Who_cant_seat(j):
        if (a+b+c+d+e+f+g+h+i+j)>103:
            print(str((a+b+c+d+e+f+g+h+i+j)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_J.Who_cant_seat(j)
station_J.BusBroad(j)
print("The remaining Seats are  " + str(Bus1.maxcap))

# k
k = int(input("Enter no. of passengers in station K:"))

class station_K(station_J):
    t1_mints=station_A.t1_mints*11
    def BusBroad(k):
        if ((a+b+c+d+e+f+g+h+i+j+k) <= 103):
             print(f"Passengers picked up from c " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i+j+k)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i+j+k)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*11)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*11)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i+j+k)>=0) :
         i1 = station_J.i1 + k * 4 * 20 * 20
    elif((a+b+c+d+e+f+g+i+j)>=103):
         i1= station_J.i1
    else:
        i1 = station_J.i1 + (103-(a+b+c+d+e+f+g+h+i+j))*4*20*20
    def Who_cant_seat(k):
        if (a+b+c+d+e+f+g+h+i+j+k)>103:
            print(str((a+b+c+d+e+f+g+h+i+j+k)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_K.Who_cant_seat(k)
station_K.BusBroad(k)
print("The remaining Seats are  " + str(Bus1.maxcap))

# l
l = int(input("Enter no. of passengers in station L:"))
class station_L(station_K):
    t1_mints=station_A.t1_mints*12
    def BusBroad(k):
        if ((a+b+c+d+e+f+g+h+i+j+k+l) <= 103):
             print(f"Passengers picked up from c " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i+j+k+l)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i+j+k+l)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*12)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*12)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i+j+k+l)>=0) :
         i1 = station_K.i1 + l * 3 * 20 * 20
    elif((a+b+c+d+e+f+g+i+j+k)>=103):
         i1= station_K.i1
    else:
        i1 = station_K.i1 + (103-(a+b+c+d+e+f+g+h+i+j+k))*3*20*20
    def Who_cant_seat(l):
        if (a+b+c+d+e+f+g+h+i+j+k+l)>103:
            print(str((a+b+c+d+e+f+g+h+i+j+k+l)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_L.Who_cant_seat(l)
station_L.BusBroad(l)
print("The remaining Seats are  " + str(Bus1.maxcap))
# m
m = int(input("Enter no. of passengers in station M:"))
class station_M(station_L):
    t1_mints=station_A.t1_mints*13
    def BusBroad(m):
        if ((a+b+c+d+e+f+g+h+i+j+k+l+m) <= 103):
             print(f"Passengers picked up from c " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i+j+k+l+m)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i+j+k+l+m)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
        print(str(station_A.t1_mints*13)+" mints for the bus filled")
    else:
        print(str(station_A.t1_mints*13)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i+j+k+l+m)>=0) :
         i1 = station_L.i1 + m * 2 * 20 * 20
    elif((a+b+c+d+e+f+g+i+j+k+l)>=103):
         i1= station_L.i1
    else:
        i1 = station_L.i1 + (103-(a+b+c+d+e+f+g+h+i+j+k+l))*2*20*20
    def Who_cant_seat(m):
        if (a+b+c+d+e+f+g+h+i+j+k+l+m)>103:
            print(str((a+b+c+d+e+f+g+h+i+j+k+l+m)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_M.Who_cant_seat(m)
station_M.BusBroad(m)
print("The remaining Seats are  " + str(Bus1.maxcap))
# n
n = int(input("Enter no. of passengers in station N:"))

class station_N(station_M):
    t1_mints=station_A.t1_mints*14
    def BusBroad(n):
        if ((a+b+c+d+e+f+g+h+i+j+k+l+m+n) <= 103):
             print(f"Passengers picked up from n " + str(i))
        else:
            print("Max capacity reached all 103 seats are fulled")
        if ((a+b+c+d+e+f+g+h+i+j+k+l+m+n)<103):
         Bus1.maxcap = 103 - (a+b+c+d+e+f+g+h+i+j+k+l+m+n)
        else:
            Bus1.maxcap = 0
    if Bus1.maxcap != 0:
            print(str(station_A.t1_mints*14)+" mints for the bus filled")
    else:
            print(str(station_A.t1_mints*14)+" mints for the bus has no seat")
    if(103-(a+b+c+d+e+f+g+h+i+j+k+l+m+n)>=0) :
         i1 = station_M.i1 + n * 1 * 20 * 20
    else:
        i1 = station_M.i1 
    def Who_cant_seat(n):
        if (a+b+c+d+e+f+g+h+i+j+k+l+m+n)>103:
            print(str((a+b+c+d+e+f+g+h+i+j+k+l+m+n)-103)+" passenger cannot get seat")
        else:
            pass
    print("The income till now  "+str(i1))
    
        
    
station_N.Who_cant_seat(n)
station_N.BusBroad(n)
print("The remaining Seats are  " + str(Bus1.maxcap))
class total_income(station_A):
    conductor_income = station_N.i1*(0.3) # Assuming conductor gets 30% of total income 
print(Bus1.name+ " got "+ str(total_income.conductor_income))