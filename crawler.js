/** *
*   crawler.js 
*   Created By Thaweesak Saiwongse (Note) 07/02/2020
*/

const company = require("./web-crawler.js");

const main = async () => {
  const companies = await company(); //call module web-crawler.js
  const sorted = companies.sort((a, b) => -(a.description - b.description)); //sort by length of text by ascending
  const output = sorted.map(e => e.companyLogo);
  const END_POINT = "https://theinternship.io/";
  const parsed = output.map(e => ({
    logo: END_POINT + e
  }));
  console.log({companies: parsed});
};

main();
