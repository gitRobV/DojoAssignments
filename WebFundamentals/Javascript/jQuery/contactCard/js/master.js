

function resetForm() {
    $('input, textarea').val('');
    $('.card').removeClass('new');
}



$(document).ready(function() {

    $('#contact_form').submit(function() {
        var f_name = $('input[name=f_name]').val();
        var l_name = $('input[name=l_name]').val();
        var desc = $('textarea[name=desc]').val();
        // Create card
        $('#card_box').append('<div class="card new"></div>');
        $('.new').append('<h2><a href="#">' + f_name + ' ' + l_name + '</a></h2>');
        $('.new').append('<p class="hidden">' + desc + '</p>');
        resetForm();
        return false
    })

    $(document).on('click', '.card h2', function() {
        $(this).siblings('p').toggle('slow');
    })

});
