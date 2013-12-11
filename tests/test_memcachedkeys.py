from memcachedkeys import make_key


def test_short():
    key = 'A' * 241
    full_key = 'prefix:1:%s' % key
    assert full_key == make_key(key, 'prefix', 1)

def test_long():
    key = 'A' * 242
    hashed_key = '%s[865768d1a3bbc7e33c749dc133260242]' % ('A' * 207)
    full_key = 'prefix:1:%s' % hashed_key
    assert full_key == make_key(key, 'prefix', 1)

def test_space():
    assert make_key('hello world', 'prefix', '1') == 'prefix:1:helloworld[5eb63bbbe01eeed093cb22bb8f5acdc3]'
