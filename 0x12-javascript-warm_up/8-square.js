#!/usr/bin/node

if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let x = parseInt(process.argv[2]); x > 0; x--) {
    let line = '';
    for (let x = parseInt(process.argv[2]); x > 0; x--) line += 'X';
    console.log(line);
  }
}
