$(document).ready(function () {
    document.title = 'Metrics';
    loadGlobalTopTenGraph();
    loadColleaguesEncounteredGraph();
    $(window).trigger('resize');
});

function loadColleaguesEncounteredGraph() {
    $.get("/encountered/", function (data) {
        nv.addGraph({
            generate: function () {
                var chart = nv.models.multiBarHorizontalChart()
                    .x(function (d) {
                        return d.label
                    })
                    .y(function (d) {
                        return d.value
                    })
                    .margin({top: 30, right: 30, bottom: 10, left: 30})
                    .showValues(false)           //Show bar value next to each bar.
                    .tooltips(true)             //Show tooltips on hover.
                    .barColor(d3.scale.category20().range())
                    .showControls(false)        //Allow user to switch between "Grouped" and "Stacked" mode.
                    .stacked(true);

                chart.yAxis
                    .tickFormat(d3.format('d'));

                chart.tooltipContent(function (key, y, e, graph) {
                    return '<h5>' + y + ' : ' + e + '</h5>';
                });

                d3.select('#colleaguesEncountered svg')
                    .datum(data)
                    .transition().duration(500)
                    .call(chart);

                nv.utils.windowResize(chart.update);
                chart.dispatch.on('stateChange', function (e) {
                    nv.log('New State:', JSON.stringify(e));
                });

                return chart;
            }
        });
    });

}


function loadGlobalTopTenGraph() {
    $.get("/globally_known/", function (data) {
        var labels = data.names;
        var times_correct = data.times_correct;

        var barChartData = {
            labels: labels,
            datasets: [
                {
                    fillColor: "rgba(76, 175, 80,1)",
                    strokeColor: "rgba(220,220,220,0.8)",
                    highlightFill: "rgba(220,220,220,0.75)",
                    highlightStroke: "rgba(220,220,220,1)",
                    data: times_correct
                }
            ]

        };

        new Chart(document.getElementById("globalTenGraph").getContext("2d")).Bar(barChartData, {
            responsive: true
        });
    });


}