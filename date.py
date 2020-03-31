class Date:
    MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def update_date(self):
        if self.__year % 4 == 0 and self.__month == 2:
            add = 1
        else:
            add = 0
        if self.__day < self.MONTH_DAYS[self.__month - 1] + add:
            self.__day += 1
        else:
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
