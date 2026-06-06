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

total_lines = 0
total_words = 0
total_chars = 0

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
            
            output_parts = []
            if args.l:
                output_parts.append(f"{line_count:>7}")
            if args.w:
                output_parts.append(f"{word_count:>7}")
            if args.c:
                output_parts.append(f"{char_count:>7}")
                
            if not args.w and not args.l and not args.c:
                print(f"{line_count:>7}{word_count:>7}{char_count:>7} {file}")
            else:
                output_parts.append(f" {file}")
                print("".join(output_parts))
            
    except FileNotFoundError:
        print(f"wc: {file}: open: No such file or directory")

if len(args.files) > 1:
    total_parts = []
    if args.l:
        total_parts.append(f"{total_lines:>7}")
    if args.w:
        total_parts.append(f"{total_words:>7}")
    if args.c:
        total_parts.append(f"{total_chars:>7}")
        
    if not args.w and not args.l and not args.c:
        print(f"{total_lines:>7}{total_words:>7}{total_chars:>7} total")
    else:
        total_parts.append(" total")
        print("".join(total_parts))
