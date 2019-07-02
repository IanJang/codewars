// https://www.codewars.com/kata/checking-groups/train/javascript
const assert = require('assert');

function groupCheck(s){
    // console.log(s);
    const open_close_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    };
    let stack = [];
    for (c of s) {
        // open
        if (Object.keys(open_close_map).indexOf(c) !== -1) {
            stack.unshift(c);
        }
        // close
        else if (Object.values(open_close_map).indexOf(c) !== -1) {
            if (stack.length && open_close_map[stack[0]] === c) {
                stack.shift();
            }
            else
                return false
        }
    }
    return !stack.length;
}

assert.equal(groupCheck("()"), true);
assert.equal(groupCheck("{(})"), false);
assert.equal(groupCheck("[])"), false);
assert.equal(groupCheck("({})"), true);
