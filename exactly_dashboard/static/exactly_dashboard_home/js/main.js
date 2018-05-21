$(document).ready(function () {
  if (localStorage.getItem('sidebar_state') != null) {
    if (localStorage.getItem('sidebar_state') === '0') {
      $('#sidebar').removeClass('active');
    } else {
      $('#sidebar').addClass('active');
    }
  }

  $('#sidebarCollapse').on('click', function (event) {
    $('#sidebar').toggleClass('active');
    setSidebarState();

  });

  $('#dashboards').collapse('show');
})


function setSidebarState() {
  if (localStorage.getItem('sidebar_state') === null) {
    localStorage.setItem('sidebar_state', 0);
  } else {
    if (localStorage.getItem('sidebar_state') === '0') {
      localStorage.setItem('sidebar_state', 1);
    } else {
      localStorage.setItem('sidebar_state', 0);
    }
  }
}
