import { promises as fs } from "node:fs";

const args = process.argv.slice(2);

const showLines = args.includes("-l");
const showWords = args.includes("-w");
const showChars = args.includes("-c");
let paths = args.filter(arg => !arg.startsWith("-"));
if (paths.length === 0) paths = ["."];

// helper for formatting like real wc
const pad = (n) => String(n).padStart(8, " ");

let totalLines = 0;
let totalWords = 0;
let totalChars = 0;

for (const path of paths) {
    try {
        const content = await fs.readFile(path, "utf-8");

        const lines = content.split("\n").length;
        const words = content.split(/\s+/).filter(Boolean).length;
        const chars = content.length;

        totalLines += lines;
        totalWords += words;
        totalChars += chars;

    } catch (err) {
        console.error(`Error reading file "${path}": ${err.message}`);
    }

}
if (showLines) {
    console.log("lines:", totalLines);
}

if (showWords) {
    console.log("words:", totalWords);
}

if (showChars) {
    console.log("chars:", totalChars);
}


// default output when no flags
if (!showLines && !showWords && !showChars) {
    console.log(
    `${pad(totalLines)}\t${pad(totalWords)}\t${pad(totalChars)}\ttotal`
  );
}


