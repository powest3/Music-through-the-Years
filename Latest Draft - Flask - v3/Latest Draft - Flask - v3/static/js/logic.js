
// Plot the default route once the page loads
var defaultURL = "/the1960s";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { title: "Top 10 Songs and Number of Weeks at #1",margin: { t: 50, b: 200 } };
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


// Plot the default route once the page loads
d3.json('/line').then(function(data2) {
  var layout = {title: "Average Number of Weeks at #1 Over Time", margin: { t: 0 } }
  var LINE = document.getElementById('Chart2');
  Plotly.plot(LINE, data2, layout)
})



// // d3.selectAll("#filter-btn").on("click", Click);
// var testjsonurl = "/testjson";
// // create the function to build the table
// function buildCharts(sample) { 
// (d3.json(testjsonurl).then(function(data) {
//   var data = [data];
//   var layout = { margin: { t: 30, b: 100 } };
//   Plotly.plot("SumnaryChart", data, layout);
// })
// )};


// // // add function to handle click
// // function Click() {
// //   var artist = d3.select("#selYear").property("value");
// //   let dataFilter = testjsonurl;
// //   if (artist) {
// //     dataFilter = dataFilter.filter( element => element.artist === artist);
// //   }

// //   buildCharts(dataFilter);
// // }

// d3.selectAll("#filter-btn").on("click", updatePlotly);;

// function updatePlotly()  {

//   // Select the input element and get the raw HTML node
//   var inputElement = d3.select("#selYear");

//   // Get the value property of the input element
//   var inputValue = inputElement.property("value");

//   console.log(inputValue);
//   console.log(testjsonurl);

//   var filteredData = testjsonurl.filter(testjsonurl => testjsonurl.artist === inputValue);
//   buildCharts(filteredData);
//   console.log(filteredData);

// // call the build table funciton with the non-filtered data

// };

// buildCharts(testjsonurl);