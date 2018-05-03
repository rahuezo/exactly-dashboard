$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    $('#dashboards').collapse('show');

    $('.module').on('mouseover', function(){
      $(this).addClass('focus-border');
    });

    $('.module').on('mouseout', function(){
      $(this).removeClass('focus-border');
    })

})
