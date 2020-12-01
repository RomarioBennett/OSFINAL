function increment(curr, pList) {
  var current = 999;
  if (curr != -1) current = pList[curr];
  var resultPriority = 0;
  var resultIndex = -1;
  var samePriority = false;
  var areWeThereYet = false;

  jQuery.each(pList, function (key, value) {
    var update = false;

    if (key == curr){
      areWeThereYet = true;
      return true;
    }
    if (value <= current && value >= resultPriority){
      if (value == resultPriority) {
        if (current == value && !samePriority) {
          samePriority = true;
          update = true;
          resultPriority = value;
          resultIndex = key;                            
        }                        
      }
      else if (value == current) {
        if (areWeThereYet) {
          samePriority = true;
          areWeThereYet = false;
          update = true;
          resultPriority = value;
          resultIndex = key;
        }
      }
      else {
        resultPriority = value;
        resultIndex = key;
      }

      if (value > resultPriority && !update)
        samePriority = false;
    }
  });
  return resultIndex;
}



function run(){//funtion that runs results
jQuery('runspace').prepend('<div id="curtain" style="position: absolute; right: 0; width:100%; height:32px;"></div>');
  
  jQuery('#curtain').width(jQuery('#resultTable').width());//results to be the length of the table
  jQuery('#curtain').css({left: jQuery('#resultTable').position().left});//start from the left position
  
  var wipe = 0;
  jQuery('.default').each(function() {
      wipe += Number(jQuery(this).val());//iteration execute time 
  });
  
  console.log(jQuery('#resultTable').width());
  var distance = jQuery("#curtain").css("width");
  
  animationStep(wipe, 0);
  jQuery('#curtain').animate({ width: '0', marginLeft: distance}, wipe*1000/2);//jQuery add'linear'
}

function animationStep(steps, cur) {
jQuery('#timer').html(cur);
if(cur < steps) {
setTimeout(function(){ 
        animationStep(steps, cur+1);
  });//remove 500
  }
  
}

function draw() {
  jQuery('runspace').html('');
  var mainTable = jQuery('#mainTable tr');
  var th = '';
  var td = '';

  
    var quantum = jQuery('#quantum').val();
    var executeTimes = [];

    jQuery.each(mainTable, function (key, value) {
      if (key == 0) return true;
      var executeTime = parseInt(jQuery(value.children[2]).children().first().val());
      executeTimes[key - 1] = { "executeTime": executeTime, "P": key - 1 };
    });

    var areWeThereYet = false;
    while (!areWeThereYet) {
      areWeThereYet = true;
      jQuery.each(executeTimes, function (key, value) {
        if (value.executeTime > 0) {
          th += '<th style="height: 20px; width: ' + (value.executeTime > quantum ? quantum : value.executeTime) * 20 + 'px;">P' + value.P + '</th>';
          td += '<td>' + (value.executeTime > quantum ? quantum : value.executeTime) + '</td>';
          value.executeTime -= quantum;
          areWeThereYet = false;
        }
      });
    }
    jQuery('runspace').html('<table id="resultTable" style="width: 70%"><tr>'
                    + th
                    + '</tr><tr>'
                    + td
                    + '</tr></table>'
                   );
  
  run();
}

