<html>
<head>
<title>Panda Brokerage Monitor</title>
<script type='text/javascript' src='http://ajax.googleapis.com/ajax/jquery/1.6.1/jquery.min.js'></script>
<script type='text/javascript' src='js/highcharts.js'></script>
<script type='text/javascript'>
	var p1chart;
	$(document).ready(function() {
		p1chart = new HighCharts.chart({
			chart: {
				renderTo: 'p1container',
				plotBackgroundColor: null,
				plotBorderWidth: null,
				plotShadow: false
			},
			title: {
				text: 'Category A,B,C - {#QUERY_TIME#}'
			},
			tooltip: {
				formatter: function() {
					return '<br>+this.point.name+'<br>: '+this.percentage+' %';
				}
			},
			plotOptions: {
				pie: {
					allowPointSelect: true,
					cursor: 'pointer',
					dataLabels: {
						enabled: true,
						color: HighCharts.theme.textColor || '#000000',
						connectorColor: HighCharts.theme.textColor || '#000000',
						formatter: function() {
							return '<br>+this.point.name+'<br>: '+this.percentage+' %';
						}
					}
				}
			},
			series: [{
				type: 'pie',
				name: 'Panda Brokerage Job',
				data: [
					['A: site by user', 2],
					['B: cloud by user',0],
					['C: choosed by Panda',234]
				]
			}]
		});
	});
