#!/usr/bin/env python3
import cowsay
import argparse

#getting avalble animal list
animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog="cowsay program",
    description="Make animals say things"
)

parser.add_argument(
    "--animal",
    default="cow",
    choices=animals,
    help=f"The animal to be saying things (choose from: {', '.join(animals)})"
)
parser.add_argument(
    "message",
    nargs="+", 
    help="message to show")

args = parser.parse_args()

text = " ".join(args.message)
animal = args.animal

getattr(cowsay, animal)(text)