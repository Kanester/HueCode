from enum import Enum

class constants(Enum):
  SF = 50
  BC = (0,0,0)
  
  CF = 30
  rgbC = ["R", "G", "B"]
  CS = {
    "R": 50,
    "G": 80,
    "B": 140
  }
  
  metadata = '''
  {
    "version": {version},
    "metadata": {
      "Title": "{title}",
      "Description": "{desc}",
      "Author": "KanesterP-HC-v1",
      "Date": "{date}"
    },

    "image": {
      "pixels": {
        "height": {height},
        "width": {height},
        "mode": "RGB"
      },
      "data": "{data}",
      "checksum": "{checksum}"
    }
  }
  '''