<<<<<<< HEAD
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
=======
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

// popupWrapper.addEventListener("click",()=>{
//     popupWrapper.style.display='none';
// });

popup.addEventListener("click", (event) => {
  event.stopPropagation();
});

console.log(checkbox);
console.log("Insid checkbox event");
checkbox.addEventListener('change', function() {
  submit.disabled = !checkbox.checked;
  submit.addEventListener("click",()=>{
    popupWrapper.style.display='none'

      
    $.ajax({
      type:"GET",
      url:"/editprofile/",
      data:{
          user_id:id,
          Name:Name,
          Phone_Number:Phone_Number,
          address:address,
          latitude:latitude,
          longitude:longitude,
            
      },
      success:function(data){
          alert(data.data)
      }

  })



  })
});

>>>>>>> 5acf67f86e45effb12bf1926bb712f29ef6f7653
