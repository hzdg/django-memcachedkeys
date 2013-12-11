from memcachedkeys.pkgmeta import *
import re
from hashlib import md5


bad_key_chars = re.compile(ur'[\u0000-\u001f\s]+')
MAX_LENGTH = 250


def make_key(key, key_prefix, version):
    """
    Makes a memcached-safe cache key. Use as a KEY_FUNCTION

    """
    clean_key = bad_key_chars.sub('', key)
    version_str = str(version)
    full_key = ':'.join([key_prefix, version_str, clean_key])

    if clean_key != key or len(full_key) > MAX_LENGTH:
        hashed_key = md5(key).hexdigest()
        abbrev_keylen = MAX_LENGTH - len(hashed_key) - len('::[]') - len(key_prefix) - len(version_str)
        new_key = '%s[%s]' % (clean_key[:abbrev_keylen], hashed_key)
        full_key = ':'.join([key_prefix, version_str, new_key])

    return full_key
