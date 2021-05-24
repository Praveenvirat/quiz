# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class OnlineBooking:
    def __init__(self,row,cols):
        self.rows = row
        self.num_of_seats_per_row = cols
        self.total_num_of_seats = (row-1) * (cols-1)
        self.total_seats_sold = 0
        self.current_income = 0
        self.total_income = 0
        self.user_info = []
        self.seats = []
        for r in list(range(0,self.rows)):
            row_seats = []
            row_info = []
            if r == 0:
                for c in list(range(0,self.num_of_seats_per_row)):
                    row_seats.insert(c,c)
                    row_info.insert(c,{"":""})

            else:
                for c in list(range(0,self.num_of_seats_per_row)):
                    if c != 0:
                        row_seats.insert(c,'S')
                    else:
                        row_seats.insert(c,r)
                    row_info.insert(c, {"": ""})

            if self.total_num_of_seats > 60:
                if int((self.rows - 1) / 2) >= r:
                    self.total_income += (8 * self.num_of_seats_per_row)
                else:
                    self.total_income += (10 * self.num_of_seats_per_row)
            else:
                self.total_income += (10 * self.num_of_seats_per_row)

            self.seats.insert(r, row_seats)
            self.user_info.insert(r,row_info)

    def start_program(self):
        exit = 0
        while (exit == 0):
            print('1. Show the seats')
            print('2. Buy a Ticket')
            print('3. Statistics')
            print('4. Show Booked Tickets User Info')
            print('0. Exit ')
            choice = int(input(''))
            if choice == 1:
                self.show_seats()
            elif choice == 2:
                self.buy_ticket()
            elif choice == 3:
                self.statistics()
            elif choice == 4:
                self.show_user_info()
            else:
                exit = 1

    def show_seats(self):
        print('Cinema:')
        for r in self.seats:
            for value in r:
                print(value, end=" ")
            print('')

    def statistics(self):
        print('Number of purchased tickets: ',self.total_seats_sold)
        print('Percentage of Tickets booked: ',
              self.total_seats_sold * 100 / self.total_num_of_seats)
        print('Current Income: $',self.current_income)
        print('Total Income: $',self.total_income)

    def buy_ticket(self):
        row_num = int(input('Enter row : '))
        column_num = int(input('Enter column : '))
        if self.seats[row_num][column_num] == 'B':
            print('This seat is already taken')
        else:
            ticket_price = 10
            if self.total_num_of_seats > 60:
                if int((self.rows - 1)/2) >= row_num :
                    ticket_price = 8
            print('The cost of the seat is $',ticket_price)
            to_book = int(input('Do u want to book? \n1.yes\n2.no \n '))
            if to_book == 1:
                name = input('Enter the Name : ')
                gender = input('Enter the Gender : ')
                age = input('Enter the Age : ')
                phone_num = input('Enter the phone num : ')
                user_info = {'name':name,'gender':gender,'age':age,'phone_num':phone_num,'ticket_price':ticket_price}
                self.seats[row_num][column_num] = 'B'
                self.user_info[row_num][column_num] = user_info
                self.total_seats_sold += 1
                self.current_income += ticket_price
                print('Booked Successfully')

    def show_user_info(self):
        row_num = int(input('Enter row : '))
        column_num = int(input('Enter column : '))
        user_info = self.user_info[row_num][column_num]
        print('Name:',user_info.get('name'))
        print('Gender:',user_info.get('gender'))
        print('Age:',user_info.get('age'))
        print('Ticket Price: $',user_info.get('ticket_price'))
        print('Phone Number:',user_info.get('phone_num'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rows = int(input("Enter number of rows :"))
    rows = rows+1
    num_of_seats_per_row = int(input("Enter number of seats PER row :"))
    num_of_seats_per_row = num_of_seats_per_row+1
    book = OnlineBooking(rows,num_of_seats_per_row)
    book.start_program()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
