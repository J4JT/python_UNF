print('Welcome to Python program')
print('Menu options are:')
print('     Enter 1 for calculation gallons of paint needed to paint a room')
print('     Enter 2 for calculating Body Mass Index')
print('     Enter any other valye to quit program\n')
choice =input('Enter Choice now\n')
#1 for paint and 2 for BMI 
while True:
  try:
    if choice=='1':
      print('Welcome to the paint needed caculator')
      length = int(input("Enter the length of the room: "))
      width = int(input("Enter  the width of the room: "))
      height =int(input("Enter the height of the room: "))
      doors =int(input('how many doors are in the room? '))
      windows =int(input('how many windows are in the room? '))
     #Calculations total area of 4 walls - area of doors and windows
     #divide the result by how much area a gallon covers
      totalArea=2 * (length * height) + 2 *(width * height)
      gallonCovers=315
      adjustedTotalArea= float(totalArea - ((doors * 25)+(windows *10)))/315
      
      formated_float = "{:.2f}".format(adjustedTotalArea)
      
     
      print(formated_float,end='')
      print( ' gallons of paint are needed to paint a room {} feet wide by {} feet long by {} feet high with {} doors and {} windows'.format(width + 0.00, length + 0.00, height + 0.00, doors, windows))
      break
    elif choice=='2':
      print('Welcome to the body mass index (BMI) calculator')
      weight = int(input("Enter first number: "))
      height = int(input("Enter second number: "))
      BMI= (weight/(height * height)) * 703
      print('your BMI is {}, according to NIH,'.format(BMI),end='')
      if(BMI<18.5):
        print('you are Underweight')
        break
      elif(BMI>18.5 and BMI<24.9):
        print('you are Normal')
        break
      else:
        print('you are Overweight')
        break
    else:
      print('not valid')
      break
  except ValueError:
    print('not a valid choice')

