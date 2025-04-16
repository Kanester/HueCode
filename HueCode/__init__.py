"""HueCode: An encoder that turns text into image and decode image to text using RGB channels"""

__version__ = "1.0.1"

from .encoder import Encrypt
from .decoder import Decrypt

def encrypt(data, path=None, filename=None, title="HueCode", desc="No Description"):
  Encrypt(data, path, filename, title, desc).createImg()
  return
  
def decrypt(path):
  return Decrypt(path).decrypt()
