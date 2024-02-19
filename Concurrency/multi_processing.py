#---------------------- Multi-Processing------------

# from multiprocessing import Process, cpu_count
# from threading import Thread
# import time
# import os

# class MuchCPUProcess(Process):
#     def run(self):
#         print(os.getpid())
#         for i in range(200000000):
#             pass

# class MuchCPUThread(Thread):
#     def run(self):
#         print(os.getpid())
#         for i in range(200000000):
#             pass

# if __name__ == "__main__":
#     procs = [MuchCPUProcess() for f in range(cpu_count())]
#     start = time.time()
#     for proc in procs:
#         proc.start()
#     for proc in procs:
#         proc.join()

#     print("Work Time: {}".format(time.time() - start))


#----------------- Multi-Processing Pool ------------------

# from multiprocessing.pool import Pool
# import random

# def prime_factors(value):
#     factors = []
#     for divisor in range(2,value-1):
#         quotient, remainder = divmod(value,divisor)
#         if not remainder:
#             factors.extend(prime_factors(divisor))
#             factors.extend(prime_factors(quotient))
#             break
#         else:
#             factors = [value]
#     return factors

# if __name__ == "__main__":
#     pool = Pool()

#     to_factor = [random.randint(100000,50000000) for _ in range(20)]
#     results = pool.map(prime_factors,to_factor)
#     for value, factors in zip(to_factor,results):
#         print("The Factors of {} are {}".format(value,factors))