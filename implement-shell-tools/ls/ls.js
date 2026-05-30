import { promises as fs } from "node:fs";

//getting all commands 
const args = process.argv.slice(2);

const showOnePerLine = args.includes("-1"); 
const showAllFilesWithHidden = args.includes("-a");

//current path
const path = args.find(arg => !arg.startsWith("-")) || ".";
// if we do console.log("path=> ",path," args=> " ,args); it will give us this =>: path=>  sample-files  args=>  [ '-1', '-a', 'sample-files' ]

try {
  const direc = await fs.readdir(path);

  // handle hidden files (-a flag controls this)
  let files = direc;

  if (!showAllFilesWithHidden) {
    files = files.filter(file => !file.startsWith("."));
  }

  // one file per line
  if (showOnePerLine) {
    files.forEach(file => {
      console.log(file);
    });
  }

  // default behavior: also one per line (simple version of ls)
  else {
    files.forEach(file => {
      console.log(file);
    });
  }

} catch (err) {
  console.error(`Error reading directory "${path}": ${err.message}`);
}


