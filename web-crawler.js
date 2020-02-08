/** *
*   web-crawler.js 
*   Created By Thaweesak Saiwongse (Note) 07/02/2020
*/

const axios = require('axios');
const cheerio = require('cheerio');
const siteUrl = "https://theinternship.io/"

const fetchData = async ()=>{
    const result = await axios.get(siteUrl);
    return cheerio.load(result.data)
};

const getCompany = async()=>{
    const array = [];                   //array for keeping data 
    const $ = await fetchData();
    $('div.partner').each(function(){   //iterate through webpage to div.partner
        let companyLogo = $(this).find('a>img').attr('src');        //look for <a><img src="...">
        let description = $(this).find('span').text();              // look for <span>
        array.push({companyLogo,description,});
    });
    return array;
};
module.exports = getCompany;

