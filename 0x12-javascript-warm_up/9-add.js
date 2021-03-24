#!/usr/bin/node
// Prints the sum of two arguments/values

const empty = Boolean(isNaN(parseInt(process.argv[2])) ||
                       process.argv[2] === undefined ||
                       isNaN(parseInt(process.argv[3])) ||
                       process.argv[3] === undefined);

if (empty) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
