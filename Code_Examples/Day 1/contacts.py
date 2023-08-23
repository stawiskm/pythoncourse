class Contact:
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email
  
  def __str__(self):
    return f"{self.name}, {self.phone}, {self.email}"

def display(contacts):
  print("This is a list of your contacts: \n")
  for contact in contacts:
    print("Name: " + contact.name)
    print("Phone number: " + str(contact.phone))
    print("Email: " + contact.email + "\n")

def writeCSV(contact):
  f = open('contacts.csv', 'a') 
  writer = csv.writer(f)
  writer.writerow([contact.name, contact.phone, contact.email])
  f.close()

def clearCSV():
   with open('contacts.csv', 'w', newline='') as csv_file:
      pass


import csv
with open('contacts.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    contacts = []
    for row in reader:
      contact = Contact(row[0], row[1], row[2])
      contacts.append(contact)

while True:
    print("What do you want to do: list your contacts, add a contact or remove a contact? Type quit to exit the program.")
    goal= input()
    if "list" in goal.lower():
        display(contacts)
    if "add" in goal.lower():
      print("Please enter the following information for your contact, separated by commas: Name, Phone Number, Email")
      newContactInfo= input()
      chunks= newContactInfo.split(',')
      print(chunks)
      newContact = Contact(chunks[0], chunks[1], chunks[2])
      print(newContact)
      contacts.append(newContact)
      writeCSV(newContact)
      display(contacts)
    if "remove" in goal.lower():
        display(contacts)
        print("Which contact do you want to remove? Enter the name you want to delete.")
        toDelete= input()
        updated_contacts = []
        for contact in contacts:
          if toDelete.capitalize() not in contact.name:
            updated_contacts.append(contact)  
        contacts = updated_contacts
        clearCSV()
        for contact in contacts:
          
          writeCSV(contact)

    if "quit" in goal:
      break
        



