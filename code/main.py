#vehicles list
vehicleList=['Ford F-150', 
             'Chevrolet Silverado', 
             'Tesla Cybertruck', 
             'Toyota Tundra',
             'Nissan Titan',
             "Rivian R1T", 
             "Ram 1500"]

authorizedVehicles="authorizedVehicles.txt"
def saveVehicles():
  with open(authorizedVehicles,"w") as file:
    for vehicle in vehicleList:
      file.write(vehicle+ "\n")


#menu loads 1
def choose1():
  print("The AutoCountry sales manager has authorized the purchase and selling of \
  the following vehicles:")
  for vehicle in vehicleList:
    print(vehicle)

#menu loads 2
def choose2():
  print("Please Enter the full Vehicle name:")
  itemCheck= input()
  if itemCheck in vehicleList:
      print(itemCheck +" is an authorized vehicle")
      (onLoadMenu())

  if itemCheck not in vehicleList:
    print(itemCheck + " is not an authorized vehicle, if you received this in error \
    please check the spelling and try again")
  onLoadMenu()
  
#menu loads 3
def choose3():
  addVehicle = input("Please Enter the full Vehicle name you would like to add: ")
  if addVehicle not in vehicleList:
    vehicleList.append(addVehicle)
    saveVehicles()
  print("You have added '" + addVehicle + "' as an authorized vehicle")
  onLoadMenu()
  
#menu loads 4
def choose4():
  removeVehicle = input("Please Enter the full Vehicle name you would \
  like to REMOVE: ")
  if removeVehicle in vehicleList:
      confirmRemoval = input("Are you sure you want to remove '" + removeVehicle + "'\
      from the Authorized vehicles List?: ")
      if confirmRemoval == "yes":
        vehicleList.remove(removeVehicle)
        saveVehicles()
        print("You have REMOVED '" + removeVehicle + "' as \
  an authorized vehicle")
  onLoadMenu()
  
#menu loads 5
def choose5():
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  raise SystemExit

#OnloadMenu
def onLoadMenu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please enter the following number below from the following menu:")
  print("1. PRINT all Authorized Vehicles")
  print("2. SEARCH all Authorized Vehicles")
  print("3. ADD Authorized Vehicle")
  print("4. DELETE Authorized Vehicle")
  print("5. EXIT")
  user_input=input()
  if user_input=="1":
    choose1()
    onLoadMenu()

  if user_input=="3": 
    choose3()
    
  if user_input=="4": 
    choose4()
  
  if user_input=="2":
    choose2()

  if user_input=="5":
    choose5()
  
  
#print menu
print(onLoadMenu())
  
  

