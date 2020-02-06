var request = require('request');
var cheerio = require('cheerio');
var URL = require('url-parse');

const page = "https://theinternship.io/"
console.log("Visiting page : "+ page);
request(page, function(error, response, body){
    if(error){
        console.log("Error: "+ error);
    }
    console.log("Status Code:" + response.statusCode);
    if(response.statusCode!=200){
        callback();
        return;
    }
    var $ = cheerio.load(body);
    console.log("Page title: "+ $('title').text());

});