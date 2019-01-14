// https://www.codewars.com/kata/moving-zeros-to-the-end/train/javascript

const moveZeros = function (arr) {
    let res = arr.filter((x) => (x !== 0));
    const zero_count = arr.length - res.length;
    for(let i =0; i < zero_count; i++){
        res.push(0);
    }
    return res;
}

test('moveZeros', () => {
    expect(
        JSON.stringify(moveZeros([1,2,0,1,0,1,0,3,0,1]))
    ).toBe(
        JSON.stringify([ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
        )
    );
});
