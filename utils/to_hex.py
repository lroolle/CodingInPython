
to_hex = lambda x: ''.join([hex(ord(c))[2:].zfill(2) for c in x]).zfill(24)

unhex = lambda x: x and chr(int(x[:2], base=16)) + unhex(x[2:]) or ''

