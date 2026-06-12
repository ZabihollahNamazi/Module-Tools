import argparse
import os

parser = argparse.ArgumentParser(
    prog="wc shell tool",
    description="making wc tool with python"
)

parser.add_argument(
    "files",
    nargs="+",
    help="file or files to work on"
)
parser.add_argument(
    "-w",
    action="store_true",
    help="counting words"
)
parser.add_argument(
    "-l",
    action="store_true",
    help="counting lines"
)
parser.add_argument(
    "-c",
    action="store_true",
    help="counting char"
)

args = parser.parse_args()

show_all = not (args.l or args.w or args.c)
total_lines = 0
total_words = 0
total_chars = 0

def format_output(lines, words, chars, label):
    output_parts = []
    
    # If the specific flag is requested, or no flags were passed at all
    if args.l or show_all:
        output_parts.append(f"{lines:>7}")
    if args.w or show_all:
        output_parts.append(f"{words:>7}")
    if args.c or show_all:
        output_parts.append(f"{chars:>7}")
        
    return "".join(output_parts) + f" {label}"

for file in args.files:
    try:
        if os.path.isdir(file):
            print(f"wc: {file}: read: Is a directory")
            continue
            
        with open(file, "rb") as f:
            content = f.read()
            word_count = len(content.decode('utf-8', errors='ignore').split())
            line_count = content.count(b"\n")
            char_count = len(content)
            
            total_lines += line_count
            total_words += word_count
            total_chars += char_count
            
            print(format_output(line_count, word_count, char_count, file))
            
    except FileNotFoundError:
        print(f"wc: {file}: open: No such file or directory")

if len(args.files) > 1:
    print(format_output(total_lines, total_words, total_chars, "total"))
