    $(document).ready(function () {

        $('.btn_to_click').click(function (e) {
            e.preventDefault();

            var target_day = $(this).attr('data-sj-td');
            var target_month = $(this).attr('data-sj-tm');
            var target_year = $(this).attr('data-sj-ty');

            var ty, tm, td;
            ty = parseInt(target_year).toString(16);
            tm = parseInt(target_month).toString(16);
            td = parseInt(target_day).toString(16);

            var link_text = $('#data_celeb_day_url').attr('data-sj') + "?ty=" + ty + "&tm=" + tm + "&td=" + td;
            location.href = link_text;

        });
    });