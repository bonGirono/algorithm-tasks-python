"""
Задача
---------------------------------
Сейчас активно развивается новая история, основателем которой является Профессор А.С. Багиров. Он выяснил, что на протяжении многих лет на земле вместе с людьми существовали ящеры. Строительство пирамид,
захват Байкала и еще много разных событий произошли благодаря ящерам.
Учёные ещё не выяснили, сколько времени ящеры существовали на земле. Они находят разные данные в виде даты начала и даты окончания, и чтобы проверить их на корректность, необходимо посчитать,
сколько дней ящеры существовали для двух конкретных дат. Календарь ящеров очень похож на григорианский, лишь с тем исключением, что там нет високосных годов.
Вам даны дата начала и дата окончания существования ящеров, нужно найти количество полных дней и секунд в неполном дне, чтобы учёные смогли оценить, насколько даты корректны.

Формат ввода
---------------------------------
В первой строке содержатся 6 целых чисел year1, month1, day1, hour1, min1, sec1 (1≤yeaT9)— дата начала существования ящеров.
Во второй строке содержатся 6 целых чисел year2, month2, day2, hour2, min2, sec2 (1≤year2≤9999, 1≤month2≤12, 1≤day2≤31, 0≤hour2≤23, 0≤min2≤59, 0≤sec2≤59)— дата окончания существования ящеров.
Гарантируется, что дата начала меньше, чем дата конца.

Формат вывода
---------------------------------
В первой и единственной строке выведите 2 числа: количество дней, сколько существовали ящеры, а также количество секунд в неполном дне.


Пример 1
Ввод
 980 2 12 10 30 1
 980 3 1 10 31 37
	Вывод
 17 96

Пример 2
Ввод
 1001 5 20 14 15 16
 9009 9 11 12 21 11
	Вывод
 2923033 79555
Примечания
Напоминаем:
В календаре древних ящеров:
-	Нет високосных годов.
-	В одном году 365 дней.
-	Год делится на 12 месяцев, количество дней в каждом месяце: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
-	В одном дне 24 часа (от 0 до 23).
-	В одном часу 60 минут (от 0 до 59).
-	В одной минуте 60 секунд (от 0 до 59).
Первый тестовый пример.
-	Года начала и конца совпадают;
-	Между 12 февраля и 1 марта прошло 17 полных дней;
-	Начало было в 10:30:01, а конец в 10:31:37 — таким образом дополнительно прошла 1 минута и 36 секунд, то есть 96 секунд.
Второй тестовый пример.
-	Прошло 8008 полных лет;
-	В каждом году 365 дней, суммарно получается 2922920 дней.
-	От 20 дня 5 месяца до 20 дня 8 месяца прошли еще 31 + 30 + 31 день - суммарно 92 дня.
-	От 20 дня 8 месяца до 10 дня 9 месяца прошло еще (31 - 20) + 10 = 21 полный день.
-	Всего полных дней 2922920 + 92 + 21 = 2923033.
-	От 10 дня 9 месяца 14:15:16 до 11 дня 9 месяца 12:21:11 прошло 79555 секунд.

"""


class DateToSeconds:
    days: int
    hours: int
    minutes: int
    seconds: int
    seconds_in_minute = 60
    minutes_in_hours = 60
    hours_in_day = 24

    def __init__(self, days, hours, minutes, seconds) -> None:
        self.days = days
        self.hours = hours + 1
        self.minutes = minutes + 1
        self.seconds = seconds + 1

    def convert_days_to_hours(self, days) -> int:
        return self.hours_in_day * days

    def convert_hours_to_minutes(self, hours) -> int:
        return self.minutes_in_hours * hours

    def convert_minutes_to_seconds(self, minutes) -> int:
        return self.seconds_in_minute * minutes

    def total_hours(self) -> int:
        return self.hours + self.convert_days_to_hours(self.days)

    def total_minutes(self) -> int:
        return self.minutes + self.convert_hours_to_minutes(self.total_hours())

    def total_seconds(self) -> int:
        return self.seconds + self.convert_minutes_to_seconds(self.total_minutes())

    def seconds_in_day(self) -> int:
        return 60 * 60 * 24

    def __sub__(self, other) -> tuple[int, tuple[int, int]]:
        result = self.total_seconds() - other.total_seconds()
        days = result // self.seconds_in_day()
        seconds = result % self.seconds_in_day()
        return result, (days, seconds)


class DaysCounter:
    year: int
    month: int
    day: int
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, year, month, day):
        self.year = year - 1
        self.month = month - 1
        self.day = day

    def __calc_days_in_months(self):
        if self.month < 1:
            return self.MONTHS[0]
        total = 0
        for i in range(0, self.month):
            total += self.MONTHS[i]
        return total

    @property
    def days(self):
        return (self.year * 365) + self.__calc_days_in_months() + self.day


# d1 = DateToSeconds(DaysCounter(980, 2, 12).days, 10, 30, 1)
# d2 = DateToSeconds(DaysCounter(980, 3, 1).days, 10, 31, 37)
# print(d2 - d1)  # выведет: (1468896, (17, 96)), то есть 17 дней и 96 секунд, или 1 468 896 секунд в сумме
# d1 = DateToSeconds(DaysCounter(1001, 5, 20).days, 14, 15, 16)
# d2 = DateToSeconds(DaysCounter(9009, 9, 11).days, 12, 21, 11)
# print(d2 - d1)  # выведет: (252550130755, (2923033, 79555)), то есть 2 923 033 дней и 79 555 секунд, или 252 550 130 755 секунд в сумме


def solve(d1_raw, d2_raw) -> tuple[int, int]:
    y1, m1, d1, h1, n1, s1 = d1_raw.strip().split(' ')
    y2, m2, d2, h2, n2, s2 = d2_raw.strip().split(' ')
    start = DateToSeconds(DaysCounter(int(y1), int(m1), int(d1)).days, int(h1), int(n1), int(s1))
    end = DateToSeconds(DaysCounter(int(y2), int(m2), int(d2)).days, int(h2), int(n2), int(s2))
    # result = end - start
    # total_seconds = result[0]
    # days, seconds = result[1]
    return (end - start)[1]


def parse_file(fname) -> tuple[str, str]:
    d1 = None
    d2 = None
    with open(fname, 'r') as f:
        d1 = f.readline()
        d2 = f.readline()
    return d1, d2


def write_to_file(file_name: str, days: int, seconds: int) -> None:
    with open(file_name, 'w') as f:
        f.write(f"{days} {seconds}\n")


if __name__ == "__main__":
    import os
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.startswith('input') and f.endswith('.txt')]
    for file_name in files:
        write_to_file(f"output{file_name[5:]}", *solve(*parse_file(file_name)))

