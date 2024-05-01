#vehicles list
vehicleList=['Ford F-150', 
             'Chevrolet Silverado', 
             'Tesla Cybertruck', 
             'Toyota Tundra',
             'Nissan Titan']
#menu loads 1
def choose1():
  print("The AutoCountry sales manager has authorized the purchase and selling of") 
  print("the following vehicles:")
  print(vehicleList[0])
  print(vehicleList[1])
  print(vehicleList[2])
  print(vehicleList[3])
  print(vehicleList[4])

#menu loads 2
def choose2():
  print("Please Enter the full Vehicle name:")
  itemCheck= input()
  if itemCheck in vehicleList:
      print(itemCheck +" is an authorized vehicle")
      (onLoadMenu())

  if itemCheck not in vehicleList:
    print(itemCheck + " is not an authorized vehicle, if you received this in error ")
  print("please check the spelling and try again")
  onLoadMenu()
#menu loads 3
def choose3():
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
  print("3. EXIT")
  user_input=input()
  if user_input=="1":
    choose1()
    onLoadMenu()
  
  if user_input=="3": 
    choose3()
  
  if user_input=="2":
    choose2()
  
#print menu
print(onLoadMenu())
  
  

