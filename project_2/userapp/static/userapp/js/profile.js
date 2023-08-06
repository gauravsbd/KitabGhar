const edit=document.querySelector(".edit-profile");
const formContainer=document.querySelector("#edit-form-container");
const activeBook=document.querySelector("#active-books");
const activebookContainer=document.querySelector("#active-books-container");
formContainer.style.display='none';
activebookContainer.style.display="none";
edit.addEventListener("click",()=>{
    formContainer.style.display='block';
});
activeBook.addEventListener("click",()=>{
    activebookContainer.style.display="block";
});


// Code for ajax to send the data to the views

$('.submitbutton').click(function(){
    var id = $(this).attr("pid").toString();
    var Name=document.getElementById("id_Name").value
     var Phone_Number=document.getElementById("id_Phone_Number").value
     var latitude=document.getElementById("id_latitude").value
     var longitude=document.getElementById("id_longitude").value
     
    $.ajax({
        type:"GET",
        url:"/editprofile",
        data:{
            user_id:id,
            Name:Name,
            Phone_Number:Phone_Number,
            latitude:latitude,
            longitude:longitude,
              
        },
        success:function(data){
            
           
            alert(data.data)
            
        }

    })
})


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
