// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
	var nodes = $(".relay-toggle");
	var csrftoken = getCookie('csrftoken');
	nodes.on("click", function(){
		var data = {
			id:  $(this).data("id"),
			csrfmiddlewaretoken : csrftoken,
		}
		_this = $(this)
		$.ajax({
			url: "/opcuavar/relay/toggle/",
			method: "POST",
			data: data,
			success: function(data){
				_this.find("img").attr("src", "/static/admin/img/icon-"+data+".svg");
			},
			error: function(){
				alert("ha ocurrido un error. Asegurese de que los dispositivos están disponibles en la red.");
			},
		});
	});

});