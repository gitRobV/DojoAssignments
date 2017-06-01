/*
Make a function that copies an array, ONLY accepting the items that are numbers.

IT SHOULD RETURN A NEW ARRAY

ex:

var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// newArray is [1, -3, 0.5]
Copy
HINT

Use typeof to determine type (ex: typeof 24 === "number" would be true)

Bonus (Only If You Have Time):

Make a second function that removes them from the given array. (instead of copying to a new array)
Do you need to return the array?
*/


function removeNums(array) {
    var newArr = [];
    for (var i = 0; i < array.length; i++) {
        if (typeof array[i] === "number") {
            newArr.push(array[i]);
        }
    }
    return newArr;

}

var newArray = removeNums([1, "apple", -3, "orange", 0.5]);

console.log(newArray);
