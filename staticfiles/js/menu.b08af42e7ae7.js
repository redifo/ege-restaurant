//https://github.com/themewagon/feane
$(window).on('load', function () {
    var $grid = $('.grid').isotope({
        itemSelector: '.all',
    });

    $('.filters-menu li').click(function () {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });

        $('.filters-menu li').removeClass('active');
        $(this).addClass('active');
    });
});
