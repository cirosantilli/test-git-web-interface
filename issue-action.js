#!/usr/bin/env node
console.log('Starting action.js')
const github = require('@actions/github');
const payload = github.context.payload
console.log(payload)
