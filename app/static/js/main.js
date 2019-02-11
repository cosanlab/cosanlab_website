jQuery(document).ready(function($) {
    /* clickable rows */
    $(".clickable-row").click(function() {
        window.location = $(this).data("url");
    });

    /* filter divs */
    window.previousTag = null;
    $(".filter-button").on('click', function(){
        var tag = $(this).attr('data-filter');
        if(previousTag == null){
          $(".filter").not('.'+tag).hide('3000');
          $('.filter').filter('.'+tag).show('3000');
          window.previousTag = tag;
        } else if (tag === previousTag) {
          $(".filter").not('.'+tag).show('3000');
          $('.filter').filter('.'+tag).show('3000');
          window.previousTag = null;
          });
        } else {
          $('.filter').filter('.'+tag).show('3000');
          // $('.filter').not('.'+previousTag).show('1');
          $(".filter").not('.'+tag).hide('3000');
          window.previousTag = tag;
        };

    });
});
