"""
https://www.codewars.com/kata/iq-test/train/python
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given
numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness,
and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""

def iq_test(numbers):
    result = ''
    number_list = numbers.split()
    odd_list = list(filter(lambda str: int(str) % 2 == 1, number_list))
    even_list = list(filter(lambda str: int(str) % 2 == 0, number_list))

    if len(odd_list) == 1:
        result = odd_list[0]
    else:
        result = even_list[0]

    return number_list.index(result) + 1

def test_iq_test():
    assert iq_test("2 2 2 2 5")
    assert iq_test("1 3 5 6 7")
    assert iq_test("1 3 5 7 9 5 1 3 7 8 1 9 3 7")
    assert iq_test("2 5 4 8 10 12 6 100")

"""
 - javascript 


function iqTest(numbers){
  const arr = numbers.split(' ');
  
  const oddList = arr.filter(str => parseInt(str, 10) % 2 === 1);
  const evenList = arr.filter(str => parseInt(str, 10) % 2 === 0);
  
  const value = oddList.length === 1 ? oddList[0] : evenList[0];
  
  return arr.findIndex(str => str === value) + 1;
}
"""