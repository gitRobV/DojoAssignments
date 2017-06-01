function reverseArr(arr) {
    var temp = arr[arr.length-1];
    var counter = 0;

    for (var i = arr.length-1; i > Math.ceil(arr.length/2); i--) {
        arr[counter] = temp;
        counter++;
        temp = arr[i-1];
    }


}
var arr1 = [1,2,3,4,5]
reverseArr(arr1);

console.log(arr1);
