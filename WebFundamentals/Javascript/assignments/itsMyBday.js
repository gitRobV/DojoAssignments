var daysUntilMyBirthday = 60;

function itsMyBday(daysUntilMyBirthday) {
    for (var i = daysUntilMyBirthday; i >=0; i--) {
        console.log("Days until my Birthday: " + i);
        if ( i > 30 ) {
            console.log(i + " days until my Birthday. It's so far away!!! :(");
        } else if ( i <= 30 && i > 5 ) {
            console.log(i + " days until my Birthday. It's getting closer! OMG!")
        } else if ( i <= 5 && i > 0 ) {
            console.log("OMG MY BIRTHDAY IS ALMOST HERE!!!");
        } else if ( i === 0 ) {
            console.log("It's my Birthday! Woot. Woot.");
        }
    }
}

itsMyBday(daysUntilMyBirthday);
