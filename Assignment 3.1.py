try:
    hours_input= int(input("Enter Hours"))
    rate_input= float(input("Enter Rate"))
    if hours_input<=40:
        print("Pay:", (hours_input * rate_input))
    else:
        print("pay:", ((rate_input * 40)+(hours_input-40)*(rate_input * 1.5)) )
except:
    print("Error, please input numeric input.")