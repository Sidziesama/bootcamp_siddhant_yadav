import numpy as np 
import os
from dotenv import load_dotenv

def load_env():
    
    load_dotenv()
    key = os.getenv("API_KEY")
    return bool(key)

print(load_env())
