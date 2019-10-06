const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);
const express = require('express');
const asyncHandler = require('express-async-handler');
const apicache = require('apicache');
const cors = require('cors');
const app = express();

app.use(cors({
    methods: 'GET,POST,PATCH,DELETE,OPTIONS',
    optionsSuccessStatus: 200,
    origin: '*'
}));

app.options('*', cors());

app.get('/', apicache.middleware('24 hours'), function (request, response) {
    var dateFormat = require('dateformat');

    response.writeHead(200, {
        'Content-Type': 'application/json'
    })

    var home = {
        api: []
    }

    var status = {}
    status.name = "University Course REST API"
    status.api_version = "1.0.0"
    var newDate = new Date();
    var time = dateFormat(newDate.setHours(newDate.getHours() + 24), "yyyy-mm-dd h:MM:ss Z");
    status.expires = time
    home.api.push(status)

    response.end(JSON.stringify(home))
})

app.get('/undergraduate', apicache.middleware('24 hours'), function (request, response) {
    var path = require('path');

    var semester = request.param('semester').toLowerCase();
    var year = request.param('year');
    var course = request.param('course').toUpperCase();
   
    response.sendFile(path.join(__dirname, 'data/Undergraduate/' + semester + year + '/JSON/', course + '.json'));
})

app.get('/graduate', apicache.middleware('24 hours'), function (request, response) {
    var path = require('path');

    var semester = request.param('semester').toLowerCase();
    var year = request.param('year');
    var course = request.param('course').toUpperCase();
   
    response.sendFile(path.join(__dirname, 'data/Graduate/' + semester + year + '/JSON/', course + '.json'));
})

// Package the entire app routes and export it for Firebase Function Support
exports.app = functions.https.onRequest(app)