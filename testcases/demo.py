import random
import string

a = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(a)