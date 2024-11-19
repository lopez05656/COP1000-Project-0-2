# Register Dependencies
import time

# Program Start

def displayVehicles():
 print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
 file = open("availablevehicles.txt", "r")
 fileContents = file.read()
 print(fileContents)
 print("Returning to the menu in 5 seconds...")
 time.sleep(1)
 print("Returning to the menu in 4 seconds...")
 time.sleep(1)
 print("Returning to the menu in 3 seconds...")
 time.sleep(1)
 print("Returning to the menu in 2 seconds...")
 time.sleep(1)
 print("Returning to the menu in 1 seconds...")
 time.sleep(1)
 print("Returning to the menu now...")
 time.sleep(1)
 menu()

def searchForVehicles():
 Search = input("Search: ")
 file = open("availablevehicles.txt")
 filecontent = file.readlines()
 #if Search == "Tesla" or Search == "tesla":
  #print(filecontent[2])
 if Search == "Ford" or Search == "ford":
  print(filecontent[0])
 if Search == "Nissan" or Search == "nissan":
  print(filecontent[4])
 if Search == "Toyota" or Search == "toyota":
  print(filecontent[3])
 if Search == "Chevy" or Search == "chevy" or Search == "Chevrolet" or Search == "chevrolet":
  print(filecontent[1])
 else:
  print(Search, "is not an authorized vehicle. Please try again...")

def menu():
 print("************************************")
 print("  AutoCountry Vehicle Finder v0.2")
 print("************************************")
 print("Please select one of the following numbers from the menu below:")

 print("1: PRINT all Authorized Vehicles")
 print("2: SEARCH all Authorized Vehicles")
 print("3: Exit")
 menuSelection = int(input("Your Selection: "))
 
 if menuSelection == int("1"):
  displayVehicles()

 if menuSelection == int("2"):
  searchForVehicles()

 if menuSelection == int("3"):
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()
menu()

# Program Complete. 
