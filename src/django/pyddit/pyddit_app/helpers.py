# coding: utf-8

import hashlib
import base64

def create_hashed_url(title):
    return base64.urlsafe_b64encode(
        hashlib.md5(title).digest()
    )