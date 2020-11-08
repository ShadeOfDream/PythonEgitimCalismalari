import json
from datetime import date

firstname = str(input("Please enter first name: "))
lastname = str(input("Please enter last name: "))

print(f"**********************\nFull Name : {firstname} {lastname}\n**********************")

gender = str(input("Please enter gender (Male/Female):"))
#while gender == "Male" or gender == "Female":
while gender in ("Male","male","Female","female"):
    break
else:
    print("Gender should be either Male or Female")   

ssn = int(input("Please enter ssn: "))
while len(str(ssn))!=9:
  print("Only 9 digit allowed!")
  ssn = int(input("Please enter ssn: "))

yearOfBirth = int(input("Please enter birth year : "))
while len(str(yearOfBirth))!=4:
 print("Only 4 digit allowed!")
 yearOfBirth = int(input("Please enter birth year : "))

dateCurrent = date.today()
yearCurrent=dateCurrent.year
#print(yearCurrent)
age = yearCurrent - yearOfBirth
print(f"*********\nAge : {age}\n*********")
address = str(input("Please enter address: "))
print("---------------------------------")

RapperPersonelInformation = {
    "First Name" : firstname,
    "Last Name" : lastname,
    "Gender" : gender,
    "SSN" : ssn,
    "Age" : age,
    "Address" : address
} 

f = open("RapperOutput.json","w")
f.write(json.dumps(RapperPersonelInformation))
f.close()

    