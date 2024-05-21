#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const tasksdict = {};

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);

    for (let i = 0; i < tasks.length; i++) {
      const key = tasks[i].userId;
      if (tasks[i].completed) {
        if (!(key in tasksdict)) {
          tasksdict[key] = 1;
        } else {
          tasksdict[key] += 1;
        }
      }
    }
  }
  console.log(tasksdict);
});
