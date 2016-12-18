
var app = require('express')();
var http = require('http').Server(app); 
var io = require('socket.io')(http);
var fs = require('fs');
var children = require('child_process');
var port = 8888;

http.listen(port, function()
{
			console.log('listening on *:',port);
})



app.get('/', function(req,res)
{
	res.sendFile(__dirname + '/index.html');
	console.log("peer connected to HTTP server");
});

app.get('/externaljs.js', function(req,res)
{
	res.sendFile(__dirname + '/externaljs.js');
	console.log("using external JS File");
});


io.on('connect', function(socket)
{
	console.log("IO Connect to Peer Successful");

	socket.on('QuerySent',function(jquery)
	{
		var command = 'python2 TestSendSubash.py What_The_Phuoc \"' +  jquery['query'] + '\"';
		console.log(command);
		//children.execSync(command);

		var json = fs.readFileSync("aggregate_data.json");
		var jsonObj = JSON.parse(json);
		var string = JSON.stringify(jsonObj);
		

       	var columnData = {
		   columns:[ ['Data',60,30,20,80] ]
		}

		socket.emit('QueryReceived', jsonObj);
		console.log("Return data  = " + string);
	});
});



