// https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot/train/javascript

function isBalanced(s, caps) {
    const splited_caps = caps.split('');
    const open_close_map = {};
    // console.log(s, caps);
    for (let i = 0; i < splited_caps.length; i+=2 ) {
        open_close_map[splited_caps[i]] = splited_caps[i+1]
    }

    // console.log(open_close_map);

    let stack = [];
    const splited_s = s.split('');

    for (let i = 0; i < splited_s.length; i++ ) {
        let v = splited_s[i];
        // close 문자인 경우
        if(Object.values(open_close_map).includes(v)) {
            // stack 의 마지막 문자에 해당하는 open 문자의 close 문자와 같은 경우
            if(open_close_map[stack[stack.length-1]] === v ) {
                stack.pop();
            }
            // open 문자인 경우
            else if(v in open_close_map) {
                stack.push(splited_s[i]);
            }
            else {
                return false;
            }
        }
        // open 문자인 경우
        else if(v in open_close_map) {
            stack.push(splited_s[i]);
        }
    }

    return stack.length === 0;
}

let res;
res = isBalanced("(Sensei says yes!)", "()")
console.log(res);
res = isBalanced("(Sensei says no!", "()");
console.log(res);
res = isBalanced("Sensei -says no!", "--");
console.log(res);
res = isBalanced("Sensei says -yes-! --", "--");
console.log(res);
res = isBalanced("(Hello Mother can you hear me?))", "()");
console.log(res);
