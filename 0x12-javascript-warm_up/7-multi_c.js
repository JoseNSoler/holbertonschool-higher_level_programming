#!/usr/bin/node

if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let x = parseInt(process.argv[2]); x > 0; x--) console.log('C is fun');
}
