#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.

const copyArgv = process.argv.slice(2).sort(function (a, b) { return b - a; });
const empty = Boolean(isNaN(parseInt(process.argv[2])) ||
                      process.argv[2] === undefined);

if (empty) {
  console.log(0);
} else {
  const maxNum = copyArgv[0];
  if (maxNum === '1') {
    console.log(0);
    return process.exit(1);
  }
  copyArgv.forEach((val, index) => {
    if (val !== maxNum) {
      console.log(val);
      return process.exit(1);
    }
  });
}
