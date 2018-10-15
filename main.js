const googlehome = require('google-home-notifier')
const language = 'ja';

googlehome.device('Google-Home-Mini', language);

googlehome.notify("ああ、こんにちは。私はグーグルホームです。", function(res) {
	console.log(res);
});
