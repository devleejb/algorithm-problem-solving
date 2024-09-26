function findGoodNumber(input) {
  let previousNumber = input[0];
  let cnt = 1;
  const targetNumbers = [];

  for (let i = 1; i < input.length; i++) {
    const number = input[i];
    if (number === previousNumber) {
      cnt += 1;
      if (cnt === 3) {
        targetNumbers.push(111 * Number(number));
      }
    } else {
      previousNumber = number;
      cnt = 1;
    }
  }

  if (targetNumbers.length) {
    return targetNumbers.sort()[targetNumbers.length - 1];
  } else return -1;
}

console.log(findGoodNumber("12223"));
console.log(findGoodNumber("111999333"));
console.log(findGoodNumber("123"));
