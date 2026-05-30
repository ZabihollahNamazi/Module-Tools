import { promises as fs } from "node:fs";

// get all command line arguments after "node cat.js" - like -n or -b
const args = process.argv.slice(2);

// put them in variables
const showAllNumbers = args.includes("-n");
const showNonEmptyNumbers = args.includes("-b");

// getting the paths of files
const paths = args.filter(arg => arg !== "-n" && arg !== "-b");

// helper: mimic real cat line number formatting
const padLineNumber = (num) => String(num).padStart(6, " ");

// loop over each file
for (const path of paths) {
  try {
    // read file as text
    const content = await fs.readFile(path, "utf-8");

    // split them into lines
    const lines = content.split("\n");

    let lineNumber = 1; // tracks line numbers for -b and -n

    for (const line of lines) {
      if (showNonEmptyNumbers) {
        // -b: number only non-empty lines
        if (line !== "") {
          console.log(`${padLineNumber(lineNumber)}  ${line}`);
          lineNumber++;
        } else {
          console.log(line); // shows empty line with no number
        }
      } else if (showAllNumbers) {
        // -n: number all lines
        console.log(`${padLineNumber(lineNumber)}  ${line}`);
        lineNumber++;
      } else {
        // no flags: just print line
        console.log(line);
      }
    }
  } catch (err) {
    console.error(`Error reading file "${path}": ${err.message}`);
  }
}