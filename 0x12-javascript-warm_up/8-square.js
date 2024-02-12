#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[0]); i++) {
    let row = '';
    for (let j = 0; j < parseInt(args[0]); j++) {
      row += 'X';
    }
    console.log(row);
  }
}
