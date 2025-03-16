import uuid

import pytest
from uuid7 import uuid7


def test_uuid7():
    uuid_obj = uuid7()
    assert uuid_obj.version == 7
    assert uuid_obj.variant == uuid.RFC_4122
    assert len(str(uuid_obj)) == 36


def test_uuid_uniqueness():
    uuids = {uuid7() for _ in range(100000)}
    assert len(uuids) == 100000


def extract_timestamp(uid: uuid.UUID) -> int:
    # UUIDv7 timestamp is the first 6 bytes (48 bits)
    return int.from_bytes(uid.bytes[:6], byteorder='big')


def test_uuid_timestamps_are_monotonic():
    uuids = [uuid7() for _ in range(3)]
    timestamps = [extract_timestamp(uid) for uid in uuids]

    assert timestamps[0] <= timestamps[1] <= timestamps[2], \
        f"Timestamps are not monotonic: {timestamps}"
