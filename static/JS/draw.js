
var map;

function initMap() {
      console.log('map init.')
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 30.5283, lng: 114.3566},
        zoom: 18,
        mapTypeId:"satellite",
      });
      // used to record path
      PolylineCoordinates = [];
}
  
function draw_marker(map,pos,myicon){

      //var d = new Date();
      //var current_second = d.getSeconds();
      //var value = current_second - init_second;
      var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
      //var myLatLng = { lat: 30.5283+value/10000.0 , lng: 114.3566+value/10000.0 };
      
      // add different marker for RTK--FLOAT/FIX or PPP-RTK--FLOAT/WL/NL 
      // Draw Marker
      var mark = new google.maps.Marker({
            position: pos,
            map,
            icon: myicon,
            title: pos.toString(),
        });
}
  
function append_history(type,str_text) {
    var text = $("<p></p>").text(str_text);
    $("#"+type).prepend(text);
}

function AJAX_request(request_func,complete_func,fail_func,callself=true,pars={})
{
    new Ajax.Request(request_func,{
            method:"POST",
            asynchronous: true,
            parameters:pars,
            onComplete: function(transfer){
                complete_func(transfer);
                if (callself){
                    AJAX_request(request_func,complete_func,fail_func,callself,pars);
                }
            },
            onFailure: fail_func,
        });
}

function error_complete_func(transfer){
    var reply = transfer.responseJSON;
    append_history("error",reply["sow"]+", "+reply["diffE"]+", "+reply["diffN"]+", "+reply["diffU"]+", "+reply["mode"]);
}

function alert_func(transfer){
    alert(request_func+"is Wrong!!!!!!!");
}


function rtppp_complete_func(transfer){
    var reply = transfer.responseJSON;
    var pos =  {lat: reply["lat"], lng: reply["lng"]};
    console.log("rtppp",pos)
    draw_marker(map,pos,'http://maps.google.com/mapfiles/kml/pal2/icon18.png');
    //append_history("rtk",reply["sow"]+", "+reply["satNum"]+", "+reply["pdop"]+", "+reply["mode"]);
    //append_history("rtppp",reply["sow"]+", "+reply["satNumFix"]+", "+reply["satNumAug"]+", "+reply["satNum"]+", "+reply["pdop"]+", "+reply["mode"]);
}

function rtk_complete_func(transfer){
    var reply = transfer.responseJSON;
    var pos =  {lat: reply["lat"], lng: reply["lng"]};
    //append_history("rtk",reply["sow"]+", "+reply["satNum"]+", "+reply["pdop"]+", "+reply["mode"]);
    //if(reply["mode"] == "Fixed")
    //{
    console.log("great",pos)
    draw_marker(map,pos,'http://maps.google.com/mapfiles/kml/pal2/icon19.png');
    //}
}


function rtkins_complete_func(transfer){
    var reply = transfer.responseJSON;
    pos =  {lat: reply["lat"], lng: reply["lng"]};
    append_history("rtkins",reply["sow"]+", "+reply["vx"]+", "+reply["vy"]+", "+reply["vz"]+", "+reply["r"]+", "+reply["p"]+", "+reply["y"]+", "+reply["satNum"]+", "+reply["pdop"]+", "+reply["mode"]);
    draw_marker(map,pos,'http://maps.google.com/mapfiles/kml/pal2/icon18.png');
}

    