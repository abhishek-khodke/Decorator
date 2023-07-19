# def decor(func):
#     def inner(name):
#         if name=="abhishek":
#             print("Hello abhishek good morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("hello", name, "Good afternoon")

# wish("abhi")

# import time
# # import datetime

# def calculate_time(func):
#     def inner(*args):
#         t1 = time.time()
#         func(*args)
#         t2 = time.time()
#         print(f"Time taken by {func.__name__} function is {t2 - t1}")
#     return inner



# @calculate_time
# def get_even_values(*args):
#     lst = []
#     for i in range(1, 6):
#         time.sleep(1)
#         if i % 2 == 0:
#             lst.append(i)
#     print(lst)

# get_even_values()

# import time

# def calculate_time(func):
#     def inner(*args):
#         t1 = time.time()
#         func(*args)
#         t2 = time.time()
#         print(f"time taken by {func.__name__} function is {t2- t1}")

#     return inner

# @calculate_time
# def get_even_number(*args):
#     lst=[]
#     for i in range(1, 6):
#         time.sleep(1)
#         if i % 2 == 0:
#             lst.append(i)
#     print(lst)

# get_even_number()

# import time
# import datetime

# def calculate_time(func):
#     def inner(*args):
#         t1 = time.time()
#         func(*args)
#         t2 = time.time()
#         print(f"Time take by {func.__name__} function is {round(t2 - t1, 2)}")
#         print(round(t2-t1, 2))
#     return inner


# @calculate_time

# def get_even_number(*args):
#     lst = [] 
#     for i in range(1, 6):
#         time.sleep(1)
#         if i % 2 == 0:
#             lst.append(i)

#     print(lst)

# # t1 = time.time()
# get_even_number()
# # t2 = time.time()

# # print(round(t2-t1, 2))
