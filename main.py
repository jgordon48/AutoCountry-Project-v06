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
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  raise SystemExit

#OnloadMenu
def onLoadMenu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please enter the following number below from the following menu:")
  print("1. Print all Authorized Vehicles")
  print("2. Exit")
  user_input=input()
  if user_input=="1":
    return choose1() + onLoadMenu()

    
  if user_input=="2": 
    choose2()
  
#print menu
print(onLoadMenu())
  
  

