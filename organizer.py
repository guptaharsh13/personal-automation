import os
import re


def organize(path, want_name):
    temp_path = os.getcwd()
    os.chdir(path)

    # dates - contains each file date
    # also, clean file names initially
    dates = []
    for f_name in os.listdir():
        if os.path.isdir(f_name):
            continue

        date = re.findall(r'\d{2}-\w+-\d{4}', f_name)
        if not date:
            continue
        date = date[0]
        dates.append(date)
        extension = f_name.split(".")[-1]
        if extension == f_name:
            continue
        name = re.findall(r'\d{2}-\w+-\d{4}_(.+)\.\w+', f_name)
        name = name[0] if name else ""
        to_name = f"{name} {date}.{extension}"
        os.rename(f_name, to_name)

    # months - contains files with the same month - for example - all Feb files would be stored in months[1]
    months = []
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                   'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_numbers = []

    for month_number in range(1, 13):
        temp = str(month_number)
        if len(temp) == 1:
            temp = "0"+temp
        month_numbers.append(temp)

    for i in range(12):
        months.append([])

    # basically loop through each file (each date means each file)
    for date in dates:
        for i in range(12):
            if month_numbers[i] == date.split("-")[1]:
                months[i].append(date)
            elif month_names[i] in date:
                months[i].append(date)

    sortedDates = []
    for month in months:
        # month contains dates
        month.sort()
        sortedDates += month

    order = dict()

    # to reduce time complexity
    for date in sortedDates:
        order[date] = None

    count = 0
    for date in sortedDates:
        count += 1

        if order[date]:
            if type(order[date]) == int:
                order[date] = [order[date], count]
            else:
                order[date].append(count)
        else:
            order[date] = count

    for key, value in order.items():
        print(key, value)

    for f_name in sorted(os.listdir()):
        try:
            date = f_name.split()[1].split(".")[0]
        except:
            continue
        extension = f_name.split(".")[-1]
        name = f"          {f_name.split()[0]}" if want_name == "y" else ""

        if type(order[date]) is int:
            number = str(order[date])
        else:
            number = str(order[date][0])
            order[date].remove(order[date][0])

        os.rename(
            f_name, f"{number}          [{date}]{name}.{extension}")

    os.chdir(temp_path)


def main():
    path = input('Enter absolute path to your course folder - ')
    path = fr'{path}'.format(path=path)
    want_name = input("Do you want name (y/n) - ")
    want_name = want_name.lower()
    while not (want_name == "y" or want_name == "n"):
        want_name = input("Do you want name - ")
    organize(path, want_name)


if __name__ == "__main__":
    main()
