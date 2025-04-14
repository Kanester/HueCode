# HueCode

![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
![Made with](https://img.shields.io/badge/made%20with-curiosity-ff69b4)

A simple, fun project built out of curiosity in just a week.

**HueCode** is a steganography system that uses the RGB color channel to **encrypt** and **decrypt** data in visual form.

> [!NOTE]
> **Disclaimer:** This is just a personal experimental project created by a Senior High School ABM student.

## Installation

To install this mess, download the compiled Python package, then run:

```bash
pip install huecode-<version>.tar.gz
```

Dependencies: It only needs [Pillow](https://python-pillow.github.io/) to work.

## Usage

Mhm... I dunno, just use it for anything you like. It doesn’t have a concrete use case yet since it’s still experimental.
So—yeah, do whatever you want. Here's an example of how to use it:

```python
from huecode import encode, decode

# Encoding your message into an image
encode("Hello, world!", path="/path/to/file/", filename="filename.png")

# Default value of path is the current working directory and the default filename is "output.png"

# Decoding the message from the image
message = decode("output.png")
print(message)  # → Hello, world!
```

## Contributing

Please help me make this mess useful
(╥﹏╥) plz
