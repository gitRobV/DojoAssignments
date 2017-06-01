function printRange( min = -20, max, skip = 1 ) {

    if (max == undefined && skip == 1 ) {
        if (min < 0 ) {
            max = 0;
        } else {
            max = min;
            min = 0;
        }
    }

    for (var i = min; i < max; i+=skip) {
            console.log(i);
    }
}

printRange(-20);

printRange(2, 10);
