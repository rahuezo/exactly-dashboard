$(document).ready(function () {
  console.log('Current Sidebar State: ', localStorage.getItem('sidebar_state'))
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
      console.log('Set sidebar state to ', localStorage.getItem('sidebar_state'));
    } else {
      localStorage.setItem('sidebar_state', 0); 
      console.log('Set sidebar state to ', localStorage.getItem('sidebar_state') ); 
    }    
  } 
}
