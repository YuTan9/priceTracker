function load(){
    Papa.parse("https://raw.githubusercontent.com/YuTan9/priceTracker/master/log.csv",{
        download: true,
        complete: function(results){
            var date = [];
            var disc = [];
            for (let index = 0; index < results.data.length; index++) {
                if (results.data[index][0] != "") {
                    date.push(results.data[index][0]);
                    disc.push(results.data[index][1]);
                }
            }
            var progress = document.getElementById('animationProgress');
            const ctx = document.getElementById('myChart').getContext('2d');
            var myLineChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: date,
                    datasets:[{
                        label: '__ Percent off',
                        data: disc,
                        fill: false,
                        borderColor: '#fed136'
                    }]
                },
                options:{
                    scales: {
                        yAxes: [{
                            ticks:{
                                min: 0,
                                max: 100
                            }
                        }]
                    },
                    title: {
                        display: true,
                        fontSize: 24,
                        fontFamily: "sans-serif",
                        text: 'Discount rate for MYPROTEIN Taiwan'
                    },
                    legend: {
                        display: false
                    },
                    animation:{
                        onProgress: function(animation) {
                            progress.value = animation.animationObject.currentStep / animation.animationObject.numSteps;
                        },
                        onComplete: function(animation){
                            document.getElementById('myChart').style.display = "block";
                            progress.style.display = "none";
                            document.getElementById('pd').innerText = "Project description";
                            document.getElementById('p1').innerHTML = "<a href=\"https://www.myprotein.tw/\" target=\"_blank\">MYPROTEIN</a>  promotes on different holidays and seasons. And I found out that there were no data showing previous discounts for me to see if it is a good time to make a purchase. So I developed this application to present a general trend of discounts from MYPROTEIN over time.";
                            document.getElementById('dd').innerText = "Development details";
                            document.getElementById('p2').innerText = "This project is developed with Python using Beautiful Soup library and Matplotlib crawl, log, and render the data. To make it run automatically, I further programmed a shell script that will run the python code, push new log data to my Gihub, send me email if anything went wrong (e.g. the platform changed their discount page layout), and I also use the crontab command to execute the shell script everyday on a Raspberry Pi Zero chip.";
                            document.getElementById('p3').innerText = "But the chart you are looking at is not rendered by Matplotlib, instead I used Chart.js and Papa Parse to read from the log file and further render this line chart.";
                            document.getElementById('dc').innerText = "Disclaimer";
                            document.getElementById('p4').innerHTML = "All the information was retrieved from <a href=\"https://www.myprotein.tw/voucher-codes.list\" target=\"_blank\">this voucher list</a> and is probably valid only in Taiwan. And the actual discount should be based on the official site.";
                        }
                    }        
                }
            });
        }
    });
/*     document.getElementById('pd').value = "";
    document.getElementById('pd').value = "";
    document.getElementById('pd').value = "";
    document.getElementById('pd').value = "";
    document.getElementById('pd').value = ""; */
}