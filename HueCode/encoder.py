from .constants import constants
from PIL import Image, ImageDraw
import base64, math, os, zlib

class Encrypt:
  def __init__(self, data, path, filename):
    self.path = path
    if self.path is None:
      self.path = os.getcwd()
    
    self.filename = filename
    if self.filename is None:
      self.filename = "output.png"
    
    self.data = data
    self.SCALE = constants.SF.value
    self.COLORB = constants.BC.value
    self.COLORF = constants.CF.value
    self.CHANNELS = constants.rgbC.value
    self.SHIFTS = constants.CS.value

  def ToBase85(self):
    data = self.data.encode("utf8")
    encoded_data = base64.b85encode(data).decode("utf8")
    
    return encoded_data
  
  def ToRGB(self, ascii_value, channel):
    shift_value = self.SHIFTS[channel]
    return int(((ascii_value * shift_value + self.COLORF) / (127* shift_value + self.COLORF))*255)
      
  def Concat(self):
    rgb_values = []
    rgb = [0,0,0]
    chnnx = 0
    
    base85data = self.ToBase85()

    for chnx in base85data:
      ascii_value = ord(chnx)
      channel = self.CHANNELS[chnnx]
      rgb[chnnx] = self.ToRGB(ascii_value, channel)
      chnnx += 1
        
      if chnnx == 3:
        rgb_values.append(tuple(rgb))
        rgb = [0,0,0]
        chnnx = 0
        
    if chnnx != 0:
      for i in range(chnnx, 3):
        rgb[i] = 0
      rgb_values.append(tuple(rgb))
        
      return rgb_values

  def createImg(self):
      rgb_array = self.Concat()
      pixels = len(rgb_array)
      limit = math.ceil(math.sqrt(pixels))
      rows = math.ceil(pixels / limit)
      height = rows * self.SCALE
      width = limit * self.SCALE
        
      image = Image.new("RGB", (width, height), self.COLORB)
      draw = ImageDraw.Draw(image)
        
      for i, rgb in enumerate(rgb_array):
          row = i // limit
          col = i % limit
          x0 = col * self.SCALE 
          y0 = row * self.SCALE 
          x1 = (col + 1) * self.SCALE
          y1 = (row + 1) * self.SCALE
          draw.rectangle([x0, y0, x1, y1], fill=rgb)
      
      path = os.path.join(self.path, self.filename)
      
      image.save(path)
      print(zlib.__doc__)
