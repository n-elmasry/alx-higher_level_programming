#!/usr/bin/node
const args = process.argv.slice(2);
const number = parseInt(args[0]);
function factorial (number) {
  if (isNaN(number) || number < 1) {
    return (1);
  }
  return (number * factorial(number - 1));
}

console.log(factorial(number));
