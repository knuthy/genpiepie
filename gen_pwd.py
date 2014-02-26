#!/usr/bin/python

import Crypto.Hash.SHA256 as sha
import sys
import getpass

def gen_pwd(user,web,sym1=None,sym2=None,key=None):
    """
    """
    if not key:
        key = getpass.getpass('Input the KEY: ')

    if not sym1:
        sym1 = getpass.getpass('Input the first symbol: ')

    if not sym2:
        sym2 = getpass.getpass('Input the first symbol: ')

    h = sha.new()
    h.update(key.encode('utf-8'))
    h.update(user.encode('utf-8'))
    h.update(u'@')
    h.update(web.encode('utf-8'))
    digest = h.hexdigest()
    return "{}{}{}{}{}".format(
            digest[:4],
            sym1,
            digest[8:12],
            sym2,digest[-4:] 
            )

def main(argv=None):
    if len(argv) < 3:
        print("Usage: {} username website".format(argv[0]))
        return 1
    username = argv[1]
    website = argv[2]
    print(gen_pwd(username, website))

if __name__ == "__main__":
    sys.exit(main(sys.argv))