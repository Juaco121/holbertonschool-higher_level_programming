#!/usr/bin/node
// Prints x times 'C is fun'

const times = parseInt(process.argv[2]);
if (times) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
