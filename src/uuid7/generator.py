#
#     DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#            Version 2, December 2004
#
#  Copyright (C) 2025 0xShamil
#
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
#
#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. You just DO WHAT THE FUCK YOU WANT TO.
#

import os
import time
import uuid


def uuid7() -> uuid.UUID:
    timestamp = int(time.time() * 1000).to_bytes(6, byteorder='big')
    rand_bytes = bytearray(os.urandom(10))

    rand_bytes[0] = (rand_bytes[0] & 0x0F) | 0x70  # Version 7
    rand_bytes[2] = (rand_bytes[2] & 0x3F) | 0x80  # Variant RFC 4122

    return uuid.UUID(bytes=timestamp + rand_bytes)
