$(document).ready(function() {

    $('#img_block img').click(function() {
            var new_img = $(this).attr('data-alternate-src');
            var current_img = $(this).attr('src');
            $(this).attr('data-alternate-src', current_img);
            $(this).attr('src', new_img);
        })

});
