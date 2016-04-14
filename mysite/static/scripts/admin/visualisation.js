var VisualisationModule = (function () {

    var count = 0;
    var last_topic = null;
    var labels = [];
    var data = [];

    // called when the client connects
    function onConnect() {
        // Once a connection has been made, make a subscription and send a message.
        console.log("onConnect");
        $('#subscribe').attr('disabled',false);
    }

    // called when the client loses its connection
    function onConnectionLost(responseObject) {
      if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:"+responseObject.errorMessage);
      }

    }

    // called when a message arrives
    function onMessageArrived(message) {

        if (Math.floor(count) > 30){
            window.LineChart.removeData();
        }

        date = new Date();
        date_string = date.getHours()+":"+date.getMinutes()+":"+date.getSeconds();

        window.LineChart.addData([Number(message.payloadString)],date_string);
        count++;
    }
	var lineChartData = {
		labels : labels,
		datasets : [
			{
				label: "Temperature",
				fillColor : "rgba(220,220,220,0.2)",
				strokeColor : "rgba(220,220,220,1)",
				pointColor : "rgba(220,220,220,1)",
				pointStrokeColor : "#fff",
				pointHighlightFill : "#fff",
				pointHighlightStroke : "rgba(220,220,220,1)",
				data : data
			}
		]
	}

	var btnSubscribeClick = function(){
	    var topic = $('#topic').val();
	    if (topic != ""){
	        if (last_topic == null){
	            last_topic = topic
	        }

	        if (last_topic != topic) {
	            window.LineChart.clear();
	            last_topic = topic;
	        }
	        client.subscribe(topic);
	        $('#unsubscribe').attr('disabled',false);
	        $('#subscribe').attr('disabled',true);
	    } else return false;
	};

	var btnUnsubscribeClick = function(){
	    var topic = $('#topic').val();
        client.unsubscribe(topic)
        $('#unsubscribe').attr('disabled',true);
	    $('#subscribe').attr('disabled',false);
	}

     return {
         initialize: function () {
             // Create a client instance
	        client = new Paho.MQTT.Client("iot.eclipse.org", 80, "wadaw");

        	 // set callback handlers
            client.onConnectionLost = onConnectionLost;
            client.onMessageArrived = onMessageArrived;

            // connect the client
            client.connect({onSuccess:onConnect})

            var ctx = document.getElementById("canvas").getContext("2d");
		    window.LineChart = new Chart(ctx).Line(lineChartData, {
			    responsive: true,
			    showXLabels: 10,
			    animation: true,
			    bezierCurve: true,
			    maintainAspectRatio: false,
			    scaleOverride : true,
                scaleSteps : 8,
                scaleStepWidth : 5,
                scaleStartValue : 0,

		    });

		    $('#unsubscribe').attr('disabled',true);
		    $('#subscribe').attr('disabled',true);

		    $('#subscribe').on('click',btnSubscribeClick);
		    $('#unsubscribe').on('click',btnUnsubscribeClick);

         }
     };

})();

require(['jquery', 'bootstrap', 'mqtt','chart', 'utils'], VisualisationModule.initialize);