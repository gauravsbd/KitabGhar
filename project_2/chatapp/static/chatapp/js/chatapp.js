
function chatFunction(event){
    const booked_id =event.target.getAttribute("pid")
    const sendButton=document.getElementById("message-send-button")
    sendButton.setAttribute("pid",booked_id)
    
    const chatContainer=document.getElementById("chat-container")
    chatContainer.style.display='block';
        $.ajax({
           type:"get",
         url:"/chat/",
        data:{
       booked_id:booked_id
        },
        success:(data)=>{
            
          console.log(data)
            
        }
      })
}

let messageSendButton=document.getElementById("message-send-button")
messageSendButton.addEventListener("click",(event)=>{

    event.preventDefault();
    const sendButton=document.getElementById("message-send-button")
    const booked_id=sendButton.getAttribute("pid")
    alert(booked_id)
    alert("message sent")
    $.ajax({
        type:"post",
      url:"/send-chat/",
     data:{
    booked_id:booked_id,
    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
     },
     success:(data)=>{
         
       console.log(data)
         
     }
   })
         


})



export{chatFunction}