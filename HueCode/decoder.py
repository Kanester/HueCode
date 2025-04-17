from PIL import Image
from .constants import constants
import base64


class Decrypt:
	def __init__(self, path):
		self.path = path
		self.SCALE = constants.SF.value
		self.FACTOR = constants.CF.value
		self.SHIFT = constants.CS.value
		self.CHANNELS = constants.rgbC.value

	def getInfo(self):
		image = Image.open(self.path)

		if image.mode != "RGB":
			image = image.convert("RGB")

		downscaled = image.resize(
			(image.width // self.SCALE, image.height // self.SCALE), resample=Image.NEAREST
		)
		pixel = downscaled.load()
		width, height = downscaled.size

		pixels = [pixel[x, y] for y in range(height) for x in range(width)]

		return pixels, width, height

	def reverse(self, color, channel):
		shift_value = self.SHIFT[channel]

		return round(
			(((color / 255) * (127 * shift_value + self.FACTOR)) - self.FACTOR) / shift_value
		)

	def decrypt(self):
		pixels, width, height = self.getInfo()
		orig = []

		for i, (r, g, b) in enumerate(pixels):
			if all(v == 0 for v in (r, g, b)):
				break

			for chnnx in range(0, 3):
				rgb = pixels[i][chnnx]
				channel = self.CHANNELS[chnnx]
				originalVal = self.reverse(rgb, channel)
				orig.append(originalVal)

				if channel == 3:
					channel = 0

		base85data = b"".join(chr(val).encode("utf-8") for val in orig if val != 0)
		print(base85data)
		# decoded = base64.b85decode(base85data)
		# message = decoded.decode("utf-8")
		# return message
