var roomid = window.location.href.replace(`${window.location.origin}/room/`, "")

$('#newentry').scrollTop($('#newentry')[0].scrollHeight)




socket = io()
  
  socket.on('connect', function() {
    socket.emit("room_connect", {
      roomid: roomid
    })
  })


socket.on('add_element', function(msg){
  
  
  
  $('#newentry').append( '<div class = "card mb-2"><b style="color: #000">'+msg.sender+'</b> '+msg.content+'</div>' )
  
  $('#newentry').scrollTop($('#newentry')[0].scrollHeight)
        }
        
 
        
)


button = document.getElementById("Send_Message")
input = document.getElementById("Message")
button.addEventListener("click", function(){
  
  if (input.value != ""){
    socket.emit("send_message",{
      content: input.value, 
      roomid: roomid
    })
    input.value = ""
  }
})

$('#Message').keypress(function (e){

var key = e.which
if(key === 13){
  button.click()
}
  
})