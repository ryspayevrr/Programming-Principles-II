from datetime import datetime, timedelta, date

# 1


current = datetime.now()

print(current)

new = current - timedelta(days = 5)

print("Date 5 days ago:", new)


print("\n")


# 2

today = date.today()

yesterday = today - timedelta(days = 1)

tomorrow = today + timedelta(days = 1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

print("\n")


# 3

now = datetime.now()

without_mcrseconds = now.replace(microsecond=0)

print("Original:", now)
print("Without microseconds:", without_mcrseconds)

print("\n")


# 4


date1 = datetime(2026, 2, 14, 10, 0, 0)
date2 = datetime(2026, 2, 17, 12, 30, 0)

seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", seconds)
