function romans(num) {
    var str = num.toString();
    var ones = "",
        tens = "",
        hundreds = "",
        thousands = "";

    for (var i = str.length - 1; i >= 0; i--) {
        if (str[i] >= 1 && str[i] <= 3 ) {
            counter = str[i];
            while (counter > 0) {
                ones += "I";
                counter--;
            }
        } else {

        }
    }

    console.log(thousands + hundreds + tens + ones);

}

romans(3)
