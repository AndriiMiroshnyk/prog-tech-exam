import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])

if __name__ == '__main__':
    userDate = input("Enter the date: ")
    print(findDay(userDate))