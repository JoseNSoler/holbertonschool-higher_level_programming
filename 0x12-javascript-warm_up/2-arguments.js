#!/usr/bin/node

if (process.argv[2] === undefined) console.log('No Arguments');

if (process.argv[2] !== undefined && process.argv[3] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
