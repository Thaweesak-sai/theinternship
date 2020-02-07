const company = require("./web-crawler.js");

const main = async () => {
  const companies = await company();
  const sorted = companies.sort((a, b) => -(a.description - b.description));
  const output = sorted.map(e => e.companyLogo);
  const END_POINT = "https://theinternship.io/";
  const parsed = output.map(e => ({
    logo: END_POINT + e
  }));
  console.log({companies: parsed});
};

main();
