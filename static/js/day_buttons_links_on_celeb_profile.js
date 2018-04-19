    $(document).ready(function () {
/*
        $('#btn_today').click(function (e) {

            e.preventDefault();
            var targetDate = new Date(new Date().getTime());

            var target_day = targetDate.getDate();
            var target_month = targetDate.getMonth() + 1;
            var target_year = targetDate.getFullYear();

            var ty, tm, td;
            ty = target_year.toString(16);
            tm = target_month.toString(16);
            td = target_day.toString(16);

            location.href = $('#data_celeb_day_url').attr('data-sj') + "?ty=" + ty + "&tm=" + tm + "&td=" + td;

        });

        $('#btn_tomorrow').click(function (e) {
            e.preventDefault();
            var targetDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);

            var target_day = targetDate.getDate();
            var target_month = targetDate.getMonth() + 1;
            var target_year = targetDate.getFullYear();

            var ty, tm, td;
            ty = target_year.toString(16);
            tm = target_month.toString(16);
            td = target_day.toString(16);

            location.href = $('#data_celeb_day_url').attr('data-sj') + "?ty=" + ty + "&tm=" + tm + "&td=" + td;

        });


        $('#btn_dayaftertomorrow').click(function (e) {
            e.preventDefault();
            var targetDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000 * 2 );

            var target_day = targetDate.getDate();
            var target_month = targetDate.getMonth() + 1;
            var target_year = targetDate.getFullYear();

            var ty, tm, td;
            ty = target_year.toString(16);
            tm = target_month.toString(16);
            td = target_day.toString(16);

            location.href = $('#data_celeb_day_url').attr('data-sj') + "?ty=" + ty + "&tm=" + tm + "&td=" + td;
        });
  */
        var i;

        for (i = 0; i < 3; i++) {
            var date_for_button = new Date(new Date().getTime() + 24 * 60 * 60 * 1000 * i);

            var day_for_day_button = date_for_button.getDate();
            var month_for_day_button = date_for_button.getMonth() + 1;
            var year_for_day_button = date_for_button.getFullYear();
            var btn_id = '#' + 'btn_day_' + i;
            var btn_day= $(btn_id);
            var btn_day_current_text = btn_day.text();
            var btn_day_text_to_add = btn_day_current_text + " (" + year_for_day_button + "-" +
                month_for_day_button + "-" + day_for_day_button + ")";
            btn_day.text(btn_day_text_to_add);
            btn_day.attr({'data-sj-ty': year_for_day_button, 'data-sj-tm': month_for_day_button,
                'data-sj-td': day_for_day_button});
        }

        $('.btn_to_click').click(function (e) {
            e.preventDefault();

            if (selected_year!="non_year" && selected_month!="non_month" && selected_day!="non_day"){

                var target_day = $(this).attr('data-sj-td');
                var target_month = $(this).attr('data-sj-tm');
                var target_year = $(this).attr('data-sj-ty');

                var ty, tm, td;
                ty = parseInt(target_year).toString(16);
                tm = parseInt(target_month).toString(16);
                td = parseInt(target_day).toString(16);

                var link_text = $('#data_celeb_day_url').attr('data-sj') + "?ty=" + ty + "&tm=" + tm + "&td=" + td;
                location.href = link_text;
            }
            else {
                $("#p_birth_warning").html($('#phrase_birthday').attr('data-sj'));
            }
        });

    });