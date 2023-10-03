
const chatRow=document.querySelector(".chat-row")
function chatFunction(event){ 
    const booked_id =event.target.getAttribute("pid")
    const sendButton=document.getElementById("message-send-button")
    sendButton.setAttribute("pid",booked_id)
    const chatContainer=document.getElementById("chat-container")
    chatContainer.style.display='block';

    // const chatSection=document.querySelector(".chat-section")
    // chatSection.style.display="block";
        $.ajax({
           type:"get",
         url:"/chat/",
        data:{
       booked_id:booked_id
        },
        success: (data) => {
         
          const data1 = {
            conversation: [
              {
                message: "hello this is buyer and it's",
                sender_id: 10,
              },
              {
                message: "hello this is buyer",
                sender_id: 10,
              },
              {
                message: "hello this is buyer",
                sender_id: 10,
              },
              {
                message: "hello this is sender",
                sender_id: 2,
              },
              {
                message:
                  "hello this is sender laidflkjdf oiadfkjl sjkdf odlkflsdfj ",
                sender_id: 2,
              },
              {
                message:
                  "hello this is sender jklaeuekrjoij aldfjoier kjadoifuadfn okj",
                sender_id: 2,
              },
              {
                message:
                  "hello this is buyer lkajdfiualkdf ajd lkajdfoija df lsjadfij dfknk k",
                sender_id: 10,
              },
            ],
            user_id: 10,
          };
          while (chatRow.firstChild) {
            chatRow.removeChild(chatRow.firstChild);
          }

          data.conversation.forEach((element) => {
           
            if (element.sender_id == data.user_id) {
              const messageDiv = document.createElement("div");
              messageDiv.innerText = `${element.message}`;
              messageDiv.classList.add("chat", "buyer");
              chatRow.appendChild(messageDiv);
            } else {
              const messageDiv = document.createElement("div");
              messageDiv.innerText = `${element.message}`;
              messageDiv.classList.add("chat", "seller");
              chatRow.appendChild(messageDiv);
            }
          });
        },
    
      })
}

const crossBtn=document.querySelector("#cross-icon")
crossBtn.addEventListener("mouseover", function () {
  crossBtn.className = "fa-solid fa-circle-xmark"; // Add the solid icon class
});
crossBtn.addEventListener("mouseout", function () {
  crossBtn.className = "fa-regular fa-circle-xmark"; // Add the solid icon class
});


crossBtn.addEventListener("click",()=>{
    // const chatSection=document.querySelector(".chat-section")
    // chatSection.style.display="none";
    const chatContainer=document.getElementById("chat-container")
    chatContainer.style.display='none';
    // if(chatSection.classList.contains("my-chat")){
    //   chatSection.classList.remove("my-chat")
    // }else{
    //   chatSection.classList.add("my-chat")
    // }
  })
  
  
  let messageSendButton=document.getElementById("message-send-button")
  messageSendButton.addEventListener("click",(event)=>{

    event.preventDefault();
    const sendButton=document.getElementById("message-send-button")
    const booked_id=sendButton.getAttribute("pid")
    const message=document.getElementById("message").value
    
    $.ajax({
        type:"post",
        url:"/send-chat/",
        data:{
          booked_id:booked_id,
          message:message,
    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
  },
  success:(data)=>{

    const messageDiv = document.createElement("div");
    messageDiv.innerText = `${message}`;
    messageDiv.classList.add("chat", "buyer");
    chatRow.appendChild(messageDiv);
      
       alert(data.data)
         
     }
   })
         
})
  
export{chatFunction}