#!/usr/bin/env python

from __future__ import print_function

import argparse
import binascii
import os
import sys

try:
    import nacl
except ImportError:
    print("pynacl must be installed. do 'pip install pynacl'.")
    sys.exit(1)

from nacl.public import PublicKey, PrivateKey, Box

SERVER_SECRET_KEY_FILE = "server_secret_key"

def create_parser():
    parser = argparse.ArgumentParser();
    parser.add_argument("-k", "--keyfile",
                        help="A file containing the server's hex-encoded secret NaCl key")
    parser.add_argument("-r", "--report",
                        help="A hex-encoded, encrypted report.")
    parser.add_argument("-n", "--nonce",
                        help="A hex-encoded nonce.")
    parser.add_argument("-c", "--reporterkey",
                        help="The reporter's hex-encoded public NaCl key")
    return parser

def from_hex(thing):
    return binascii.a2b_hex(thing)

def to_hex(thing):
    return binascii.b2a_hex(thing)

def decode_server_secret_key(keyfile):
    keyfile = keyfile or SERVER_SECRET_KEY_FILE
    sk = None
    with open(keyfile) as fh:
        hex = fh.read()
        sk = PrivateKey(from_hex(hex.strip()))
    return sk

def decode_reporter_key(key):
    return PublicKey(from_hex(key))

def decode_report(report, reporterkey, nonce, keyfile):
    pk = decode_reporter_key(reporterkey)
    sk = decode_server_secret_key(keyfile)
    nonce = from_hex(nonce)
    ciphertext = from_hex(report)
    box = Box(sk, pk)
    plaintext = box.decrypt(ciphertext, nonce)
    return plaintext
    
def test():
    pk = decode_reporter_key("4e9921b2ce590bffdbd31627b60e8e1ebd2603222381a99565488833ded2cf3e")
    nonce = from_hex("ede1604557223f4a50bbc667647d6baeaeae4cf6f86e7079")
    ciphertext = from_hex("6a9b95f98cf70c4ae2f50364375d833dd807448b90aa1db80329a3db08564c147e8325029850f2586079eec7640c01ab96bb85305a47d0ea0c3df585")
    sk = decode_server_secret_key(None);
    box = Box(sk, pk)
    plaintext = box.decrypt(ciphertext, nonce)
    print(plaintext)

def doit():
    parser = create_parser()
    args = parser.parse_args()

    if not (args.reporterkey and args.nonce and args.report):
        print("Missing report or reporterkey or nonce.\n")
        sys.exit(1)

    keyfile = args.keyfile or None
    report = decode_report(args.report, args.reporterkey, args.nonce, keyfile)
    if report:
        print(report)
        sys.exit(0)

    print("Could not decrypt report!")
    sys.exit(1)

if __name__ == "__main__":
    #test()
    doit()
