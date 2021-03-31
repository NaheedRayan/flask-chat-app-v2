


// when a group is clicked we will get the room id and render that room message
function clicked_group(roomid){

    console.log(roomid)

    document.getElementById("chat-area").innerHTML = "";


    // be careful with this link in production server
    link = "http://0.0.0.0:5000/chat/" + roomid ;
    // similar behavior as an HTTP redirect
    window.location.replace(link);
    // document.getElementById("chat-area").innerHTML = "Refreshed";

}