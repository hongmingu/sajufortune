    $(document).ready(function () {

        var selected_lang;

        $('#btn_lang').click(function (e) {
            e.preventDefault();
            selected_lang = $("#select_lang option:selected").val();

            switch (selected_lang){

                case 'non_lang':
                    $("#p_lang_warning").html($('#phrase_language').attr('data-sj'));
                    break;
                case 'ara':
                    location.href = $('#url_ara').attr('data-sj');
                    break;
                case 'chi':
                    location.href = $('#url_chi').attr('data-sj');
                    break;
                case 'eng':
                    location.href = $('#url_eng').attr('data-sj');
                    break;
                case 'por':
                    location.href = $('#url_por').attr('data-sj');
                    break;
                case 'spa':
                    location.href = $('#url_spa').attr('data-sj');
                    break;
                default:
                    break;
                }
            });
    });