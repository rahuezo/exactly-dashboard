$(document).ready(function() {
  $('.scroll-btn.left').click(function(event){
    horizontalScroll('.horizontal-scroll', -1);
  });

  $('.scroll-btn.right').click(function(){
    horizontalScroll('.horizontal-scroll', 1);
  });

  $('.module').click(function(){
    console.log("Clicked module");
    horizontalScroll($('.horizontal-scroll'), 1, index=$(this).data('index'))
  });
});


function horizontalScroll(element, direction, index=-1) {
  let padding = 4;
  let moduleSize = 210 + padding;
  let scrollDirection;

  if (index < 0) {
    scrollDirection = (direction > 0) ? `+=${moduleSize}` : `-=${moduleSize}`;
  } else {
    let delta = $(element).find(`[data-index=${index}]`).position().left - $(element).position().left;
    scrollDirection= `${(delta < 0) ? "-" : "+"}=` + (Math.abs(delta - ((delta === 0) ? 0 : 40)));
  }

  $(element).animate({
    scrollLeft: scrollDirection,
  }, 250, 'swing');
}
