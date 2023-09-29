
function chatFunction(event){
    const booked_id =event.target.getAttribute("pid")
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
messageSendButton.addEventListener("click",()=>{
    alert("message sent")
})



export{chatFunction}