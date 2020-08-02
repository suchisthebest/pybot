const {Client,
	Attachment
} = require('discord.js');
const bot = new Client();

const cheerio = require('cheerio');


const request = require('request')

const PREFIX = '$';

var version = '2.0';

bot.on('ready', () =>{
	console.log('asuh dud');
	bot.user.setActivity('');

	bot.on('message', msg=>{

	let args = msg.content.substring(PREFIX.length).split(" ");

	switch(args[0]){
		case 'cursed':
        image(msg);

        break;
        }
});
function image(msg){

    var options = {
        url: "http://results.dogpile.com/serp?qc=images&q=" + "minecraft cursed images",
        method: "GET",
        headers: {
            "Accept": "text/html",
            "User-Agent": "Chrome"
        }
    };





    request(options, function(error, response, responseBody) {
        if (error) {
            return;
        }


        $ = cheerio.load(responseBody);


        var links = $(".image a.link");

        var urls = new Array(links.length).fill(0).map((v, i) => links.eq(i).attr("href"));

        console.log(urls);

        if (!urls.length) {

            return;
        }

        // Send result
        msg.channel.send( urls[Math.floor(Math.random() * urls.length)]);
    });








}

bot.login('*your bot token here*');
