// Execute the inject.js in a tab and call a method,
// passing the result to a callback function.
function injectedMethod (tab, method, callback) {
	chrome.tabs.executeScript(tab.id, { file: 'inject.js' }, function(){
		chrome.tabs.sendMessage(tab.id, { method: method }, callback);
	});
}

function getBgColors (tab) {
	injectedMethod(tab, 'getBgColors', function (response) {
		var colors = response.data;
		if (colors && colors.length) {
			var url = 'http://colorpeek.com/#' + colors.join(',');
			chrome.tabs.create({ url: url });
		} else {
			alert('No background colors were found! :(');
		}
		return true;
	})
}
function addLink(tab){
	injectedMethod(tab, 'addLink', function (response) {
		return true;
	});
}
// When the browser action is clicked, call the
// getBgColors function.
chrome.browserAction.onClicked.addListener(addLink);