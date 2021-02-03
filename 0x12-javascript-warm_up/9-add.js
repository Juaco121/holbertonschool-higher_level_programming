#!/usr/bin/node
// Prints the addition of 2 integers

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add (a, b) {
    let res = a + b;
    return res;
}

console.log(add(a, b));
