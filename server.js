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

/*

console.log(Generate());

function Generate() {
	PythonShell.run('generate.py', function (err, results) {
		if (err) throw err;
		// results is an array consisting of messages collected during execution
		console.log(results[0]);
	});
}
*/