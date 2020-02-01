// Plot the default route once the page loads
var defaultURL = "/song_count";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { margin: { t: 30, b: 100 } };
  Plotly.plot("Chart1", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("Chart1", "x", [newdata.x]);
  Plotly.restyle("Chart1", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}
