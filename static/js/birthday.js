    $(document).ready(function () {
        /* select birthday */
        var select_year, select_month, select_day, i_birth;

        var currentDate = new Date(new Date().getTime());
        var current_year = currentDate.getFullYear();

        select_year = $('#select_year');

        for ( i_birth = current_year; i_birth >= 1900; i_birth -= 1 ) {
            select_year.append("<option value=\""+i_birth+"\">"+i_birth+"</option>");
        }

        select_month = $('#select_month');

        for ( i_birth = 1; i_birth <= 12; i_birth += 1 ) {
            select_month.append("<option value=\""+i_birth+"\">"+i_birth+"</option>");
        }

        select_day = $('#select_day');

        for ( i_birth = 1; i_birth <= 31; i_birth += 1 ) {
            select_day.append("<option value=\""+i_birth+"\">"+i_birth+"</option>");
        }
        /*select birth end */

    });