from twisted.scripts.twistd import run
from os.path import join, dirname
from sys import argv
import nest.application

if __name__ == '__main__':
    argv[1:1] = ['-n', '-y', join(dirname(nest.application.__file__), 'app.py')]
    print(argv)
    run()
