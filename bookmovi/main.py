from tkinter import * 
class moviephase1():
    
    print('Hi! Admin. Please fix the row and columns of the seating hall in cinema.')
    
        
    def welcome(self):
        print('====================================')
        print('            MOVIE MASALA            ')
        print('====================================')
        print('              ^ ^                   ')
        print("            '(o o)'                 ")
        print('               Y                    ')
        print("             _/|\_                  ")
        print("               |                    ")
        print("             _/ \_                  ")
        print("HELLO!!!  Welcome to movie ticket booking: ")
        print('Are you a USER or a ADMIN')
        print('For USER press:1')
        print('For ADMIN press:2')
        key=int(input('Enter the no.:'))
        if key==1:
            self.user_login()
        elif key==2:
            self.statistics()
        else:
            print('Choose only 1 or 2')
            self.welcome()
    def user_login(self):
        print('Please 1)login or 2)create a new account')
        Already_a_user=input('Already a user?')
        if Already_a_user=='yes':
            name=input('Enter you username:')
            password=input('Enter you password:')
            print('Welcome back', name)
            self.city()
        elif Already_a_user=='no':
            print("Let's create a new account ")
            name=input('Enter you username:')
            password=input('Enter you password:')
            phno=int(input('Enter your phone number:'))
            otp=int(input('Enter the otp sent to your phone number:'))
            print('Account created successfully!!')
            self.city()
        else:
            print('Please submit your response in yes or no.')
            self.user_login()
        
    
            
    def city(self):
        print("Please, select your city:")
        print("1:Mumbai")
        print("2:Hyderabad ")
        print("3:Delhi ")
        print("4:Chennai")
        print("5:Kolkata ")
        print("6:Vishakhapatnam")
        print("7:Pune ")
        print("8:Gurgaon ")
        print("9:Noida ")
        print("10:Indore")
        print("11:Gwalior ")
        print("12:Mysore ")
        print("13:Jaipur")
        print("14:Allahabad ")
        print("15: Ahemdabad ")
        city_dict={1:"Mumbai", 2:'Hyderabad' , 3:'Delhi', 4:'Chennai', 5:'Kolkata', 6:'Vishakhapatnam',7:'Pune',8:'Gurgaon',9:'Noida',10:'Indore',11:'Gwalior',12:'Mysore',13:'Jaipur', 14:'Allahabad', 15:'Ahemdabad' }
        place = int(input("Choose your City number: "))
        self.place=place
    
        if place in range(1,16):
            self.center()

        else:
            print("Please select from the above options only")
            self.city()

        
        
    def center(self):
        print("Which theater do you wish to see the movie? ")
        print("1:Inox")
        print("2:Icon")
        print("3:pvr")
        print("4:back")
        a = int(input("choose your option: "))
        if a==1 or a==2 or a==3:
            self.name_movie()
            return 0
        elif a==4:
            self.city()
        else:
            print("Please select from the above options only")
            self.center()


    
        



    def name_movie(self):
         
        city_dict={1:"Mumbai", 2:'Hyderabad' , 3:'Delhi', 4:'Chennai', 5:'Kolkata', 6:'Vishakhapatnam',7:'Pune',8:'Gurgaon',9:'Noida',10:'Indore',11:'Gwalior',12:'Mysore',13:'Jaipur', 14:'Allahabad', 15:'Ahemdabad' }
        
        if self.place==1 or self.place==3 or self.place==5 or self.place==7  or self.place==8 or self.place==9 or self.place==10 or self.place==11 or self.place==13 or self.place==14 or self.place==15:
            print('The following movies are playing in', city_dict[self.place] )
            print("which movie do you want to watch?")
            print("1: uppena ")        
            print("2: master ")
            print("3: love aaj kal 2")
            print("4: dabang 4")
            print("5: Lost in space ")
            print("6: Witcher ")
            print("7: xyz")
            print("8: Back")
            movie = int(input("choose your movie: "))
            self.movie=movie
            if movie == 8:
    
                self.center()
                
            else:
                self.theater()
        if self.place==2 or self.place==6:
            print('The following movies are playing in', city_dict[self.place] )
            print("which movie do you want to watch?")
            print("1: Uppena ")        
            print("2: Master ")
            print("3: love aaj kal 2")
            print("4: Check")
            print("5: Naandhi")
            print("6: Angulika ")
            
            print("7: back")
            movie = int(input("choose your movie: "))
            self.movie=movie
            if movie == 7:
    
                self.center()
                
            else:
                self.theater()
        if self.place==12 or self.place==4:
            print('The following movies are playing in', city_dict[self.place] )
            print("which movie do you want to watch?")
            print("1: Pogaru ")        
            print("2: Preman ")
            print("3: Kushka")
            print("4: Salt")
            print("5: Master ")
            print("6: Centha ")
            print("7: Chakra")
            print("8: back")
            movie = int(input("choose your movie: "))
            self.movie=movie
            if movie == 8:
    
                self.center()
                self.theater()
                return 0
            else:
                self.theater()
        
        
        
        
    def theater(self):
        print("Which screen do you want to watch:")
        print("1:SCREEN 1")
        print("2:SCREEN 2")
        print("3:SCREEN 3")
        print("4:Back")
        a = int(input("choose your screen: "))
        
        
        if a==1 or a==2 or a==3:
            self.proceed()
        elif a==4:
            self.name_movie()
        else:
            print('Wrong choice: Choose from the given options only')
            self.theater()
    
    def proceed(self):
        print( 'For the selected movie, proceed and select one of the given options:')
        print('1: Show the seats')
        print('2: Buy a ticket')
        print('Only for Admin:')
        print('3: Statistics')
        print('4: Show booked ticket user info')
        select_option=int(input('type your response:'))
        if select_option==1:
            self.show_the_seat()
        elif select_option==2:
            self.buy_the_ticket()
        elif select_option==3:
            self.statistics()
        elif select_option==4:
            self.User_info()
        else:
            print('Choose only the above options.')
            self.proceed()
            
            
    global dictionary_of_users
    dictionary_of_users={}
    global user 
    user=0 
    global total_income
    total_income=0
    global number_of_rows
    number_of_rows= int(input('The no. of rows:'))
    global number_of_columns
    number_of_columns=int(input('The no. of columns: '))
    global cinema
    cinema = []
    for j in range(1,number_of_rows+1):
        column = []
        column.append(j)
        if number_of_columns<11:
            for i in range(1,number_of_columns+1):
        
                column.append('S')
            cinema.append(column)
        elif number_of_columns>10:
            for i in range(1,10):
                column.append('S')
            for i in range(10,number_of_columns+1):
                column.append('S ')
            cinema.append(column)
    def show_the_seat(self):
        global number_of_rows
        global number_of_columns
        global cinema

        print('  ', end='')
        for k in range(1 , number_of_columns+1):
            self.k=k
    
            print(k , end=' ')
        print(end='\n')   
        

        for column in cinema:
            for item in column:
                
                print(item, end = " ")
            print()
        
            
            
        print('S is for vaccant seat and B is for booked ')
        print('Do you want to \n 1:book the ticket \n  Press any key:Go back')
        answer=int(input())
        if answer==1:
            self.buy_the_ticket()
        else:
            self.proceed()
       
    def buy_the_ticket(self):
        global cinema
        global user
        global dictionary_of_users 
        ticket_number=0
        
        row=int(input('Which row no. you wish to book the ticket?:'))
        self.row=row
        column=int(input('Which column no. you wish to book the ticket?:'))
        self.column=column
        if cinema[row-1][column]=='B':
            print('Sorry, that seat has been booked. We encourage you to pick another seat')
            self.buy_the_ticket()
            return 0
        elif row<number_of_rows+1 and column<number_of_columns+1:
            if number_of_rows*number_of_columns<60:
                price=int(10)
                self.price=price
                print('The price of ticket is: $10')
                    
            elif number_of_rows*number_of_columns>60:
                if number_of_rows/2<row:
                    price=int(8)
                    self.price=price
                    print('The price of ticket is: $8')
                        
                else:
                    price=int(10)
                    self.price=price
                    print('The price of ticket is: $10')
                       
        else:
            print('The choosen row/column is out of range')
                
        print('Do you want to book the ticket?')
        print('1: Yes')
        print('2: Select another seat')
        answer=int(input('Press 1 or 2:'))
        if answer==1:
            user+=1
            user_dict={}
            print('Please provide the following information:')
            user_dict['User']='user'+str(user) 
            user_dict['Name']=input('Name:')
            user_dict['Age']=input('Age:')
            user_dict['Gender']=input('Gender:')
            user_dict['Phone_number']=input('Phone no.:')
            key=str(row)+','+str(column)
            dictionary_of_users[key]=user_dict
            self.payment()
        elif answer==2:
            self.buy_the_ticket()
        
   
    def payment(self):
        
        global total_income
        print('You are paying to book ticket of row no.', self.row, 'and column no.', self.column, 'for the price $' + str(self.price) )
        print('The following payment options are available:')
        print('1: credit card')
        print('2: debit card')
        print('3: UPI')
        print('4: Back to seat selection')
        payment_opt=int(input('Enter the no.:'))
        if payment_opt==1 or payment_opt==2 or payment_opt==3:
            card_number=int(input('Enter the card no.:'))
            print('Payment is success full for row no.', self.row, 'and column no.', self.column, 'for the price $' + str(self.price))
            cinema[self.row-1][self.column] = 'B'
            total_income=total_income+self.price 
            

            root=Tk()
            root.title('Movie Masala')
            root.geometry('350x200')

            label = Label(root , text ="Ticket is booked!! Enjoy your movie.") 
            label.pack()

            root.mainloop()

            
    def statistics(self):
        global number_of_rows
        global number_of_columns
        print('ALERT!! Access only to admin.')
        password=input('enter admin password:')
        if password=='admin001':
            print('Welcome admin')
            print('The no. of purchased tickets are:', user)
            print ('The percentage of tickets booked is', user/(number_of_rows*number_of_columns)*100)
            print('The total revenue generated is:' , total_income)
            if number_of_rows*number_of_columns<60:
                print('The total expected income is: $'+str(number_of_rows*number_of_columns*10)) 
            else:
                print('The total expected income is: $' + str ((((number_of_rows//2)*10)+(number_of_rows-(number_of_rows//2))*8)*number_of_columns))
            
        else:
            print("wrong password. Access denied")
            self.statistics()
    
        
        
        
    def User_info(self):
        print('ALERT!! Access only to admin.')
        password=input('enter admin password:')
        if password=='admin001':
            print('Welcome admin')
            row_no=int(input('Enter the row no.:'))
            column_no=int(input('Enter the column no.:'))
            if cinema[row_no-1][column_no] == 'B':
                print(dictionary_of_users[str(row_no)+','+str(column_no)])
            else:
                print('The seat is not booked yet')
        else:
            print("wrong password. Access denied")
            self.User_info()
            
book1=moviephase1()
book1.welcome()
    