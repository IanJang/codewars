// https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot/train/javascript
const assert = require('assert');

function isBalanced(s, caps) {
    var i, stack = [];

    for (var c of s) {
        i = caps.indexOf(c);

        if (i === -1)
            continue;

        else if (stack.length && stack[0] === caps.lastIndexOf(c) - 1)
            stack.shift();

        else
            stack.unshift(i);
    }

    return !stack.length
}

assert.equal(isBalanced("(Sensei says yes!)", "()"), true);
