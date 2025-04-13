"""HueCode: An encoder that turns text into image and decode image to text using RGB channels"""

__version__ = "0.1.0"

from .encoder import Encrypt
from .decoder import Decrypt

def encrypt(data, path, filename):
  Encrypt(data, path, filename).createImg()
  return
  
def decrypt(path):
  return Decrypt(path).decrypt()