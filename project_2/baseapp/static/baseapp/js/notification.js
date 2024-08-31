const notificationButton = document.getElementById("notification-button");
const notificationDropdown=document.querySelector( "#notification-dropdown")
const menu=document.querySelector(".notification-menu ")



notificationButton.addEventListener("click", () => {
  // responsive notification

  if(window.innerWidth>=992){
    if(menu.classList.contains("dropdown-menu-start")){
      menu.classList.remove("dropdown-menu-start")
    }
    menu.classList.add("dropdown-menu-end")
  }
  else if(window.innerWidth<992){
    if(menu.classList.contains("dropdown-menu-end"))
    {
      menu.classList.remove("dropdown-menu-end")
    }
    menu.classList.add("dropdown-menu-start")
  }
  
  
  // Clear the existing notifications
  
  while (notificationDropdown.firstChild) {
    notificationDropdown.removeChild(notificationDropdown.firstChild);
  }

  $.ajax({
    type: "GET",
    url: "/notification/",
    data: {},
    success: function (notification_data) {
      notification_data.search_notification.forEach((element) => {
        const notificationDropdownList = document.createElement("li");
        notificationDropdownList.setAttribute("book_id", element.book_id);
        notificationDropdownList.setAttribute("search_id", element.search_id);
        notificationDropdownList.className = "border-r border notification-list";
        notificationDropdownList.addEventListener(
          "click",
          handleSearchNotificationClick
        );

        const notificationContent = document.createElement("p");
        notificationContent.className="dropdown-item"
        notificationContent.textContent = `${element.title} book is now available you may like this.`;

        

        notificationDropdownList.appendChild(notificationContent);
        notificationDropdown.appendChild(notificationDropdownList);
      });

      notification_data.pending_notification.forEach((element) => {
        const notificationDropdownList = document.createElement("li");
        notificationDropdownList.setAttribute("pending_id", element.pending_id);
        notificationDropdownList.className = "border-r border notification-list dropdown-item";
        notificationDropdownList.addEventListener(
          "click",
          handlePendingNotificationClick
        );

        const notificationContent = document.createElement("p");
        notificationContent.textContent = ` ${element.buyer_name} wants to buy the ${element.book_name} posted by you.`;

      
        notificationDropdownList.appendChild(notificationContent);
        notificationDropdown.appendChild(notificationDropdownList);
      });
    },
  });
});



function handleSearchNotificationClick(event)
{
  listElement=event.target;
  listElement=listElement.closest("li")
  const searchId=listElement.getAttribute("search_id")
  
  listElement=listElement.closest("li");
  book_id=listElement.getAttribute("book_id");
  window.location.href = `/book-detail/${book_id}`;
  
}

 async function handlePendingNotificationClick(event){
 listElement=event.target;
 listElement=listElement.closest("li")
 const pending_id=listElement.getAttribute("pending_id")
 
 window.location.href="/profile/";
}


// code for the message displaying the 
function getMessages(){
   
  $.ajax({
    method:"get",
    url:"/get-messages/",
    data:{},
    success:function(data){
      data.messages.forEach((data)=>{
        let messageContainer=document.getElementById('message-container')
        messageContainer.innerHTML = `
        <div class="alert alert-info hide mt-3 pt-1" id="alert-message-container">
          <span class="fas fa-exclamation-circle"></span>
          <span class="msg fw-light">
            <div class="messages">
              <div class="message" id="alert-message"></div>
            </div>
          </span>
          <div class="close-btn">
            <span class="fas fa-times"></span>
          </div>
        </div>
      `;
      const messageSpan=document.querySelector('.alert span')
      $('.alert').addClass("show");
      $('.alert').removeClass("hide");
      let alertContainer=document.getElementById('alert-message-container')
      $('#alert-message').text(data.message);
      if(data.header=="success"){
        alertContainer.style.backgroundColor = "lightgreen";
      }
      if(data.header=="info"){
        alertContainer.style.backgroundColor = "rgb(173, 216, 230)";
      }
      if(data.header=="warning"){
        alertContainer.style.backgroundColor = "rgb(255, 192, 203)";
      }

        setTimeout(function(){
          $('.alert').removeClass("show");
          $('.alert').addClass("hide");
          messageContainer.innerHTML=``;
        },3000);
      
      $('.close-btn').click(function(){
        $('.alert').removeClass("show");
        $('.alert').addClass("hide");
        messageContainer.innerHTML=``;
      });
    })
    }
  })
}

// setInterval(()=>{
  //   getMessages();
  // },100)
  getMessages();