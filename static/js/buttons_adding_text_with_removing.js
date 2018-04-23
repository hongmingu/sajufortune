        $(document).ready(function () {
            var i, target_day;

            target_day = $("#data_td").attr("data-sj");

            for (i = 0; i < 3; i++) {
                var date_for_button = new Date(new Date().getTime() + 24 * 60 * 60 * 1000 * i);

                var day_for_day_button = date_for_button.getDate();
                var month_for_day_button = date_for_button.getMonth() + 1;
                var year_for_day_button = date_for_button.getFullYear();
                var btn_id = '#' + 'btn_day_' + i;
                var btn_day = $(btn_id);
                var btn_day_current_text = btn_day.text();
                var btn_day_text_to_add = btn_day_current_text + " " + year_for_day_button + "-" +
                    month_for_day_button + "-" + day_for_day_button;
                btn_day.text(btn_day_text_to_add);
                btn_day.attr({
                    'data-sj-ty': year_for_day_button, 'data-sj-tm': month_for_day_button,
                    'data-sj-td': day_for_day_button
                });

                if (day_for_day_button == target_day) {
                    btn_day.remove()
                }
            }
        });