import random
import handlers

def my_bot(remainder_sweet):
    if remainder_sweet > 28:
       return random.randint(1,28)
    else:
       return remainder_sweet 