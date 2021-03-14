import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""

    #lisää loppuun välilyöntejä
    s = s.ljust(1000-origlen)

    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError

    #FAILED test_mycrypt.py::test_invalid_char[\xe5\xe4\xf6] - Failed: DID NOT RAISE <class 'ValueError'>
    if ('å' or 'ä' or 'ö') in s:
        raise ValueError
    #FAILED test_mycrypt.py::test_invalid_char[+] - Failed: DID NOT RAISE <class 'ValueError'>
    if '+' in s:
        raise ValueError

    for c in s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            crypted+=digitmapping[c]
            #toimii muuten paitsi se kusee encryptauksen testauksen koska niissä on lopussa pisteitä
    #crypted = crypted.ljust(1000-origlen,".")

    #poista lopuksi välilyönnit
    crypted = crypted.rstrip()
    return crypted

def decode(s):
    #FAILED test_mycrypt.py::test_encode_decode[123] - assert '!"#' == '123'
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            decrypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
            decrypted+=digitmapping[c]
    #decrypted = decrypted.rstrip(".")
    return decrypted
