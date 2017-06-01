$(document).ready(function(){

$('#click').click(function() {
    alert("You Clicked");
})

$('#hide').click(function() {
    $('#hideShow').hide();
})

$('#show').click(function() {
    $('#hideShow').show();
})

$('#toggle').click(function() {
    $('#toggleThis').toggle('slow', function() {
        // $('#toggleThis').show();
    });
})

$('#slideDown').click(function() {
    $('#troll').slideDown();
})

$('#slideUp').click(function() {
    $('#troll').slideUp();
})

$('#slideToggle').click(function() {
    $('#troll').slideToggle();
})

$('#fadeIn').click(function() {
    $('#casper').fadeIn(5000);
})

$('#fadeOut').click(function() {
    $('#casper').fadeOut(3000);
})

$('#addPadding').click(function() {
    $('#addClassToThis').addClass('addPadding')
})

$('#addColor').click(function() {
    $('#addClassToThis').addClass('addBold');
})

$('#removeClass').click(function() {
    $('#addClassToThis').removeClass('addPadding addBold');
})

$('#before').click(function() {
    $('#beforeAfter').before('<h3 class="removeElement">Hello world</h3>');
})

$('#after').click(function() {
    $('#beforeAfter').after('<h3 class="removeElement">Good Bye!</h3>');
})

$('#removeElement').click(function() {
    $('.removeElement').remove();
})

$('#append').click(function() {
    $('#appendHere').append('<blockquote class="removeBlockQuote">This Was Appended!</blockquote>')
})

$('#removeAppend').click(function() {
    $('.removeBlockQuote').remove();
})

$('#html').click(function() {
    var copyHtml = $('#getHtml').html();
    $('#showHtml').text(copyHtml);
})

$('#addList').click(function() {
    var listItem = "<li>this Was added by clicking the button</li>";
    $('.addLists').html(listItem);
})

$('#getAttr').click(function() {
    var title = $('.getAttr').attr('title');
    $('#showAttrs').text(title);
})

$('#setAttr').click(function() {
    $('.getAttr').attr('title','This Title has Changed');
    $('#showAttrs').text('The title for the link above has changed! click "Get Attr" to see what it is.');
})

$('#valUpdate').keyup(function() {
    var value = $( this ).val();
    $('#valChange').text(value);
})

$('#setVal').click(function() {
    var value = $('#valUpdate').val();
    $('.setVal').val(value);
})














})
