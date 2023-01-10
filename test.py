import argparse

parser = argparse.ArgumentParser(description='Auto Order HKJC MarkSix')
parser.add_argument('--order', help='買入六合彩', action='store_true')
args = parser.parse_args()

if args.order:
    print(args.order)
else:
    print(args.order)