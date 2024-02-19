#------------------------ Threads ----------------------

from threading import Thread

class InputReader(Thread):
    def run(self):
        self.line_of_text = input()

print("Enter some text and then enter.")
thread = InputReader()
thread.run()

count = result = 1

while thread.is_alive():
    result = count * count
    count += 1

print("calculate squares upto {0} * {0} = {1}".format(count,result))
print("While you type '{}'.".format(thread.line_of_text))
