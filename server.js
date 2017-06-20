var fs = require('fs'),
    path = require('path'),
    Twit = require('twit'),
    PythonShell = require('python-shell'),
    config = require(path.join(__dirname, 'config.js'));

var T = new Twit(config);

setInterval(function(){
	try {
    	Tweet();
	}
	catch (e) {
		console.log(e);
	}
}, 60000 * 1);

function Tweet() {
	PythonShell.run('generate.py', { mode: 'text' }, function (err, results) {
		if (err) throw err;
		// results is an array consisting of messages collected during execution
		T.post('statuses/update', { status : results[0] }, function(err, data, response) {
			console.log(data)
		});
	});
}