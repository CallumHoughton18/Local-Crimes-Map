$(document).ready(function(){
    $("#crimetype-select").change(function() {
        var searchterm = $(this).val().toUpperCase();
        // $("#crimesList li").filter(function() {
        //     $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        // });
        $("#crimesList div").each(function() {
            var currentText = $(this).text().toUpperCase();
            if (currentText.indexOf(searchterm) > -1) {
                $(this).show();
            }
            else{
                $(this).hide();
            }
          });
    });
});