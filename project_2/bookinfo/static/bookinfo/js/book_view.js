
const contact = document.querySelector("#buy");
const popupWrapper = document.querySelector(".popup-wrapper");
const close = document.querySelector(".close");
const popup = document.querySelector(".popup");
const checkbox = document.getElementById("checkbox");
const submit = document.querySelector(".submit-btn")

contact.addEventListener("click", () => {
  popupWrapper.style.display = "block";
});

close.addEventListener("click", () => {
  popupWrapper.style.display = "none";
});

popup.addEventListener("click", (event) => {
  event.stopPropagation();
});


checkbox.addEventListener('change', function() {
submit.disabled = !checkbox.checked;
submit.addEventListener("click",()=>{
popupWrapper.style.display='none'
    const book=document.getElementById("book-id")
    const book_id=book.getAttribute("attr")
   
    
    $.ajax({
      type:"GET",
      url:"/book-book/",
      data:{
          book_id:book_id,
      },
      success:function(data,textStatus,xhr){
        alert("done")
        if (data.error === 'authentication_required') {
          var redirectUrl = data.redirect_url;
          if (redirectUrl) {
              window.location.href = redirectUrl;
          }
      } 
      
      
  },
  error: function(xhr, textStatus, errorThrown) {
    if (xhr.status === 401) {
          window.location.href = "/login/";
        // User is not authenticated, handle this scenario
        // You can redirect to the login page or show an error message
       
    } else {
        // Handle other errors
        console.error('AJAX error:', errorThrown);
    }
}
  
  })
})
});


document.addEventListener('DOMContentLoaded', function() {
  var imageInput = document.getElementById('id_image');  // Replace with your image field ID
  var imagePreview = document.getElementById('image-preview');
  
  imageInput.addEventListener('change', function() {
      
      var file = imageInput.files[0];
      if (file) {
          var reader = new FileReader();
          reader.onload = function(e) {
              imagePreview.src = e.target.result;
          };
          reader.readAsDataURL(file);
      }
  });
});

