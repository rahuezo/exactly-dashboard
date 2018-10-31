Chart.defaults.global.defaultFontColor = '#FFF';
Chart.defaults.global.defaultFontSize = 16;

let graphsCollapse = $('#graphs-collapse');
let modulesClickMsg = $('.modules-click-msg');
let graphsContainer = $('#graphs-container');

$(document).ready(function(){
  $('.module').on('mouseover', function(){
    $(this).addClass('focus-border');
  });

  $('.module').on('mouseout', function(){
    $(this).removeClass('focus-border');
  });

  $('.module').click(function(event){
    let element = $(event.currentTarget);
    let graphs = element.data('graphs');
    let moduleIndex = element.data('index');
    let sameModule = graphsCollapse.data('module-index') == moduleIndex;

    $('#current-module-name').html(` <i class="fas fa-angle-right"></i> ${$(element.find('.card-title')[0]).text()}`);

    if (!sameModule) $('.module').removeClass("active-border"); 
    if (!element.hasClass("active-border")) element.addClass("active-border"); 
    else element.removeClass("active-border"); 

    graphsCollapse.data('module-index', moduleIndex);
    
    if (graphsCollapse.hasClass('show')) {
      if (sameModule) {
        $('#current-module-name').html("");        
        graphsCollapse.collapse('hide');
      } else {
        showChart(graphs);
      }
    } else {
      $('.graphing-card').css('background', 'red');
      showChart(graphs);
      graphsCollapse.collapse('show');
    }
  });
});


function expandCollapse() {

}

function showChart(graphs) {
  graphsContainer.html('');
  let chartSize = 90 / graphs.length;

  for (let i=0; i < graphs.length; i++) {
    let graph = graphs[i];
    let chartId = 'chart-' + i;
    let html = `<div class="graphing-card"><div class="chart-container py-4 ml-auto mr-auto" style="position: relative; height: 50vh; width: ${chartSize}vw;"><canvas id="${chartId}"></canvas></div></div>`;
    graphsContainer.append(html);
    let ctx = document.getElementById(chartId).getContext('2d');
    let chart = new Chart(ctx, graph);
  }
}
