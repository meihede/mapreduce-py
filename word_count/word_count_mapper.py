#!/usr/bin/env python3

import sys
import socket


class Mapper:
    def __init__(self):
        self.count = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)

    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)

    def map(self):
        self._log('mapping ...')
        for line in sys.stdin:
            line = line.strip()
            self._log(line)
            words = line.split()
            for word in words:
                print('{}\t{}'.format(word, 1))


def main(argv):
    mapper = Mapper()
    mapper.map()


if __name__ == "__main__":
    main(sys.argv[:1])
