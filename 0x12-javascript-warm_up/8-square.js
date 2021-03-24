#!/usr/bin/node
const arr = [];

if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let x = parseInt(process.argv[2]);
  let string = '';

  while (x > 0) {
    arr.push('x');
    x--;
  }
  arr.forEach((element) => {
    string += element;
  });
  arr.forEach((element) => {
    console.log(string);
  });
}
