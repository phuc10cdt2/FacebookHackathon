// This helps avoid conflicts in case we inject 
// this script on the same page multiple times
// without reloading.
var injected = injected || (function(){

	var methods = {};

	methods.addLink = function(){
		$("body").append("<div id=\"dialogDiv\" style=\"display:none\"></div>");

		var nodes = document.getElementsByClassName("_3dp _29k");


		if (window.jQuery) {
			console.log('jQuery loaded');
		}


		else{
			alert('not loaded');
		}
		for (var i = nodes.length - 1; i >= 0; i--) {
			// var postUrl = '';
			var postUrl = nodes[i].getElementsByTagName("a")[1].getAttribute('href');
			(function(postUrl){
				link = document.createElement("a");
				link.id = "bookmark";
				link.onclick = function test(){
					requestList(postUrl);
				}
				link.href = '#';
				link.innerHTML = 'Bookmark';
				var div = document.createElement('div');
				div.appendChild(link);
				nodes[i].childNodes[0].appendChild(div);
			})(postUrl);
		};
		return nodes;
	}

	function requestList(postUrl){
		$.ajax({
			url: 'https://cymn1.pythonanywhere.com/api_list/88/',
			type: 'GET',
			success: function(data) {
				console.log(data);
				var lists = JSON.parse(data);

				var theDialog = $("#dialogDiv").dialog();
				theDialog.empty();
				theDialog.dialog("open");

				for (var i = lists.length - 1; i >= 0; i--) {
					console.log(lists[i].title);
					var radioBtn = $('<input type="radio" name="rbtnCount" value = "' + lists[i].id +  '">' +lists[i].title+ '<br>');
					radioBtn.appendTo('#dialogDiv');
				};

				$("#dialogDiv").append('<button id = "saveButton">Save</button>');
				$('#saveButton').click(function(){
					var list_id = $('input[name=rbtnCount]:checked').val();
					savePost(postUrl, list_id);
				});
			},
			error: function(e) {
				console.log(e);
			}
		}); 
	}

	function closeDialog() {
		var theDialog = $("#dialogDiv").dialog();
		theDialog.empty();
	}
	function savePost(postUrl, list_id){
		closeDialog();
		console.log("saving  " + postUrl + "to list " + list_id);
		var fullUrl = 'wwww.facebook.com' + postUrl + '/';
		var sentObject = {};
		sentObject.list_id = list_id;
		sentObject.postUrl = postUrl;
		$.ajax({
			url: 'https://cymn1.pythonanywhere.com/add/',
			type: 'POST',
			data: sentObject,
			success: function(data) {
				alert('Successfully saved!');
			},
			error: function(e) {
				console.log(e);
			}
		}); 
	}
	chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
		var data = {};
		if (methods.hasOwnProperty(request.method))
			data = methods[request.method]();
		sendResponse({ data: data });
		return true;
	});

	return true;
})();