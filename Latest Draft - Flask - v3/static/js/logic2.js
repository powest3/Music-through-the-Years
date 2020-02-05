///////use this/////
function buildCharts(sample) {
  d3.json("/artists").then((data) => {
    var resultArray = data.filter(sampleObj => sampleObj.artist == sample);
    var song = resultArray.map(row => row.title)
    var length = resultArray.map(row => row.issue_date.length)
    var layout = { title: "#1 Songs and Number of Weeks at #1",margin: { t: 50, b: 200 } };
    console.log(resultArray)
    console.log(length)
    var data = [
      {
        x: length,
        y: song,
        type: "bar",
        orientation: "h",
      }
    ];
    
    Plotly.newPlot("Chart3", data, layout);


    
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selArtist");
  
  // Use the list of sample names to populate the select options
  d3.json("/artists").then((data) => {
    var sampleNames = [...new Set(data.map(row => row.artist))].sort();

    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    var firstSample = sampleNames[0];
    buildCharts(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
}

// Initialize the dashboard
init();
