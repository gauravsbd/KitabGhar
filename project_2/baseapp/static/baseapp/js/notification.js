const notificationButton = document.getElementById("notification-button");
const notificationDropdown=document.querySelector( "#notification-dropdown")
notificationButton.addEventListener("click", (event) => {

  const notificationCount=event.target
  while(notificationCount.firstChild){
    notificationCount.removeChild(notificationCount.firstChild)
  }
  while(notificationDropdown.firstChild){
    notificationDropdown.removeChild(notificationDropdown.firstChild)
  }
  $.ajax({
    type: "GET",
    url: "/notification/",
    data: {},
    success: function (notification_data) {
      notification_data.search_notification.forEach(element => {
        const notificationDropdownList=document.createElement("li");
        notificationDropdownList.setAttribute("book_id",element.book_id)
        notificationDropdownList.setAttribute("search_id",element.search_id)
        notificationDropdownList.className=("border-r border notification-list")
        notificationDropdownList.addEventListener("click",handleSearchNotificationClick)
        const notificationContent=document.createElement("p");
        notificationContent.textContent=` ${element.title} book is now available you may like this.`;
        notificationDropdownList.appendChild(notificationContent)
        notificationDropdown.appendChild(notificationDropdownList)
        
      });
    notification_data.pending_notification.forEach(element=>{
      const notificationDropdownList=document.createElement("li");
      notificationDropdownList.setAttribute("pending_id",element.pending_id)
      notificationDropdownList.className=("border-r border notification-list")
      notificationDropdownList.addEventListener("click",handlePendingNotificationClick)
      const notificationContent=document.createElement("p");
      notificationContent.textContent=` ${element.buyer_name} wants to buy the ${element.book_name} posted by you.`;
      notificationDropdownList.appendChild(notificationContent)
      notificationDropdown.appendChild(notificationDropdownList)
      
    })
    },
  });
});

function handleSearchNotificationClick(event)
{
  listElement=event.target;
  listElement=listElement.closest("li")
  const searchId=listElement.getAttribute("search_id")
  alert(searchId)
  listElement=listElement.closest("li");
  book_id=listElement.getAttribute("book_id");
  window.location.href = `/book-detail/${book_id}`;
  
}

 async function handlePendingNotificationClick(event){
 listElement=event.target;
 listElement=listElement.closest("li")
 const pending_id=listElement.getAttribute("pending_id")
 alert(pending_id)
 window.location.href="/profile/";
}