"""
locks.py: support methods useable for locks and alike
"""

from pathlib import Path


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
