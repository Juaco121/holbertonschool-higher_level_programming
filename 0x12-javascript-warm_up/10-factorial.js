#!/usr/bin/node
// Computes and prints a factorial recursively

const num = parseInt(process.argv[2]);

function factorial (num) {
  if (Number.isNaN(num) || num === 0) {
    return (1);
  }
  if (num < 0) {
    return (-1);
  }
  return (num * factorial(num - 1));
}

console.log(factorial(num));
