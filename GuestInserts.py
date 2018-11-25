#/usr/bin/python
from random import randrange
print("Attempting to generate inserts from the guest table. Never trust Torren to do anything write")
guestFile = open("HotelGuestList.txt", "r")
guests = guestFile.readlines()
guestFile.close()

gInsertFile = open("GuestInserts.txt", "w")
ccNum = 1111111111111111
countryCode = 1
areaCode = 111
phoneNum = 1111111
streetNum = 1
streets = ("Diagon Alley", "Godric's Hollow", "Godric's Hollow", "Knockturn Alley", "Hogsmeade", "Privet Drive, Little Whinging, Surrey")
for line in guests:
	guestTokens = line.split(" ")
	address = str(streetNum) + " " + streets[randrange(6)]  
	firstName = guestTokens[0]
	lastName = guestTokens[1]
	email = guestTokens[2]
	fullPhone = str(countryCode) + str(areaCode) + str(phoneNum)
	insert = "INSERT INTO GUEST VALUES("
	insert += "'" + firstName + " " + lastName + "', '" + str(ccNum) + "', " + "'" + fullPhone + "', " + "'" + address + "');"
	ccNum += randrange(1,101) * 42701
	areaCode += randrange(0,16)
	phoneNum += randrange(1,10)
	streetNum += 1
	countryCode += randrange(0,10)
	gInsertFile.write(insert + "\n")
gInsertFile.close()
print("Done")
	
	
	
	