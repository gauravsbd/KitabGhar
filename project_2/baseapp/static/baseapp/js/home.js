const button =document.getElementById("profile-ajax")
button.addEventListener("click",()=>{
    $.ajax({
      type:"GET",
      url:"/profile-data/",//url is in userapp urls
      data:{},
      success:function(data){
        // window.location.href="/profile/"
        // const activeBooksElement=document.getElementById("active_books")
        // activeBooksElement.textContent=data.activebooks
        // Redirect first
    window.location.href = "/profile/";
    // Update content after a brief delay
    setTimeout(function() {
        alert("done")
        const activeBooksElement = document.getElementById("active_books");
        activeBooksElement.textContent = data.activebooks;
    }, 100); // Adjust the delay time as needed (in milliseconds)
      }
    })

    
}
)
