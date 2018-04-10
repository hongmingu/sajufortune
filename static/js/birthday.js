    $(document).ready(function () {
        var select_year, select_month, select_day, i;

        select_year = $('#select_year');
        select_year.append("<option selected disabled>"+"Year"+"</option>");

        for ( i = 1900; i <= 2017; i += 1 ) {
            select_year.append("<option>"+i+"</option>");
        }

        select_month = $('#select_month');
        select_month.append("<option selected disabled>"+"Month"+"</option>");

        for ( i = 1; i <= 12; i += 1 ) {
            select_month.append("<option>"+i+"</option>");
        }

        select_day = $('#select_day');
        select_day.append("<option selected disabled>"+"Day"+"</option>");

        for ( i = 1; i <= 31; i += 1 ) {
            select_day.append("<option>"+i+"</option>");
        }



    });