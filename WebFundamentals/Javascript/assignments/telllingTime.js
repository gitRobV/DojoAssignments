var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

var str1;
var str2;



if (MINUTE < 30 ) {
    str1 = "just after ";
} else {
    str1 = "almost ";
    HOUR += 1;
}

if (PERIOD === "AM") {
    str2 = " in the morning.";
} else {
    str2 = " in the evening";
}

console.log("it's " + str1 + HOUR + str2);
