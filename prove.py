import os
import sys
import time

timer = 0
loading = "Loading: [----------]"
backtrack = '\b'*len(loading)

while timer < 11:
    sys.stdout.write(backtrack + loading)
    sys.stdout.flush()
    loading = loading.replace("-","=",1)
    time.sleep(1)
    timer += 1
time.sleep(1)
sys.stdout.write(backtrack)
print (loading+" Complete!")