    $(document).ready(function () {

        var targetDate = new Date(new Date().getTime());
        var targetTomorrowDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);
        var targetDayAfterTomorrowDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000 * 2);

        var selected_year, selected_month, selected_day;

        var target_day;
        target_day = $("#data_td").attr("data-sj-td");


        var target_today = targetDate.getDate();
        var target_tomorrow = targetTomorrowDate.getDate();
        var target_dayaftertomorrow = targetDayAfterTomorrowDate.getDate();

        if(target_today == target_day){
            $('#btn_today').remove();
        } else if (target_tomorrow == target_day){
            $('#btn_tomorrow').remove();
        } else if (target_dayaftertomorrow == target_day){
            $('#btn_dayaftertomorrow').remove();
        }
        /* remove buttons end */

        /* get page by birth start */
        selected_year = $("#data_by").attr("data-sj-by");
        selected_month = $("#data_bm").attr("data-sj-bm");
        selected_day = $("#data_bd").attr("data-sj-bd");


        $('#btn_today').click(function (e) {
            e.preventDefault();

            if (selected_year!="" && selected_month!="" && selected_day!=""){

                var targetDate = new Date(new Date().getTime());

                var target_day = targetDate.getDate();
                var target_month = targetDate.getMonth() + 1;
                var target_year = targetDate.getFullYear();

                var by, bm, bd, ty, tm, td;
                by = parseInt(selected_year).toString(16);
                bm = parseInt(selected_month).toString(16);
                bd = parseInt(selected_day).toString(16);
                ty = target_year.toString(16);
                tm = target_month.toString(16);
                td = target_day.toString(16);

                location.href = $('#url_today').attr('data-sj') + "?by=" + by + "&bm=" + bm + "&bd=" + bd + "&ty=" + ty + "&tm=" + tm + "&td=" + td;
            }
            else {
                console.log("error")
            }
        });


        $('#btn_tomorrow').click(function (e) {
            e.preventDefault();
            if (selected_year!="" && selected_month!="" && selected_day!=""){

                var targetDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);

                var target_day = targetDate.getDate();
                var target_month = targetDate.getMonth() + 1;
                var target_year = targetDate.getFullYear();

                var by, bm, bd, ty, tm, td;
                by = parseInt(selected_year).toString(16);
                bm = parseInt(selected_month).toString(16);
                bd = parseInt(selected_day).toString(16);
                ty = target_year.toString(16);
                tm = target_month.toString(16);
                td = target_day.toString(16);

                location.href = $('#url_today').attr('data-sj') + "?by=" + by + "&bm=" + bm + "&bd=" + bd + "&ty=" + ty + "&tm=" + tm + "&td=" + td;
            }
            else {
                console.log("error")
            }
        });


        $('#btn_dayaftertomorrow').click(function (e) {
            e.preventDefault();
            if (selected_year!="non_year" && selected_month!="non_month" && selected_day!="non_day"){

                var targetDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000 * 2);

                var target_day = targetDate.getDate();
                var target_month = targetDate.getMonth() + 1;
                var target_year = targetDate.getFullYear();

                var by, bm, bd, ty, tm, td;
                by = parseInt(selected_year).toString(16);
                bm = parseInt(selected_month).toString(16);
                bd = parseInt(selected_day).toString(16);
                ty = target_year.toString(16);
                tm = target_month.toString(16);
                td = target_day.toString(16);

                location.href = $('#url_today').attr('data-sj') + "?by=" + by + "&bm=" + bm + "&bd=" + bd + "&ty=" + ty + "&tm=" + tm + "&td=" + td;
            }
            else {
                console.log("error")
            }
        });
        /* get page by birth end */
    });