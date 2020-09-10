import locale
print(locale.getpreferredencoding())


def to_str(bytes_or_str,decoder = 'utf-8'):
    if isinstance(bytes_or_str,bytes):
        value = bytes_or_str.decode(decoder) # decode is decode ascii code?
    else:
        value = bytes_or_str
    return value

print('a\u0300 propos') # the type is string with unicode points, human readable language
print(b'a\u0300 propos') # the type is bytes
print(to_str(b'a\u0300 propos')) # because it's not a bytes with byte points?
print(to_str(b'h\x65llo')) # decode is decode ascii code?

def to_bytes(bytes_or_str, encoder = 'utf-8'):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode(encoder)
    else:
        value = bytes_or_str
    return value

print(list(to_bytes('hello')))

path = './effective-py/'
with open(path + 'data.bin','wb') as f :
    print(to_str(b'\xf1',decoder='cp1252'))
    f.write(b'\xf1')

with open(path + 'data.bin', 'r',encoding='cp1252') as f:
    data = f.read()
    print(data)

with open(path + 'data.bin', 'rb') as f:
    data = f.read()
    print(data)