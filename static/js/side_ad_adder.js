    $(document).ready(function () {

        /* side_ad add */
        var br = "<br><br><br><br>";

        var adside = "<div class=\"bottom_0_absolute\">\n" +
            "<div class=\"center-block ad_side_scrapper_wrapper\">\n" +
            "    <script async src=\"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js\"></script>\n" +
            "    <!-- example_responsive_1 -->\n" +
            "    <ins class=\"adsbygoogle ad_side_scrapper\"\n" +
            "        style=\"background-color: green\"\n" +
            "        data-ad-client=\"ca-pub-1234\"\n" +
            "        data-ad-slot=\"5678\"></ins>\n" +
            "    <script>\n" +
            "        (adsbygoogle = window.adsbygoogle || []).push({});\n" +
            "    </script>\n" +
            "</div>\n" +
            "\n" +
            "</div>";

        var contentdiv_height = $('#div_detail').height();

        if (contentdiv_height > 1600) {
            $('#div_side_scrapper').height(contentdiv_height);
            $('#div_side_scrapper').append(br + adside);
        }
        /* side_ad add */
    });