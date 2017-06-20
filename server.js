var fs = require('fs'),
    path = require('path'),
    Twit = require('twit'),
    PythonShell = require('python-shell'),
    config = require(path.join(__dirname, 'config.js'));

var pyshell = new PythonShell('generate.py');
var T = new Twit(config);

pyshell.on('message', function(message) {
	T.post('statuses/update', { status : message }, function(err, data, response) {
		console.log(data)
	});
});