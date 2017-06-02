

function resetForm() {
    $('input[text],input[email]').val('');
}

$(document).ready(function() {
    $('#users_form').submit(function() {
        var inputs = $(this).serializeArray();
        console.log(inputs);
        if (inputs.length < 1) {
            console.log("Enter some info plese!");
        }else {
            var users_input = {};

            for ( var i in inputs) {
                var input_name = inputs[i]['name'];
                var input_value = inputs[i]['value'];
                users_input[input_name] = input_value;
            }
            var f_name = "<td>" + users_input.f_name + "</td>",
                l_name = "<td>" + users_input.l_name + "</td>",
                email = "<td>" + users_input.email + "</td>",
                contact = "<td>" + users_input.contact + "</td>";

            var tr = "<tr>" + f_name + l_name + email + contact + "</tr>";
            $('tbody').append(tr);
            resetForm();
        }


        return false
    })






});
