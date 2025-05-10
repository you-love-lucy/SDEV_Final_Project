"""

Name: Lucy Jones
Project: Reservation Records
Function: Record hotel reservation and payment info
Notes: Faced some issues with opening a new window and input validation.
Add/Fix:
- Test the application
- Write a manual.

"""

# import neccesary modules
from breezypythongui import EasyFrame
from tkinter import PhotoImage
resLog = open("reservationRecordLogs.txt.", "w")

# make a class for the reservation information window
class ReservationWindow(EasyFrame):
    
    def __init__(self):
        # title
        EasyFrame.__init__(self, title = "New Reservation")
        # logo image
        try:
            label = self.addLabel(text = "", row = 0, column = 3) 
            self.logoImage = PhotoImage(file = "logo.gif")
            label["image"] = self.logoImage
        except Exception:
            label = self.addLabel(text = "Hotel Logo", row = 0, column = 3)
        # heading
        self.addLabel(text = "Enter guest information: ", row = 0, column = 0, columnspan = 2)
        # last name
        self.addLabel(text = "Last name: ", row = 1, column = 0)
        self.lName = self.addTextField(text = "", row = 1, column = 1)
        # first name
        self.addLabel(text = "First name: ", row = 2, column = 0)
        self.fName = self.addTextField(text = "", row = 2, column = 1)
        # address
        self.addLabel(text = "Address: ", row = 3, column = 0)
        self.address = self.addTextField(text = "", row = 3, column = 1)
        # phone number
        self.addLabel(text = "Phone number: ", row = 4, column = 0)
        self.phoneNum = self.addIntegerField(0, row = 4, column = 1)
        # payment type
        self.payType = self.addRadiobuttonGroup(row = 5, column = 1)
        self.payType.addRadiobutton(text = "Cash")
        self.payType.addRadiobutton(text = "Card")
        self.payType.addRadiobutton(text = "Check")
        # check-in date
        self.addLabel(text = "Check-in date: ", row = 1, column = 2)
        self.inDate = self.addTextField(text = "", row = 1, column = 3)
        # nights
        self.addLabel(text = "Nights:  ", row = 2, column = 2)
        self.nightNum = self.addIntegerField(0, row = 2, column = 3)
        # rate
        self.addLabel(text = "Rate: ", row = 3, column = 2)
        self.rate = self.addIntegerField(0, row = 3, column = 3)
        # price calculations
        self.addButton(text = "Get price", row = 4, column = 2, columnspan = 2, command = self.calculatePrice)
        self.addLabel(text = "Price: ", row = 5, column = 2)
        self.price = 0
        self.priceNum = self.addLabel(text = self.price, row = 5, column = 3)
        # room number
        self.addLabel(text = "Room number: ", row = 6, column = 0)
        self.roomNum = self.addRadiobuttonGroup(row = 6, column = 1)
        self.roomNum.addRadiobutton(text = "101")
        self.roomNum.addRadiobutton(text = "102")
        self.roomNum.addRadiobutton(text = "103")
        self.roomNum.addRadiobutton(text = "104")
        # save and open folio buttons
        self.addButton(text = "Save", row = 6, column = 3, command = self.saveReservation)
        self.addButton(text = "Open Folio", row = 7, column = 1, columnspan = 2, command = self.openFolio)
        
    def openFolio(self):
        # open folio window
        FolioWindow(self.price).mainloop()

    def calculatePrice(self):
        # calculate the price
        try:
            rate = self.rate.getNumber()
            nightNum = self.nightNum.getNumber()
            self.price = rate*nightNum
            self.priceNum["text"] = self.price
        except ValueError:
            self.messageBox(title = "Error", message = "Error in entered data.")
            
    def saveReservation(self):
        # save the reservation information to the file
        try:
            lName = self.lName.getText()
            fName = self.fName.getText()
            address = self.address.getText()
            phoneNum = str(self.phoneNum.getNumber())
            payType = self.payType.getSelectedButton()["text"]
            inDate = self.inDate.getText()
            nightNum = str(self.nightNum.getNumber())
            roomNum = self.roomNum.getSelectedButton()["text"]
            resLog.write(lName + ", " + fName + " | " + address + " | " + payType + " | Check-in: " + inDate + " | " + nightNum + " | " + roomNum)
            resLog.close()
        except ValueError:
            self.messageBox(title = "Error", message = "Error in entered data.")
    
class FolioWindow(EasyFrame):

    def __init__(self, price):
        self.result = []
        # title
        EasyFrame.__init__(self, title = "Folio")
        # folio image
        try:
            label = self.addLabel(text = "", row = 0, column = 3)
            self.folioImage = PhotoImage(file = "folio.gif")
            label["image"] = self.folioImage
        except Exception:
            label = self.addLabel(text = "Bill Image", row = 0, column = 3)
        # price
        self.price = price
        self.addLabel(text = "Total price due: ", row = 1, column = 0)
        self.addLabel(text = price, row = 1, column = 1)
        # payment log and payment log additions
        self.payment = self.addIntegerField(0, row = 2, column = 0)
        self.addButton(text = "Add payment", row = 2, column = 1, command = self.calculate)
        self.addLabel(text = "Payments: ", row = 3, column = 0)
        self.payments = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 8)
        # balance
        self.balance = price
        self.addLabel(text = "Remaining balance: ", row = 5, column = 0)
        self.curBalance = self.addLabel(text = self.balance, row = 5, column = 1)

    def calculate(self):
        # calculate the new balance
        if self.payment.getNumber() <= self.balance:
            try:
                payment = self.payment.getNumber()
                currentBalance = self.balance
                self.result.append(payment)
                self.paymentText = "\n".join(str(payment) for payment in self.result)
                self.payments.setText(self.paymentText)
                currentBalance = currentBalance - payment
                self.curBalance["text"] = currentBalance
                self.balance = currentBalance
                print(self.balance)
            except ValueError:
                self.messageBox(title = "Error", message = "Error in entered data.")
        else:
            self.messageBox(title = "Error", message = "Payment exceeds current balance. Maximum payment: " + str(self.balance))

def main():
    ReservationWindow().mainloop()

if __name__ == "__main__":
    main()
