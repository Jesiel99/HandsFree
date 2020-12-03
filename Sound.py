import time
import sys


class Sound:

    @staticmethod
    def error():
        for i in range(1, 6):
            sys.stdout.write('\r\a{i}'.format(i=i))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\n')