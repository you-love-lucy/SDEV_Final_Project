"""

Name: Lucy Jones
Project: Reservation Records
Function: Record hotel reservation and payment info
Notes: So far I have the user-facing windows made. I need to create the logic behind them next, including a module to write the entered information to a text file.
I will also need to create a module to add new payments and calculate the new balance. I faced a few problems with the "Open Folio" button, but I worked it out.
I also need to add input validation and images. After that I need to test the application, write a manual, and add comments.

"""

from breezypythongui import EasyFrame

class ReservationWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "New Reservation")
        self.addLabel(text = "Enter guest information: ", row = 0, column = 0, columnspan = 2)
        self.addLabel(text = "Last name: ", row = 1, column = 0)
        self.addTextField(text = "", row = 1, column = 1)
        self.addLabel(text = "First name: ", row = 2, column = 0)
        self.addTextField(text = "", row = 2, column = 1)
        self.addLabel(text = "Address: ", row = 3, column = 0)
        self.addTextField(text = "", row = 3, column = 1)
        self.addLabel(text = "Phone number: ", row = 4, column = 0)
        self.addTextField(text = "", row = 4, column = 1)
        self.addLabel(text = "Payment type: ", row = 5, column = 0)
        self.addTextField(text = "", row = 5, column = 1)
        self.addLabel(text = "Check-in date: ", row = 1, column = 2)
        self.addTextField(text = "", row = 1, column = 3)
        self.addLabel(text = "Nights:  ", row = 2, column = 2)
        self.nightNum = self.addIntegerField(0, row = 2, column = 3)
        self.addLabel(text = "Rate: ", row = 3, column = 2)
        self.rate = self.addIntegerField(0, row = 3, column = 3)
        self.addButton(text = "Get price", row = 4, column = 2, columnspan = 2)
        self.addLabel(text = "Price: ", row = 5, column = 2)
        self.price = 0
        self.addLabel(text = self.price, row = 5, column = 3)
        self.addLabel(text = "Room number: ", row = 6, column = 1)
        self.addTextField(text = "", row = 6, column = 2)
        self.addButton(text = "Open Folio", row = 7, column = 1, columnspan = 2, command = self.openFolio)
    def openFolio(self):
        FolioWindow(self.price).mainloop()

class FolioWindow(EasyFrame):
    def __init__(self, price):
        EasyFrame.__init__(self, title = "Folio")
        self.addLabel(text = "Total price due: ", row = 0, column = 0)
        self.addLabel(text = price, row = 0, column = 1)
        self.addLabel(text = "Add payment: ", row = 1, column = 0)
        self.addIntegerField(0, row = 1, column = 1)
        self.addLabel(text = "Payments: ", row = 2, column = 0)
        self.addTextArea("", row = 3, column = 0, columnspan = 2, width = 50, height = 10)
        paymentsTotal = 0
        balance = price - paymentsTotal
        self.addLabel(text = "Remaining balance: ", row = 4, column = 0)
        self.addLabel(text = balance, row = 4, column = 1)
    
def main():
    ReservationWindow().mainloop()

if __name__ == "__main__":
    main()
