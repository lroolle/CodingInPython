""" Python ImageCaptcha validate with signature

## Requirements:

- Python3.6

```
pip install captcha
```

## Usage:

- gen_captcha: return file path and signature
- gen_captcha_base64: return png base64 and signature

"""


import os
import base64
import random
import string
from hashlib import blake2b
from hmac import compare_digest

from captcha.image import ImageCaptcha


# FONTS = (
#     os.path.join(settings.BASE_DIR, "authentication", "fonts/courier.otf"),
#     os.path.join(settings.BASE_DIR, "authentication", "fonts/dejavubold.ttf"),
# )

LENGTH = 4
AUTH_SIZE = 16
OUTDIR = "/tmp"


def sign(code, secret_key="0ec(=9)=s9rrt315r)iky27draepxl42g1hes+%hx$_9fk0*%8"):
    h = blake2b(digest_size=AUTH_SIZE, key=secret_key.encode("utf-8"))
    h.update(code.lower().encode("utf-8"))
    return h.hexdigest()


def verify_code(code, signature):
    good_signature = sign(code.lower())
    return compare_digest(good_signature, signature)


def random_text(length=4):
    return "".join(random.sample(f"{string.ascii_letters}0123456789", length))


def gen_captcha(length=None):
    length = length if length else LENGTH
    image = ImageCaptcha(width=130, height=60)  # fonts=FONTS)
    text = random_text(length)
    image.generate(text)
    code_signature = sign(text)
    fpath = os.path.join(OUTDIR, code_signature + ".png")
    image.write(text, fpath)
    return fpath, code_signature


def gen_captcha_base64(length=None):
    length = length if length else LENGTH
    image = ImageCaptcha(width=130, height=60)  # fonts=FONTS)
    text = random_text(length).lower()
    im = image.generate(text)
    code_signature = sign(text)
    b64 = base64.b64encode(im.getvalue()).decode("utf-8")
    return f"data:image/png;base64, {b64}", code_signature
