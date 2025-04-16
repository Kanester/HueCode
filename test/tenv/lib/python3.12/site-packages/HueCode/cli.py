from .encoder import Encrypt
from .decoder import Decrypt
import argparse

class Main(Encrypt, Decrypt):
  def __init__(self, data=None, path=None, filename=None):
    self.data = data
    if not self.data:
      print("Please input a proper data!")
    
    self.path = path
    self.file = filename
      
  def encrypt(self):
    Encrypt(self.data, self.path, self.file).createImg()
  
  def decrypt(self):
    return Decrypt(self.data).decrypt()

def cli_entry():
  parser = argparse.ArgumentParser(description="Encode data to image using RGB values and decode it back")
  parser.add_argument("action", choices=["encrypt", "decrypt"])
  help = "Action to perform: encrypt & decrypt"
  parser.add_argument("data", type=str, help="The given data should be any strings, integers, or mixed; it should be supported by the standard ASCII table")
  
  #For argvs
  args = parser.parse_args()
  cipher = Main(args.data)
  
  if args.action == "encrypt":
    cipher.encrypt()
    print("done!")
    
  if args.action == "decrypt":
    decrypted = cipher.decrypt()
    print(decrypted)

if __name__ == "__main__":
  cli_entry()