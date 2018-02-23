##########################
##### PROOF OF WORK ######
##########################

import hashlib
import time





# how many prefix zeross
difficulty = 1

# target string with number of zeros
target = ''.join(['0' for s in range(difficulty)])





# Look for the nonce
def nonce_get(my_hash):
    nonce = 0
    temp = my_hash
    while not temp[0:difficulty] == target:
        sha = hashlib.sha256()
        nonce += 1
        m = str(my_hash) + str(nonce)
        sha.update(m.encode())
        temp = sha.hexdigest()
    return nonce





# Verifies a given nonce
def verify_nonce(my_hash, nonce):
    sha = hashlib.sha256()
    m = str(my_hash) + str(nonce)
    sha.update(m.encode())
    compare_hash = sha.hexdigest()
    if compare_hash[0:difficulty] == target:
        print("The new hash is:", compare_hash)
        print("Valid nonce")
        return True
    else:
        print("Not a valid nonce")
        return False




# check how much time has elapsed
def elapsed_time(start_time, end_time):
    return end_time - start_time

# SANDBOX----------------------------------------------------------------------

# start the clock
time_test = float(time.time())




# Transaction object
# {
sender = "Satoshi Nakamoto"
recipient = "Charlie Lee"
amount = "1000000"
# }




# Hash object
sha = hashlib.sha256()
m = str(sender) + str(recipient) + str(amount) + str(time_test)
sha.update(m.encode())
test_hash = sha.hexdigest()




# original hash
print("The original hash is:", test_hash)



print("Seeking nonce...")

# retrieve hash
my_nonce = nonce_get(test_hash)

print("Nonce found!")




# stop the clock
time_diff = elapsed_time(time_test, float(time.time()))


# Analysis
print("Time it took to find the nonce:", time_diff)

print("The nonce is:", my_nonce)



# verify the nonce
verify_nonce(test_hash,my_nonce)
