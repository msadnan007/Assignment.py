seconds=int(input("Enter seconds:"))
hour=seconds//3600
seconds2=seconds%3600
minutes=seconds2//60
seconds3=seconds2%60
print(seconds, "Seconds is",hour,"hours,",minutes,"minutes,",seconds3,"seconds")
