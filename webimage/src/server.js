#!/usr/bin/env node

var http   = require("http");
var fs     = require("fs");
var wsServ = require("ws").Server;
var wss    = new wsServ({port: 8090}) 
var exec   = require('child_process').exec;

var args = process.argv

wss.on("connection", function(ws) {
	ws.on('message', function(message) {
		exec("xxd -p "+message, function(err, stdout, stderr) {
			ws.send(stdout || stderr || err);
		})
	})
})


if (args[2] && ( args[2] == "-h" || args[2] == "--help") ) {
	console.log("Usage servjs [index file] [port]")
	return
}

http.createServer(function(req,res) {
	var url = req.url.substr(1) || args[2] || "index.html"
	url = url.split("..")[0]
	if (req.method == "GET") {
		var cT = getMime(url.split(".")[1])
		console.log("Request received for: "+url);
		getFile(url, function(data,err) {
			res.writeHead(err || 200, {'Content-Type': cT});
			res.write(data);
			res.end();
		})
	}
}).listen(args[3] || 1337, '0.0.0.0');
console.log('Server running');

var getFile = function(url,cb) {
	fs.readFile(url, function(err, data) {
		if (err || !data) {
			cb("404",404)
			return
		}
		cb(data);
	})
}

var getMime = function(str) {
	if (!str) {
		return "text/plain";
	}
	str = str.toLowerCase();
	switch (str) {
		case "html":
			return "text/html"
		case "txt":
			return "text/plain"
		case "js":
		case "min":
		case "json":
			return "application/javascript"
		case "gif":
			return "image/gif"
		case "jpeg":
		case "jpg":
			return "image/jpeg"
		case "png":
		case "bmp":
		case "ico":
			return "image/png"
		case "css":
			return "text/css"
		case "xml":
			return "text/xml"
		default:
			return "text/html"

	}
}
