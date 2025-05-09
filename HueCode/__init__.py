"""HueCode: An encoder that turns text into image and decode image to text using RGB channels"""

__version__ = "1.0.2"

from .encoder import Encrypt
from .decoder import Decrypt

def encrypt(data, path=None, filename=None, title=None, desc=None):
  return Encrypt(data, path, filename, title, desc).createImg()
  
  
def decrypt(path):
  return Decrypt(path).decrypt()
