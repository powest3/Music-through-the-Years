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
        x: song,
        y: length,
        type: "bar",
      
      }
    ];
    
    Plotly.newPlot("Chart3", data, layout);

    
    var layout2 = { title: "#1 Songs and Number of Weeks at #1",margin: { t: 50, b: 200 } };
    var desired_maximum_marker_size = 40;
    var size = length;
    var year = resultArray.map(row => row.year);
    var data2 = [
      {
        x: year,
        y: length,
        mode: "markers",
        marker: {
          size: size,
          sizeref: 2.0 * Math.max(...size) / (desired_maximum_marker_size**2),
          sizemode: 'area'
        }
      }];
    
    Plotly.newPlot("Chart4", data2, layout2);

    
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
