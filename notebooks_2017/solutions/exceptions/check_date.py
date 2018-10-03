def check_date(date):
    d, m, y = date.split("/")
    d, m, y = int(d), int(m), int(y)

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 12 < m or m < 1:  # m in [1,12]
        return False

    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):  # leap year
        months[1] = 29

    if months[m - 1] < d or d < 1:
        return False

    return True


while True:
    try:
        if check_date(input("Please enter a date (DD/MM/YYYY) : ")):
            print("OK")
            break
        else:
            raise ValueError()

    except ValueError:
        print("Oops!  That was no valid date.  Try again...")
