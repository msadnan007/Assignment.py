def computepay(hours, rate):

        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            overtime_hours = hours - 40
            overtime_rate = rate * 1.5
            regular_pay = 40 * rate
            overtime_pay = overtime_hours * overtime_rate
            total_pay = regular_pay + overtime_pay
        else:
            total_pay = hours * rate
        return total_pay

try:
    hours_input = input("Enter hours worked: ")
    rate_input = input("Enter hourly rate: ")
    pay = computepay(hours_input,rate_input)
    print("Total pay:", pay)
except:
    print("Error,please input numeric input")

