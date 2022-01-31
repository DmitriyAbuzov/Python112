import time

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)
import locale
locale.setlocale(locale.LC_ALL, "")

print(time.strftime("Сегодня: %B %d, %Y", time.localtime()))