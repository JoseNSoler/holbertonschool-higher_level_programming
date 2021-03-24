#!/usr/bin/node
// Factorial recursion

function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const empty = Boolean(isNaN(parseInt(process.argv[2])) ||
                      process.argv[2] === undefined);
if (empty) {
  console.log(1);
} else {
  const result = factorial(parseInt(process.argv[2]));
  console.log(`${result}`);
}
