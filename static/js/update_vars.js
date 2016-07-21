function updateVars(){
    $.get('/opcuavar/updatevars/', function(data) {
        // data es un JSON
        if(data[0]=="E"){
            alert(data)
            return 0;
        }
        objs = JSON.parse(data);

        for(var i = 0; i< objs.length; i++){
        	$("#variable"+objs[i].pk+"-value").html(objs[i].fields.value);
        	$("#variable"+objs[i].pk+"-timestamp").html(Date(objs[i].fields.timestamp).toLocaleString());
        }

        setTimeout(updateVars,500);
    });

}

$(function(){
	updateVars();
});
