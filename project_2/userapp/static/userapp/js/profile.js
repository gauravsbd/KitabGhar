const edit=document.querySelector(".edit-profile");
const formContainer=document.querySelector("#edit-form-container");
const activeBook=document.querySelector("#active-books");
const activebookContainer=document.querySelector("#active-books-container");
const bookformcontainer= document.querySelector("#book-form-container")
formContainer.style.display='none';
activebookContainer.style.display="none";
bookformcontainer.style.display="none";
edit.addEventListener("click",()=>{
    activebookContainer.style.display="none";
    formContainer.style.display='block';
    const element = document.getElementById('edit-form-container');
    element.scrollIntoView();
});
activeBook.addEventListener("click",()=>{
    formContainer.style.display='none';
    activebookContainer.style.display="block";
    const element = document.getElementById('active-books-container');
    element.scrollIntoView();
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


//code for sending ajax requesr to the backend for edit books info
const edit_books=document.querySelectorAll(".edit-books");

const handleElementClick = (event) => {
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
           

            var map = L.map('bookmap').setView([28.26689, 83.96851], 13);
                           L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                              maxZoom : 19,
                             attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
                             }).addTo(map);
                             var lat = data.latitude
                             var lng =data.longitude
                             var marker = new L.marker([lat, lng]).addTo(map);
                            
                            map.on('click', function(e) {
                                var marker = new L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);;
                                var lat=document.getElementById("id_bookform-latitude")
                             lat.value = e.latlng.lat;
                             var lng=document.getElementById("id_bookform-longitude")
                             lng.value = e.latlng.lng;
                            });
        }
})
}
  edit_books.forEach(element => {
    element.addEventListener("click", handleElementClick);
    
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
