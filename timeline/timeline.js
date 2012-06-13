var tl;
$(document).ready(function() {
  var eventSource = new Timeline.DefaultEventSource();
  var d = Timeline.DateTime.parseIso8601DateTime("2001-06-10");
  var bandInfos = [
    Timeline.createBandInfo({
      eventSource: eventSource,
      date: d,
      width: "70%", 
      intervalUnit: Timeline.DateTime.MONTH, 
      intervalPixels: 100
   }),
    Timeline.createBandInfo({
      eventSource: eventSource,
      date: d,
      width: "30%", 
      intervalUnit: Timeline.DateTime.YEAR, 
      intervalPixels: 200
    })
  ];
  bandInfos[1].syncWith = 0; 
  bandInfos[1].highlight = true; 

  tl = Timeline.create(document.getElementById("timeline-coops"), bandInfos);
//  Timeline.loadJSON("data.json", function(data, url) { console.log(url);console.log(data); eventSource.loadJSON(data, url); });
  Timeline.loadJSON("cooperativas.json", function(data, url) { console.log(url);console.log(data); eventSource.loadJSON(data, url); });
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
