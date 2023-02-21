import random
import handlers

def my_bot(num_sweet):
    if num_sweet > 28:
       return 28
    else:
       return random.randint(1,28) 