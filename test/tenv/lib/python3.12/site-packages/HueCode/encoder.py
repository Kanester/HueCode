from .constants import constants
from PIL import Image, ImageDraw
from datetime import datetime
import base64, math, os, zlib, hashlib


class Encrypt:
	def __init__(self, data, path, filename, title, desc):
		self.path = path if path is not None else os.getcwd()
		self.filename = filename if filename is not None else "output.png"
		self.title = title if title is not None else "HueCode"
		self.desc = desc if desc is not None else "No description."
		self.data = data
		self.SCALE = constants.SF.value
		self.COLORB = constants.BC.value
		self.COLORF = constants.CF.value
		self.CHANNELS = constants.rgbC.value
		self.SHIFTS = constants.CS.value
		self.TEMPLATE = constants.metadata.value

	def generateMetadata(self, height, width, b85data, checksums):
		metadata = self.TEMPLATE.format(
			version=1,
			title=self.title,
			desc=self.desc,
			date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			height=height,
			width=width,
			data=b85data,
			checksum=checksums,
		)
		return metadata

	def ToBase85(self):
		data = self.data.encode("utf8")
		compress = zlib.compress(data)
		encoded_data = base64.b85encode(compress)
		checksum = hashlib.sha256(encoded_data).hexdigest()
		encoded_data.decode("utf8")
		
		return encoded_data, checksum

	def ToRGB(self, ascii_value, channel):
		shift_value = self.SHIFTS[channel]
		return int(
			((ascii_value * shift_value + self.COLORF) / (127 * shift_value + self.COLORF))
			* 255
		)

	def Concat(self, data):
		rgb_values = []
		rgb = [0, 0, 0]
		chnnx = 0

		for chnx in data:
			ascii_value = ord(chnx)
			channel = self.CHANNELS[chnnx]
			rgb[chnnx] = self.ToRGB(ascii_value, channel)
			chnnx += 1

			if chnnx == 3:
				rgb_values.append(tuple(rgb))
				rgb = [0, 0, 0]
				chnnx = 0

		if chnnx != 0:
			for i in range(chnnx, 3):
				rgb[i] = 0
			rgb_values.append(tuple(rgb))

		return rgb_values

	def createImg(self):
		base85, checksum = self.ToBase85()

		tmp_metadata = self.generateMetadata(0, 0, base85, checksum)

		tmp_rgb = self.Concat(tmp_metadata)

		pixels = len(tmp_rgb)
		limit = math.ceil(math.sqrt(pixels))
		rows = math.ceil(pixels / limit)
		height = rows * self.SCALE
		width = limit * self.SCALE

		final_metadata = self.generateMetadata(height, width, base85, checksum)
		rgb_array = self.Concat(final_metadata)

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
		return f"Done Cooking!\n path: {path}"
