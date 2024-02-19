#------------------------ Threads ----------------------

# from threading import Thread

# class InputReader(Thread):
#     def run(self):
#         self.line_of_text = input()

# print("Enter some text and then enter.")
# thread = InputReader()
# thread.run()

# count = result = 1

# while thread.is_alive():
#     result = count * count
#     count += 1

# print("calculate squares upto {0} * {0} = {1}".format(count,result))
# print("While you type '{}'.".format(thread.line_of_text))


# --------- Checking temperature of every city in a state

# from threading import Thread
# import time,json
# from urllib.request import urlopen

# CITIES = [
#     'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton', 
#     "St. John's", 'Halifax', 'Toronto', 'Charlottetown',
#     'Quebec City', 'Regina'
# ]

# class TempGetter(Thread):
#     def __init__(self, city):
#         super().__init__()
#         self.city = city

#     def run(self):
#         url_template = (
#             'http://api.openweathermap.org/data/2.5/'
#             'weather?lat=33.44&lon=-94.04&put my api key here')
#         response = urlopen(url_template)
#         data = json.loads(response.read().decode())
#         self.temperature = data["main"]["temp"]

# threads = [TempGetter(c) for c in CITIES]
# start = time.time()
# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# for thread in threads:
#     print(
#         "it is {0.temperature:.0f}°C in {0.city}".format(thread))
# print(
#     "Got {} temps in {} seconds".format(
#     len(threads), time.time() - start))