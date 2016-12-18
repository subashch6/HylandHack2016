
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

app.get('/index.css', function(req,res)
{
	res.sendFile(__dirname + '/index.css');
	console.log("using external css file");
});


app.get('')

io.on('connect', function(socket)
{
	console.log("IO Connect to Peer Successful");

	socket.on('QuerySent',function(jquery)
	{
		var command = 'python2 TestSendSubash.py '+ ' "' + jquery['query'][0] + '"' + ' "'  +  jquery['query'][1] + '" ';
		console.log(command);
		
	  ///////////////////////////////
      	children.execSync(command);//
	  ///////////////////////////////

		var json = fs.readFileSync("aggregate_data.json");
		var jsonObj = JSON.parse(json);
		var string = JSON.stringify(jsonObj);
		
		
		socket.emit('QueryReceived', jsonObj);
		console.log("Return data  = " + string);
	});


	socket.on('receiveRaw',function()
			{
				console.log("recieved raw ask");
				var raw = fs.readFileSync("raw_all_tweets.json");
				var rawObj = JSON.parse(raw);
				var rawstr = JSON.stringify(rawObj);
				console.log(rawstr);
				
				socket.emit('rawSend', rawObj);
			});
});



