class Movie:
    
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.seats = []
        self.Total_seat = self.row*self.col
        self.user_booking_details = {}
        self.ticket_price = " "

        for i in range(0,self.row+1):
            self.seats.append([])
        for i in range(0,self.row+1):
            for j in range(0,self.col+1):
                self.seats[i].append(j)
                self.seats[i][j]=False
        
    def show_seats(self):
        print('Cinema: \n')
            
        for i in range(0,self.row+1):
            for j in range(0,self.col+1):
                
                if self.seats[i][j] == False:
                    self.seats[i][j]="S"
                elif self.seats[i][j] == True:
                    self.seats[i][j]="B"                       
            
        for i in range(0,self.row+1):
            for j in range(0,self.col+1):
                
                if i==0:
                    if j==1:
                        for x in range(0,self.col+1):
                            if x==0:
                                print(" ",end=' ')
                            else:
                                print(x,end=' ') 
                else:
                    if j==0:
                        print(i,end=' ')
                    else:
                        print(self.seats[i][j],end=' ')
            print()
        print()
        
    def buy_a_ticket(self,nth_row,nth_col):
        self.nth_row = nth_row
        self.nth_col = nth_col
        self.id_of_seat = self.nth_row*self.nth_col
        
        choice_yes_no = {1:'Yes',2:'No'}
        
        if self.Total_seat <= 60:
            self.ticket_price = "10$"
            print("The price of seat of row",self.nth_row," and column",self.nth_col, " is:", self.ticket_price)
            
        else:
            if self.Total_seat > 60:
                first_half = self.row//2

                if self.nth_row <= first_half:
                    self.ticket_price = "10$"
                    print("The price of seat of row",self.nth_row," and column",self.nth_col, " is:", self.ticket_price)
                else:
                    self.ticket_price = "8$"
                    print("The price of seat of row",self.nth_row," and column",self.nth_col, " is:", self.ticket_price)

        print("Do you want to book ?")
        
        for value in choice_yes_no:
            print(str(value)+'.',choice_yes_no[value])
            
        confirmation = int(input())
        
        if confirmation == 1:
            Details = {}
            Details['Name'] = input("Please enter your name: ")
            Details['Gender'] = input("Please enter your gender: ")
            Details['Age'] = input("Please enter your age: ")
            Details['Ticket Price'] = self.ticket_price
            Details['Phone No.'] = int(input("Please enter your mobile no.: "))
            if self.seats[self.nth_row][self.nth_col] == "S":
                self.seats[self.nth_row][self.nth_col]="B"
                self.user_booking_details[self.id_of_seat]=Details
                print("\n Booked Successfully")

            elif self.seats[self.nth_row][self.nth_col] == "B":
                print("Selected Seat Already Booked \nPlease select another seat")
                
                
    def statistics(self):
        Booked_seat = 0
        for i in range(0,self.row+1):
            for j in range(0,self.col+1):
                if self.seats[i][j]=="B":
                    Booked_seat+=1
        self.current_income = Movie.set_current_income(self.Total_seat,self.row,self.col,self.seats)          
        self.percentage = Movie.find_percentage(Booked_seat,self.Total_seat)
        self.format_float_percentage = "{:.2f}".format(self.percentage)

        
        self.Total_income = Movie.set_total_income(self.Total_seat,self.row,self.col)

        values = {"Number of purchased tickets": Booked_seat,"Percentage": str(self.format_float_percentage)+"%",
                  "Current income": str(self.current_income)+"$","Total income": str(self.Total_income)+"$"}
        print()
        for value in values:
            print(str(value)+':',values[value])
        print()
        

    def show_details(self,nth_row,nth_col):
        self.nth_row = nth_row
        self.nth_col = nth_col
        self.id_of_seat = self.nth_row*self.nth_col
        print()
        if self.seats[self.nth_row][self.nth_col] == "B":
        
            for details_of_person in self.user_booking_details[self.id_of_seat].items():

                print(details_of_person[0],": --> ",details_of_person[1])
        else:
            print("Details not found because there is no booking of row",nth_row,"and column",nth_col)
            
        print() 
    
        
    @staticmethod
    def find_percentage(Booked_seat,Total_seat):
        percentage = (Booked_seat/Total_seat)*100
        return percentage
    
    def set_current_income(Total_seat,row,col,seats):
        current_income_count = []
        
        if Total_seat <= 60:
            for i in range(0,row+1):
                for j in range(0,col+1):
                    if seats[i][j]=="B":
                        current_income_count.append(10)
        else:
            if Total_seat > 60:
                first_half = row // 2
                
                for i in range(0,first_half+1):
                    for j in range(0,col+1):
                        if seats[i][j]=="B":
                            current_income_count.append(10)
                            
                for i in range(i+1,row+1):
                    for j in range(0,col+1):
                        if seats[i][j]=="B":
                            current_income_count.append(8)
                            
        return sum(current_income_count)
    
    def set_total_income(Total_seat,row,col):
        if Total_seat > 60:
            first_half = row // 2
            second_half = row - first_half
            total_price = (first_half*col*10)+(second_half*col*8)
        else:
            total_price = Total_seat*10
        return total_price
    
        
Bioscope = Movie(int(input("Enter the number of rows: ")),
                int(input("Enter the number of seats in each row: "))
                )

print()

choice = {1:'Show the seat',2:'Buy a ticket',3:'Statistics',4:'Show Booked Ticket User Info',0:'Exit'}

while True:
    for value in choice:
        print(str(value)+'.',choice[value])
    choice_input = int(input())
    if choice_input == 1:
        Bioscope.show_seats()
    elif choice_input == 2:
        Bioscope.buy_a_ticket(int(input("Please enter the row number in which you want to book seat: ")),
                    int(input("Please enter the column number in which you want to book seat: ")))
    elif choice_input == 3:
        Bioscope.statistics()
    elif choice_input == 4:
        Bioscope.show_details(int(input("Please enter the row number of which you want to see booked seat details: ")),
                    int(input("Please enter the column number of which you want to see booked seat detailst: ")))
    elif choice_input == 0:
        print('\n You are out')
        break
    else:
        print("\n Opp's invalid input! Please try again.\n ")
        
