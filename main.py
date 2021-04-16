# COMPULSORY TASK - JHB Metro Police Demerit
your_speed = int(input("What was your average speed in km/h: "))
average_speed = int(input("What was the allowed speed on the road: "))
diff = your_speed - average_speed

if your_speed <= average_speed:
    print("Ok!")
else:
    point = diff/5
    point = int(point)
    print(point)
    if point > 12:
        print("Time to go to jail!")
