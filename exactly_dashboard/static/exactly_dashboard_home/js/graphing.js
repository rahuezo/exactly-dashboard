$(document).ready(function(){
  $('.module').on('mouseover', function(){
    $(this).addClass('focus-border');
  });

  $('.module').on('mouseout', function(){
    $(this).removeClass('focus-border');
  });

  $('.module').click(function(event){
    let element = $(event.currentTarget);
    let values = element.data('values');
    let chart_type = element.data('chart-type');
    let colors = eval(element.data('colors'));
    let labels = eval(element.data('labels')) ;
    let graphs = element.data('graphs')

    // showChart(chart_type, values, colors, labels);
    showChart2(graphs);

    $('.module').not($(event.currentTarget)).removeClass('active-border');
    $(event.currentTarget).addClass('active-border');
    $('.graphing-card').addClass('active-border');
  });
});

function showChart2(graphs) {
  $('#graphs-container').html('');
  let chart_size = 90 / graphs.length;


  for (let i=0; i < graphs.length; i++) {
    let graph = graphs[i];
    let chart_id = 'chart-' + i;
    let html = `<div class="card graphing-card"><div class="chart-container py-4 ml-auto mr-auto" style="position: relative; height: 50vh; width: ${chart_size}vw;"><canvas id="${chart_id}"></canvas></div></div>`;
    $('#graphs-container').append(html);
    let ctx = document.getElementById(chart_id).getContext('2d');
    console.log(html);
    let chart = new Chart(ctx, graph);
  }




}


function showChart(chart_type, values, colors, labels) {
    var ctx = document.getElementById('myChart').getContext('2d');
    var ctx2 = document.getElementById('myChart2').getContext('2d');


    // var chart = new Chart(ctx, {
    //     type: chart_type,
    //     data: {
    //         datasets: [{
    //         data: values,
    //         backgroundColor: colors,
    //         }],
    //         labels: labels
    //     },
    // })
    //
    // var myChart = new Chart(ctx2, {
    //   type: 'line',
    //   data: {
    //       labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    //       datasets: [{
    //           label: 'Something',
    //           data: [12, 19, 3, 5, 2, 3],
    //           // backgroundColor: [
    //           //     'rgba(255, 99, 132, 0.2)',
    //           //     'rgba(54, 162, 235, 0.2)',
    //           //     'rgba(255, 206, 86, 0.2)',
    //           //     'rgba(75, 192, 192, 0.2)',
    //           //     'rgba(153, 102, 255, 0.2)',
    //           //     'rgba(255, 159, 64, 0.2)'
    //           // ],
    //           borderColor: [
    //               'rgba(255,99,132,1)',
    //               'rgba(54, 162, 235, 1)',
    //               'rgba(255, 206, 86, 1)',
    //               'rgba(75, 192, 192, 1)',
    //               'rgba(153, 102, 255, 1)',
    //               'rgba(255, 159, 64, 1)'
    //           ],
    //           borderWidth: 1
    //       }, {
    //           label: 'Other',
    //           data: [15, 89, 2, 5, 90, 3],
    //           // backgroundColor: [
    //           //     'rgba(2, 245, 132, 0.2)',
    //           //     'rgba(54, 162, 235, 0.2)',
    //           //     'rgba(50, 206, 86, 0.2)',
    //           //     'rgba(75, 192, 192, 0.2)',
    //           //     'rgba(20, 102, 255, 0.2)',
    //           //     'rgba(255, 20, 64, 0.2)'
    //           // ],
    //           borderColor: [
    //               'rgba(255,99,132,1)',
    //               'rgba(54, 162, 235, 1)',
    //               'rgba(255, 206, 86, 1)',
    //               'rgba(75, 192, 192, 1)',
    //               'rgba(153, 102, 255, 1)',
    //               'rgba(255, 159, 64, 1)'
    //           ],
    //           borderWidth: 1
    //       }]
    //   },
    //   options: {
    //       scales: {
    //           yAxes: [{
    //               ticks: {
    //                   beginAtZero:true
    //               }
    //           }]
    //       }
    //   }
  // });
    // var chart2 = new Chart(ctx2, {
    //     type: chart_type,
    //     data: {
    //         datasets: [{
    //         data: values,
    //         backgroundColor: colors,
    //         }],
    //         labels: labels
    //     },
    // })
}
