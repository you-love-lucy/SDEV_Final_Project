"""

Name: Lucy Jones
Project: Reservation Records
Function: Record hotel reservation and payment info.

"""

# import neccesary modules
from breezypythongui import EasyFrame
from tkinter import PhotoImage
resLog = open("reservationRecordLogs.txt.", "a")

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
        self.addLabel(text = "Payment type: ", row = 5, column = 0)
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
        self.addLabel(text = "Room number: ", row = 7, column = 0)
        self.roomNum = self.addRadiobuttonGroup(row = 7, column = 1)
        self.roomNum.addRadiobutton(text = "101")
        self.roomNum.addRadiobutton(text = "102")
        self.roomNum.addRadiobutton(text = "103")
        self.roomNum.addRadiobutton(text = "104")
        self.roomNum.addRadiobutton(text = "105")
        self.roomNum.addRadiobutton(text = "106")
        self.roomNum.addRadiobutton(text = "107")
        self.roomNum.addRadiobutton(text = "108")
        # save and open folio buttons
        self.addButton(text = "Save", row = 6, column = 3, command = self.saveReservation)
        self.addButton(text = "Open Folio", row = 8, column = 1, columnspan = 2, command = self.openFolio)
        
    def openFolio(self):
        # open folio window
        FolioWindow(self.price).mainloop()

    def calculatePrice(self):
        # calculate the price
        rate = self.rate.getNumber()
        nightNum = self.nightNum.getNumber()
        if rate >= 1 and nightNum >= 1:
            try:
                self.price = rate*nightNum
                self.priceNum["text"] = self.price
            except ValueError:
                self.messageBox(title = "Error", message = "Error in entered data.")
        else:
            self.messageBox(title = "Error", message = "Error in entered data.")
            
    def saveReservation(self):
        # save the reservation information to the file
        try:
            # get last name and make sure it isn't blank
            lName = self.lName.getText()
            if lName == "":
                self.messageBox(title = "Error", message = "No last name entered.")
            # get first name and make sure it isn't blank
            fName = self.fName.getText()
            if fName == "":
                self.messageBox(title = "Error", message = "No first name entered.")
            # get address and make sure it isn't blank
            address = self.address.getText()
            if address == "":
                self.messageBox(title = "Error", message = "No address entered.")
            # get phone number
            phoneNum = str(self.phoneNum.getNumber())
            # get payment type
            payType = self.payType.getSelectedButton()["text"]
            # get check-in date and make sure it isn't blank
            inDate = self.inDate.getText()
            if inDate == "":
                self.messageBox(title = "Error", message = "No check-in date entered.")
            # make sure price has been calculated
            if self.price > 0:
                # get number of nights
                nightNum = str(self.nightNum.getNumber())
                # get rate
                rate = str(self.rate.getNumber())
            else:
                self.messageBox(title = "Error", message = "Calculate price before saving.")
            # get room number
            roomNum = self.roomNum.getSelectedButton()["text"]
            # write information to file
            resLog.write(lName + ", " + fName + " | " + address + " | " + payType + " | Check-in: " + inDate + " | " + nightNum + " | " + rate + " | " + "Total: " + str(self.price) + " | " + roomNum)
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
            except ValueError:
                self.messageBox(title = "Error", message = "Error in entered data.")
        else:
            self.messageBox(title = "Error", message = "Payment exceeds current balance. Maximum payment: " + str(self.balance))

def main():
    ReservationWindow().mainloop()

if __name__ == "__main__":
    main()
