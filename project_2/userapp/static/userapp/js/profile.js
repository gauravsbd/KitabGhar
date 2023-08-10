const edit=document.querySelector(".edit-profile");
const formContainer=document.querySelector("#edit-form-container");
const activeBook=document.querySelector("#active-books");
const activebookContainer=document.querySelector("#active-books-container");
const bookformcontainer= document.querySelector("#book-form-container")
formContainer.style.display='none';
activebookContainer.style.display="none";
bookformcontainer.style.display="none";
let restoreButton;
let soldButton;
let editButton;
edit.addEventListener("click",()=>{
    activebookContainer.style.display="none";
    formContainer.style.display='block';
    const element = document.getElementById('edit-form-container');
    element.scrollIntoView();
});
activeBook.addEventListener("click",()=>{
     $.ajax({
        type:"GET",
        url:"/activebooks",
        data:{}
        ,success:function(data){
           
          
            
            data.forEach(activebook => {
                const cardrow =document.createElement('div');
                cardrow.className="row"
                const cardCol = document.createElement('div');
                cardCol.className = 'col-lg-3 col-md-4 col-sm-6 col-12 py-5 card-col';
                
                const card = document.createElement('div');
                card.className = 'card shadow-lg book-item h-100';
                
                

                const img = document.createElement('img');
                const url= activebook.image;
                img.src = url
                img.className = 'card-img-top fixed-image';
                img.alt = 'Book image';
                
                const cardBody = document.createElement('div');
                cardBody.className = 'card-body text-center';
                
                // const category = document.createElement('span');
                // category.className = 'category px-4';
                // category.textContent = activebook.fields.category;
                
                const title = document.createElement('p');
                title.className = 'fw-bold my-0 py-1';
                title.textContent = activebook.title;
                
                // cardBody.appendChild(category);
                cardBody.appendChild(title);
                
                editButton = document.createElement('button');
                editButton.className = 'btn edit-books';
                editButton.type = 'button';
                editButton.setAttribute('pid', activebook.id);
                editButton.textContent = 'Edit';
                editButton.addEventListener("click", handleEditButtonClick);

                const pendingButton = document.createElement('button');
                pendingButton.className = 'btn pending-book-request';
                pendingButton.type = 'button';
                pendingButton.setAttribute('pid', activebook.id);
                pendingButton.textContent = 'Pending';
                pendingButton.addEventListener("click",handlePendingButtonClick)

                restoreButton = document.createElement('button');
                restoreButton.className = 'btn restore-book-request';
                restoreButton.type = 'button';
                restoreButton.setAttribute('pid', activebook.id);
                restoreButton.textContent = 'Restore';
                restoreButton.addEventListener("click",handleRestoreButtonClick)

                soldButton = document.createElement('button');
                soldButton.className = 'btn sold-book-request';
                soldButton.type = 'button';
                soldButton.setAttribute('pid', activebook.id);
                soldButton.textContent = 'Sold';

                
                
                card.appendChild(img);
                card.appendChild(cardBody);
                card.appendChild(editButton);
                if (activebook.status==false)
                {
                card.appendChild(pendingButton)
                card.removeChild(editButton)
                }
                if(activebook.status==true)
                {
                    card.appendChild(restoreButton)
                    card.appendChild(soldButton)
                    card.removeChild(editButton)
                }
                
                cardrow.appendChild(cardCol);
                cardCol.appendChild(card);
                
                activebookContainer.appendChild(cardCol);
            });
            formContainer.style.display='none';
            activebookContainer.style.display="block";
            activebookContainer.scrollIntoView();
                        

        }
     })

    
});
// Code for ajax to send the data to the views for edit profile

