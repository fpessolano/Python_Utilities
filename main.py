"""
xxx.py: abc
"""

from pathlib import Path
from datetime import datetime
from time import sleep


def detect_new_day(lock_file: Path = Path('.daylock')):
    day_of_the_year = datetime.now().timetuple().tm_yday
    new_day = True
    if lock_file.exists():
        with open(lock_file, 'r') as file:
            lock = int(file.read())
            new_day = lock != day_of_the_year
            if new_day:
                with open(lock_file, 'w') as file:
                    file.write(str(day_of_the_year) + '\n')
    else:
        with open(lock_file, 'w') as file:
            file.write(str(day_of_the_year) + '\n')

    return new_day


if __name__ == "__main__":
    for _ in range(3):
        if detect_new_day():
            print('Execute daily routine')
        print('Execute hourly routine')
        sleep((60 - datetime.now().timetuple().tm_min) * 60)
