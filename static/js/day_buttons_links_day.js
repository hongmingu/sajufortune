    $(document).ready(function () {

        var selected_year, selected_month, selected_day;
        /* get page by birth start */
        selected_year = $("#data_by").attr("data-sj-by");
        selected_month = $("#data_bm").attr("data-sj-bm");
        selected_day = $("#data_bd").attr("data-sj-bd");

        $('.btn_to_click').click(function (e) {
            e.preventDefault();

            if (selected_year!="non_year" && selected_month!="non_month" && selected_day!="non_day"){

                var target_day = $(this).attr('data-sj-td');
                var target_month = $(this).attr('data-sj-tm');
                var target_year = $(this).attr('data-sj-ty');

                var by, bm, bd, ty, tm, td;
                by = parseInt(selected_year).toString(16);
                bm = parseInt(selected_month).toString(16);
                bd = parseInt(selected_day).toString(16);
                ty = parseInt(target_year).toString(16);
                tm = parseInt(target_month).toString(16);
                td = parseInt(target_day).toString(16);
                var link_text = $('#url_day').attr('data-sj') + "?by=" + by + "&bm=" + bm + "&bd=" + bd + "&ty=" + ty + "&tm=" + tm + "&td=" + td;
                location.href = link_text;
            }
            else {
                $("#p_birth_warning").html($('#phrase_birthday').attr('data-sj'));
            }
        });
    });