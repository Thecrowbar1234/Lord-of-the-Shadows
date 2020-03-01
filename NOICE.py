from os import system, name
import sys
import time

def clear(): 
  if name == 'nt': 
    _ = system('cls') 
  else: 
    _ = system('clear') 
    
def state(text):
  text += '\n'
  for char in text :
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.005)
  
