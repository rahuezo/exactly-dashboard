$(document).ready(function(){
  $('.module').on('mouseover', function(){
    $(this).addClass('focus-border');
  });

  $('.module').on('mouseout', function(){
    $(this).removeClass('focus-border');
  });

  $('.module').click(function(event){
    let element = $(event.currentTarget);
    let graphs = element.data('graphs')

    showChart(graphs);

    $('.module').not(element).removeClass('active-border');
    element.addClass('active-border');
    $('.graphing-card').addClass('active-border');
  });
});

function showChart(graphs) {
  $('#graphs-container').html('');
  let chart_size = 90 / graphs.length;

  for (let i=0; i < graphs.length; i++) {
    let graph = graphs[i];
    let chart_id = 'chart-' + i;
    let html = `<div class="card graphing-card"><div class="chart-container py-4 ml-auto mr-auto" style="position: relative; height: 50vh; width: ${chart_size}vw;"><canvas id="${chart_id}"></canvas></div></div>`;
    $('#graphs-container').append(html);
    let ctx = document.getElementById(chart_id).getContext('2d');
    let chart = new Chart(ctx, graph);
  }
}
