var colors = ['#2ECC40','#f2f55f','#0074D9','#FF4136','#B10DC9'];

var chartData = {
    labels:["Conventional Medicine", "Lifestlye modification", "Physical Rehabilitation", "Psychotherapy", "Complementary health" ],
    datasets: [{
        backgroundColor: colors.slice(0,5),
        borderWidth: 5,
        data: [100,100,100,100,100]
    }]
};
var donutOptions = {
      cutoutPercentage: 85, 
      legend: {position:'bottom', padding:5, labels: {pointStyle:'circle', usePointStyle:true}}
};

var landingDonut = document.getElementById("landingDonut");
if(landingDonut){
    new Chart(landingDonut, {
        type: 'pie',
        data: chartData,
        options: donutOptions
    });
}
