function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    if (i % 15 === 0) {
      result.push("FizzBuzz");
    } else if (i % 3 === 0) {
      result.push("Fizz");
    } else if (i % 5 === 0) {
      result.push("Buzz");
    } else {
      result.push(i.toString());
    }
  }
  return result;
}

function arrayDiff(arr1, arr2) {
  const result = [];
  for (const element of arr1) {
    if (!arr2.includes(element) && !result.includes(element)) {
      result.push(element);
    }
  }
  return result;
}

function maximumAdjacentProduct(array) {
  let maximumProduct = null;
  for (let i = 0; i < array.length; i++) {
    if (typeof array[i] === "number" && typeof array[i + 1] === "number") {
      if (maximumProduct === null || array[i] * array[i + 1] > maximumProduct) {
        maximumProduct = array[i] * array[i + 1];
      }
    }
  }
  return maximumProduct;
}
