var tl;
$(document).ready(function() {
  var eventSource = new Timeline.DefaultEventSource();
  var d = Timeline.DateTime.parseIso8601DateTime("1927-09-20");
  var bandInfos = [
    Timeline.createBandInfo({
      eventSource: eventSource,
      date: d,
      width: "90%", 
      intervalUnit: Timeline.DateTime.MONTH, 
      intervalPixels: 100
   }),
    Timeline.createBandInfo({
      overview: true,
      eventSource: eventSource,
      date: d,
      width: "10%", 
      intervalUnit: Timeline.DateTime.YEAR, 
      intervalPixels: 200
    })
  ];
  bandInfos[1].syncWith = 0; 
  bandInfos[1].highlight = true; 

  tl = Timeline.create(document.getElementById("timeline-coops"), bandInfos);
  for (var i = 1; i <= 20; ++i) {
    var file = 'datos/cooperativas-data-' + i + '.json';
    Timeline.loadJSON(file, function(data, url) { eventSource.loadJSON(data, url); });
  }
});

var resizeTimerID = null;
$(window).resize(function() {
 if (resizeTimerID == null) {
   resizeTimerID = window.setTimeout(function() {
     resizeTimerID = null;
     tl.layout();
   }, 500);
 }
});
