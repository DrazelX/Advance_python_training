# run by command line
import argparse

parse = argparse.ArgumentParser(description="test")

parse.add_argument('count', action='store', type=int)
parse.add_argument('units', action='store')
parse.add_argument('material', action='store')

print(parse.parse_args())