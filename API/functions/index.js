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

app.use(express.json());
app.options('*', cors());

app.get('/', apicache.middleware('24 hours'), function (request, response) {
    var dateFormat = require('dateformat');

    response.writeHead(200, {
        'Content-Type': 'application/json'
    })

    asyncHandler(async () => {
        var home = {
            api: []
        }

        var status = {}
        status.name = "University Course Scheduler (REST API)"
        status.api_version = "1.0.0"
        var newDate = new Date();
        var time = dateFormat(newDate.setHours(newDate.getHours() + 24), "yyyy-mm-dd h:MM:ss Z");
        status.expires = time
        home.api.push(status)

        response.end(JSON.stringify(home)) 
    })();   
})

app.get('/undergraduate', apicache.middleware('24 hours'), function (request, response) {
    var path = require('path');

    asyncHandler(async () => {
        var semester = request.param('semester').toLowerCase();
        var year = request.param('year');
        var course = request.param('course').toUpperCase();
        response.sendFile(path.join(__dirname, 'data/undergraduate/' + semester + year + '/JSON/', course + '.json'), {headers: {'Content-Type': 'application/json'}});
    })();  
})

app.get('/graduate', apicache.middleware('24 hours'), function (request, response) {
    var path = require('path');

    asyncHandler(async () => {
        var semester = request.param('semester').toLowerCase();
        var year = request.param('year');
        var course = request.param('course').toUpperCase();
        response.sendFile(path.join(__dirname, 'data/graduate/' + semester + year + '/JSON/', course + '.json'), {headers: {'Content-Type': 'application/json'}});
    })();
})

app.get('/search', apicache.middleware('5 minutes'), function (req, res) {
    var Fuse = require('fuse.js');

    res.writeHead(200, {
        'Content-Type': 'application/json'
    })

    asyncHandler(async () => {
        var level = req.param('level').toLowerCase();
        var searchKeyword = req.param('keyword');
        var semester = req.param('semester').toLowerCase();
        var year = req.param('year');
        var course = req.param('course').toUpperCase();
        var list;

        list = JSON.parse(require('fs').readFileSync('data/' + level + '/' + semester + year + '/JSON/' + course + '.json', 'utf8'));

        var options = {
            shouldSort: true,
            threshold: 0.6,
            location: 0,
            distance: 100,
            maxPatternLength: 32,
            minMatchCharLength: 1,
            keys: [
                "Title",
                "Course Number",
                "Instructor Name",
                "CRN"
            ]
        };

        var fuse = new Fuse(list, options);
        var result = fuse.search(searchKeyword);
        res.end(JSON.stringify(result));
    })();
})

// Package the entire app routes and export it for Firebase Function Support
exports.app = functions.https.onRequest(app)