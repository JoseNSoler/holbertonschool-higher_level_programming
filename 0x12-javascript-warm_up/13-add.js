#!/usr/bin/node
// Prints the sum of two arguments/values - global scope

exports.add = function (x, y) {
  const empty = Boolean(isNaN(parseInt(x)) ||
                        x === undefined ||
                        isNaN(parseInt(y)) ||
                        y === undefined);

  if (empty) {
    return (NaN);
  } else {
    return (parseInt(x) + parseInt(y));
  }
};