$('.submitbutton').click(function(){
    
    var Name=document.getElementById("id_Name").value
    var Phone_Number=document.getElementById("id_Phone_Number").value
    var latitude=document.getElementById("id_latitude").value
    var address=document.getElementById("id_Address").value
    var longitude=document.getElementById("id_longitude").value
       
     
    $.ajax({
        type:"GET",
        url:"/editprofile",
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


//code for sending ajax request to the backend for edit books info


const handleEditButtonClick = (event) => {
    const id = event.target.getAttribute("pid");
    $.ajax({
        type:"GET",
        url:"/editbook/",
        data:{
            book_id:id, 
        },
        success:function(data){
          
            formContainer.style.display='none';
            activebookContainer.style.display="none";
            bookformcontainer.style.display="block";
            document.getElementById("id_bookform-title").value = data.title
            document.getElementById("id_bookform-description").value = data.description
            document.getElementById("id_bookform-original_price").value = data.original_price
            document.getElementById("id_bookform-selling_price").value = data.selling_price
            document.getElementById("id_bookform-condition").value = data.condition
            document.getElementById("id_bookform-latitude").value = data.latitude
            document.getElementById("id_bookform-longitude").value = data.longitude
            document.getElementById("image-preview").src=data.image_url
            var map = L.map('bookmap').setView([28.26689, 83.96851], 13);
                           L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                              maxZoom : 19,
                             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                             }).addTo(map);
                             var lat = data.latitude
                             var lng =data.longitude
                             var marker = new L.marker([lat, lng]).addTo(map);
                            
                            map.on('click', function(e) {
                                var marker = new L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
                                var lat=document.getElementById("id_bookform-latitude")
                             lat.value = e.latlng.lat;
                             var lng=document.getElementById("id_bookform-longitude")
                             lng.value = e.latlng.lng;
                            });
        }
})
}

//code for sending ajax request to the backend for handling pending request accept
const handlePendingButtonClick = (event) => {
    const button =event.target;
    const id=button.getAttribute("pid");
   
    $.ajax({
         type:"GET",
         url:"/pending-request/",
         data:{
            book_id:id
         },
         success:function(data)
         {
            const card = button.closest('.card'); // Find the closest parent card
            const pendingButtons = card.getElementsByClassName('pending-book-request');
            
            // Remove all "Pending" buttons within the card
            for (let i = 0; i < pendingButtons.length; i++) {
                card.removeChild(pendingButtons[i]);
                card.appendChild(restoreButton);
                card.appendChild(soldButton);
                
            }
           
        }
            

    })


};
//code for sending the ajax request to the backend for handling the restore request
const handleRestoreButtonClick = (event)=>{
const popupWrapper = document.querySelector(".popup-wrapper");
const close = document.querySelector(".close");
const popup = document.querySelector(".popup");
const checkbox = document.getElementById("checkbox");
const submit = document.querySelector(".submit-btn");

  popupWrapper.style.display = "block";

close.addEventListener("click", () => {
  popupWrapper.style.display = "none";
});

popup.addEventListener("click", (event) => {
  event.stopPropagation();
});

console.log(checkbox);
console.log("Insid checkbox event");
checkbox.addEventListener('change', function() {
submit.disabled = !checkbox.checked;
submit.addEventListener("click",()=>{
popupWrapper.style.display='none'
const button = event.target;
const id=button.getAttribute("pid");
$.ajax({
    type:"GET",
    url:"/restore-request/",
    data:{
        book_id:id
    },
    success:(data)=>{
        const card = button.closest('.card');
        // Find the closest parent card
        const restoreButtons = card.getElementsByClassName('restore-book-request');
        
        // Remove all "restore" buttons within the card
        for (let i = 0; i < restoreButtons.length; i++) {
           
            card.removeChild(restoreButtons[i]);
            card.appendChild(editButton);
            card.removeChild(soldButton);
            
        }
    }
})


});
});
};


//code for the booked book
const bookedBookContainer=document.getElementById("booked-book-container")
bookedBookContainer.style.display="none"

const bookedBookButton=document.getElementById("booked-books")
bookedBookButton.addEventListener("click",()=>{
   
    $.ajax({
      type:"GET",
      url:"/booked-book/",
      data:{},
      success:function(data){
        alert(data.data)
      }

    })

    bookedBookContainer.style.display="block"
})


  //code for the image field in the form

  document.addEventListener('DOMContentLoaded', function() {
    var imageInput = document.getElementById('id_bookform-image');  // Replace with your image field ID
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



// code for leaflet map
var map = L.map('map').setView([28.26689, 83.96851], 13);
 L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	  maxZoom : 19,
	 attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	 }).addTo(map);
map.on('click', function(e) {
	var marker = new L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);;
	var lat=document.getElementById("id_latitude")
 lat.value = e.latlng.lat;
 var lng=document.getElementById("id_longitude")
 lng.value = e.latlng.lng;
});
