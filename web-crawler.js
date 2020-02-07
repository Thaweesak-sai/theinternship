const axios = require('axios');
const cheerio = require('cheerio');
const siteUrl = "https://theinternship.io/"

const fetchData = async ()=>{
    const result = await axios.get(siteUrl);
    return cheerio.load(result.data)
};

const getCompany = async()=>{
    const array = [];
    const $ = await fetchData();
    $('div.partner').each(function(){
        let companyLogo = $(this).find('a>img').attr('src');
        let description = $(this).find('span').text();
        array.push({companyLogo,description,});
    });
    return array;
};
module.exports = getCompany;

