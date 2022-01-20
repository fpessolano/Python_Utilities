"""
main.py: for testing and try outs
"""

import locks as lock

from time import sleep
from datetime import datetime

if __name__ == "__main__":
    for _ in range(3):
        if lock.detect_new_day():
            print('Execute daily routine')
        print('Execute hourly routine')
        sleep((60 - datetime.now().timetuple().tm_min) * 60)
