# from datetime import datetime

# def get_weekday(date_string):
#     date = datetime.strptime(date_string, "%Y-%m-%d")
#     return date.strftime("%A")

# print(get_weekday("2025-11-06"))

from datetime import datetime

date = datetime.strptime("2026-11-06", "%Y-%m-%d")

print(date.strftime("%A"))