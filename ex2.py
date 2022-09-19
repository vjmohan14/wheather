print("************WELCOME TO TICKETNEW**************")
first_class=180
second_class=150
third_class=60
tax=40
def location():
    print("**************LOCATION******************")
    print("choose your location") 
    print("Anna nagar")
    print("Koyambedu")
    print("Villivakam")
    print("Saidapet")
    print("pallavaram")    

def language():
    print("*************LANGUAGE*****************")
    print("choose your language")
    print("Tamil")
    print("English")
    print("Telugu")
    print("Hindi")
def theater():
    print("***********THEATER********************")
    print("which theater do you want to watch movie")
    print("Sangam Cinemas")
    print("Devicineplex")
    print("Kamala Cinemas")
    print("EGA Cinemas")
    print("kasi Theater")
def movie():
    print("********NOW STREAMING*****************")
    print("Vendhu Thanindhathu kaadu")
    print("Mersal")
    print("Billa")
    print("cobra") 
def screen():
    print("************SCREEN****************")
    print("which screen do you want to watch")
    print("screen1")
    print("screen2")
    print("screen3")  
def ticket(): 
    print("***********TICKET STATUS*********")
    print("choose your ticket class")
    print("first class")
    print("second class")
    print("third class")
def timing():
    print(f"Enjoy your movie at: {x}")
#choose location
print("choose your location") 
print("Anna nagar")
print("Koyambedu")
print("Villivakam")
print("Saidapet")
print("pallavaram")    
loc=input("Enter your location:").lower().strip()    
if loc=="anna nagar":
    language()
elif loc=="koyambedu":
    language()
elif loc=="villivakam":
    language()
elif loc=="saidapet":
    language()
elif loc=="pallavaram":
    language()  
#language    
lan=input("Enter your language:").lower().strip()
if lan=="tamil":
    theater()
elif lan=="english":
    theater()
elif lan=="telugu":
    theater()
elif lan=="hindi":
    theater()
#theater name    
the=input("Enter the theater name:").lower().strip()
if the=="sangam cinemas":
    movie()
elif the=="devicineplex":
    movie()
elif the=="kamala cinemas":
    movie()
elif the=="ega cinemas":
    movie()
elif the=="kasi theater":
    movie() 
#movie name     
mov=input("Enter the movie name you want to watch:").lower().strip()
if mov=="vendhu thanindhathu kaadu":
    screen()
elif mov=="mersal":
    screen()
elif mov=="billa":
    screen()
elif mov=="cobra":
    screen()                  
scr=input("Enter the screen no do you want to watch:").lower().strip()
if scr=="screen1":         
    tim=int(input("Enter your screen no:")) 
    time1={"1":"10.00 AM-1.00 PM",
       "2":"1.10 PM-4.10 PM",
       "3":"4.20 PM-7.20 PM",
       "4":"7.30 PM-10.30 PM"
    }
if scr=="screen2":
    tim=int(input("Enter your screen no:"))
    time2={"1":"10.15 AM-1.15 PM",
       "2":"1.25 PM-4.25 PM",
       "3":"4.35 PM-7.35 PM",
       "4":"7.45 PM-10.45 PM"
}
if scr=="screen3":
    tim=int(input("Enter your screen no:"))
    time3={"1":"10.30 AM-1.30 PM",
       "2":"1.40 PM-4.40 PM",
       "3":"4.50 PM-7.50 PM",
       "4":"8.00 PM-10.45 PM"
}
if tim==1:
    print("choose your time slot you want")
    print(time1)
    tim_sl=input("Enter the slot:")
    x=time1[tim_sl]
    timing()
    ticket()
elif tim==2:
    print("choose your time slot you want")
    print(time2)
    tim_sl=input("Enter the slot:")
    x=time2[tim_sl]
    timing()
    ticket()  
elif tim==3:
    print("choose your time slot you want")
    print(time3)
    tim_sl=input("Enter the slot:")
    x=time3[tim_sl]
    timing()
    ticket()
cla=input("Enter the class status:")
if cla=="first class":
    tic=int(input("Enter the number of ticket do you want:"))
    cost=tic*first_class+tax*tic
    print(f"Your ticket cost is Rs: {cost} (including GST)") 
    print(f"Enjoy your movie in {the} at: {x}")   
elif cla=="second class":
    tic=int(input("Enter the number of ticket do you want:"))
    cost=tic*second_class+tax*tic
    print(f"Your ticket cost is Rs: {cost} (including GST)")
    print(f"Enjoy your movie in: {the} at: {x}")    
elif cla=="third class":
    tic=int(input("Enter the number of ticket do you want:"))
    cost=tic*third_class+tax*tic
    print(f"Your ticket cost is Rs: {cost} (including GST)")
    print(f"Enjoy your movie in: {the} at: {x}")
