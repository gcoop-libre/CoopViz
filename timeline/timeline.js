var tl;
$(document).ready(function() {
  var eventSource = new Timeline.DefaultEventSource();
  var bandInfos = [
    Timeline.createBandInfo({
      eventSource: eventSource,
      date: "Jun 28 2006 00:00:00 GMT",
      width: "70%", 
      intervalUnit: Timeline.DateTime.MONTH, 
      intervalPixels: 100
   }),
    Timeline.createBandInfo({
      eventSource: eventSource,
      date: "Jun 28 2006 00:00:00 GMT",
      width: "30%", 
      intervalUnit: Timeline.DateTime.YEAR, 
      intervalPixels: 200
    })
  ];
  bandInfos[1].syncWith = 0; 
  bandInfos[1].highlight = true; 

  tl = Timeline.create(document.getElementById("timeline-coops"), bandInfos);
  Timeline.loadXML("example1.xml", function(xml, url) { eventSource.loadXML(xml, url); });
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
