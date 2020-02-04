d3.json(defaultURL).then(function(data) {
      var artist = data.slice(0, 10).map(datas => datas.artist);
      var length = data.slice(0, 10).map(datas => datas.year);
      var layout = { title: "Top 10 Songs and Number of Weeks at #1",margin: { t: 50, b: 200 } };
      console.log(artist)
      console.log(layout)// Build a Bubble Chart
      var data = [
        {
          x: artist,
          y: length,
          type: "bar"
        }
      ];
      
      Plotly.plot("Chart3", data, layout);
})