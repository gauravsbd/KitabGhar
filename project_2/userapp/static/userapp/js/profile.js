let editProfile = document.querySelector(".edit-profile");
let editProfileContainer = document.querySelector("#edit-form-container");
let activeBook = document.querySelector("#active-books");
let activeBookContainer = document.querySelector("#active-books-container");
let editBookContainer = document.querySelector("#book-form-container");
let bookedBookContainer = document.getElementById("booked-book-container");
let restoreButton;
let soldButton;
let editButton;
let pendingButton;
bookedBookContainer.style.display = "none";
editProfileContainer.style.display = "none";
activeBookContainer.style.display = "none";
editBookContainer.style.display = "none";
editProfile.addEventListener("click", () => {
  bookedBookContainer.style.display = "none";
  activeBookContainer.style.display = "none";
  editBookContainer.style.display = "none";
  editProfileContainer.style.display = "block";
  const element = document.getElementById("edit-form-container");
  element.scrollIntoView();
});

//code for the active books
activeBook.addEventListener("click", () => {
  const activeBookrow = document.getElementById("active-books-row");
  while(activeBookrow.firstChild){
    activeBookrow.removeChild(activeBookrow.firstChild)
  }
  $.ajax({
    type: "GET",
    url: "/activebooks",
    data: {},
    success: function (data) {
      data.forEach((activebook) => {
        const cardrow = document.createElement("div");
        cardrow.className = "row";
        const cardCol = document.createElement("div");
        cardCol.className = "col-lg-3 col-md-4 col-sm-6 col-12 py-5 card-col";

        const card = document.createElement("div");
        card.className = "card shadow-lg book-item overflow-hidden h-100";

        const buttonContainer = document.createElement("div");
        buttonContainer.className = "py-2 mx-3 button-container";

        const img = document.createElement("img");

        const url = activebook.image;
        img.src = url;
        img.className = "card-img-top object-fit-cover w-100 h-50 px-1 py-1";
        img.alt = "Book image";

        const title = document.createElement("span");
        title.className = "fw-bold text-center py-1";
        title.textContent = activebook.title;

        editButton = document.createElement("button");
        editButton.className =
          "btn edit-books my-2 w-100 border border-r btn-sm";
        editButton.type = "button";
        editButton.setAttribute("pid", activebook.id);
        editButton.textContent = "Edit";
        editButton.addEventListener("click", handleEditButtonClick);

        pendingButton = document.createElement("button");
        pendingButton.className ="btn btn-sm pending-book-request my-0 w-100 border border-r";
        pendingButton.type = "button";
        pendingButton.setAttribute("pid", activebook.id);
        pendingButton.textContent = "Pending";
        pendingButton.addEventListener("click", handlePendingButtonClick);

        restoreButton = document.createElement("button");
        restoreButton.className =
          "col btn btn-sm restore-book-request my-0 mx-1 border border-r";
        restoreButton.type = "button";
        restoreButton.setAttribute("pid", activebook.id);
        restoreButton.textContent = "Restore";
        restoreButton.addEventListener("click", handleRestoreButtonClick);

        soldButton = document.createElement("button");
        soldButton.className =
          "col btn btn-sm sold-book-request my-0 mx-1 border border-r";
        soldButton.type = "button";
        soldButton.setAttribute("pid", activebook.id);
        soldButton.textContent = "Sold";

        card.appendChild(img);
        card.appendChild(title);
        buttonContainer.appendChild(editButton);
        if (activebook.status == false) {
          buttonContainer.removeChild(editButton);
          buttonContainer.appendChild(pendingButton);
        }
        if (activebook.status == true) {
          buttonContainer.removeChild(editButton);
          buttonContainer.appendChild(restoreButton);
          buttonContainer.appendChild(soldButton);
        }
        card.appendChild(buttonContainer);
        cardCol.appendChild(card);
        cardrow.appendChild(cardCol);
        activeBookrow.appendChild(cardCol);
      });
      editProfileContainer.style.display = "none";
      bookedBookContainer.style.display = "none";
      editBookContainer.style.disaplay = "none";
      activeBookContainer.style.display = "block";
      activeBookContainer.scrollIntoView();
    },
  });
});
// Code for ajax to send the data to the views for edit profile

$(".save-change-button").click(function () {
  var Name = document.getElementById("id_Name").value;
  var Phone_Number = document.getElementById("id_Phone_Number").value;
  var latitude = document.getElementById("id_latitude").value;
  var address = document.getElementById("id_Address").value;
  var longitude = document.getElementById("id_longitude").value;
 
  $.ajax({
    type: "POST",
    url: "/edit-profile/",
    data: {
    
      Name: Name,
      Phone_Number: Phone_Number,
      address: address,
      latitude: latitude,
      longitude: longitude,
    },
    success: function (data) {
window.location.href="/profile/"

    },
  });
});

//code for sending ajax request to the backend for edit books info

const handleEditButtonClick = (event) => {
  const id = event.target.getAttribute("pid");
  $.ajax({
    type: "GET",
    url: "/editbook/",
    data: {
      book_id: id,
    },
    success: function (data) {
      editProfileContainer.style.display = "none";
      activeBookContainer.style.display = "none";
      bookedBookContainer.style.display = "none";
      editBookContainer.style.display = "block";
      const imageInputElement = document.getElementById("id_bookform-image");
      imageInputElement.removeAttribute("required");
      document.getElementById("id_bookform-title").value = data.title;
      document.getElementById("id_bookform-description").value =
        data.description;
      document.getElementById("id_bookform-original_price").value =
        data.original_price;
      document.getElementById("id_bookform-selling_price").value =
        data.selling_price;
      document.getElementById("id_bookform-condition").value = data.condition;
      document.getElementById("id_bookform-latitude").value = data.latitude;
      document.getElementById("id_bookform-longitude").value = data.longitude;
      document.getElementById("image-preview").src = data.image_url;
      var map = L.map("bookmap").setView([28.26689, 83.96851], 13);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
          '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
      var lat = data.latitude;
      var lng = data.longitude;
      var marker = new L.marker([lat, lng]).addTo(map);

      map.on("click", function (e) {
        var marker = new L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
        var lat = document.getElementById("id_bookform-latitude");
        lat.value = e.latlng.lat;
        var lng = document.getElementById("id_bookform-longitude");
        lng.value = e.latlng.lng;
      });
    },
  });
};

//code for sending ajax request to the backend for handling pending request accept
const handlePendingButtonClick = (event) => {
  const button = event.target;
  const id = button.getAttribute("pid");

  $.ajax({
    type: "GET",
    url: "/pending-request/",
    data: {
      book_id: id,
    },
    success: function (data) {
      const buttonContainer = button.closest(".button-container");
      buttonContainer.removeChild(button);
      buttonContainer.appendChild(restoreButton);
      buttonContainer.appendChild(soldButton);
    },
  });
};
//code for sending the ajax request to the backend for handling the restore request
const handleRestoreButtonClick = (event) => {
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

  checkbox.addEventListener("change", function () {
    submit.disabled = !checkbox.checked;
    submit.addEventListener("click", () => {
      popupWrapper.style.display = "none";
      const button = event.target;
      const id = button.getAttribute("pid");
      $.ajax({
        type: "GET",
        url: "/restore-request/",
        data: {
          book_id: id,
        },
        success: (data) => {
          const card = button.closest(".card");
          // Find the closest parent card
          const restoreButtons = card.getElementsByClassName(
            "restore-book-request"
          );

          // Remove all "restore" buttons within the card
          for (let i = 0; i < restoreButtons.length; i++) {
            card.removeChild(restoreButtons[i]);
            card.appendChild(editButton);
            card.removeChild(soldButton);
          }
        },
      });
    });
  });
};
//code for the booked book

const bookedBookButton = document.getElementById("booked-books");

bookedBookButton.addEventListener("click", () => {
  editProfileContainer.style.display = "none";
  activeBookContainer.style.display = "none";
  editBookContainer.style.display = "none";
  bookedBookContainer.style.display = "block";
  bookedBookContainer.scrollIntoView();

  // code for reverse geo encoding
  let cancelButton;
  

  $.ajax({
    type: "GET",
    url: "/booked-book/",
    data: {},
    success: function (data) {
      var tableBody = document.querySelector("#data-table tbody");
      var rows = tableBody.getElementsByTagName("tr");

      // Remove each row
      for (var i = rows.length - 1; i >= 0; i--) {
        var row = rows[i];
        tableBody.removeChild(row);
      }
      let chatButton
      data.data.forEach(async function (item) {
        cancelButton = document.createElement("button");
        cancelButton.textContent = "Cancel";
        cancelButton.setAttribute("pid", item.booked_id);
        cancelButton.className = "my-button-class";

        
        chatButton = document.createElement("button");
        chatButton.textContent = "Chat";
        chatButton.setAttribute("pid", item.booked_id);
        chatButton.className = "chat-button";
        chatButton.addEventListener("click", handleChatRequest)


        var disabledCancelButton = document.createElement("button");
        disabledCancelButton.textContent = "Cancel";
        disabledCancelButton.className = "my-button-class"; // Add your own CSS class if needed
        disabledCancelButton.addEventListener("click", function () {
          alert("Disabled clicked!");
        });

        var row = tableBody.insertRow();

        var titleCell = row.insertCell(0);
        var sellerCell = row.insertCell(1);
        var contactCell = row.insertCell(2);
        var addressCell = row.insertCell(3);
        var priceCell = row.insertCell(4);
        var bookedStatusCell = row.insertCell(5);
        var contactSellerCell = row.insertCell(6);
       
        titleCell.textContent = item.title;
        sellerCell.textContent = item.seller;
        contactCell.textContent = item.contact_no;
        priceCell.textContent = item.price;
        addressCell.textContent=item.location
        contactSellerCell.appendChild(chatButton);
        if (item.booked_status) {
          bookedStatusCell.appendChild(disabledCancelButton);
        } else {
          
          bookedStatusCell.appendChild(cancelButton);
          cancelButton.addEventListener("click", function (event) {
            handleCancelRequest(event, item.booked_id);
          });
        }
        //= item.booked_status ? 'Booked' : 'Not Booked';
      });
    },
  });
});


async function popupfunction(booked_id) {
  const popupWrapper = document.querySelector(".popup-wrapper");
  const close = document.querySelector(".close");
  const popup = document.querySelector(".popup");
  const checkbox = document.getElementById("checkbox");
  const submit = document.querySelector(".submit-btn");

  popupWrapper.style.display = "block";
  return new Promise((resolve, reject) => {
    close.addEventListener("click", () => {
      popupWrapper.style.display = "none";
      resolve(false);
    });

    popup.addEventListener("click", (event) => {
      event.stopPropagation();
    });

    checkbox.addEventListener("change", function () {
      submit.disabled = !checkbox.checked;
    });
    submit.addEventListener("click", () => {
      popupWrapper.style.display = "none";
      resolve(true);
    });
  });
}

function handleCancelRequest(event, booked_id) {
  popupfunction(booked_id).then((result) => {
    if (result) {
      $.ajax({
        type: "GET",
        url: "/cancel-book/",
        data: {
          booked_id: booked_id,
        },
        success: (data) => {
          var row = event.target.closest("tr");
          row.remove();
        },
      });
    }
  });
}
//code for the profile picture change

$(document).ready(function () {
  $("#upload-button").click(function () {
    const popupWrapper = document.querySelector(".edit-profile-popup-wrapper");
    const close = document.querySelector(".edit-profile-close");
    const popup = document.querySelector(".edit-profile-popup");
    const uploadPhoto = document.querySelector(".edit-profile-submit-btn");
    popupWrapper.style.display = "block";

    close.addEventListener("click", () => {
      popupWrapper.style.display = "none";
    });

    popup.addEventListener("click", (event) => {
      event.stopPropagation();
    });
    uploadPhoto.addEventListener("click", (event) => {
      const saveButton = document.createElement("Button");
      saveButton.className = "edit-profile-submit-btn";
      saveButton.textContent = "Save";

      const imageInput = document.querySelector("#image-input");
      imageInput.click();
      imageInput.addEventListener("change", () => {
        uploadButton = event.target;
        const imgElement = document.querySelector(
          ".edit-profile-popup-content .user-photo img"
        );
        parentOfUploadButton = uploadButton.parentNode;
        parentOfUploadButton.removeChild(uploadButton);
        parentOfUploadButton.appendChild(saveButton);
        var file = imageInput.files[0];
        if (file) {
          var reader = new FileReader();
          reader.onload = function (e) {
            imgElement.src = e.target.result;
          };
          reader.readAsDataURL(file);
        }
        saveButton.addEventListener("click", () => {
          var formData = new FormData();
          formData.append("image", imageInput.files[0]);
          $.ajax({
            url: "/edit-profile-photo/", // Replace with your API endpoint URL
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
              const image_url = response.image_url;
              popupWrapper.style.display = "none";
              const imgTag = document.querySelector(
                ".user-details .user-photo-container .user-photo img"
              );
              imgTag.src = image_url;
              const headerImgTag = document.querySelector(
                "#header-user-image #navbarDropdown img"
              );
              headerImgTag.src = image_url;
            },
            error: function () {
              alert("Image upload failed");
            },
          });
        });
      });
    });
  });
});

//code for the image field in the form
document.addEventListener("DOMContentLoaded", function () {
  var imageInput = document.getElementById("id_bookform-image"); // Replace with your image field ID
  var imagePreview = document.getElementById("image-preview");

  imageInput.addEventListener("change", function () {
    var file = imageInput.files[0];
    if (file) {
      var reader = new FileReader();
      reader.onload = function (e) {
        imagePreview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
});
// code for chatapp 
import { chatFunction } from '../../chatapp/js/chatapp.js';

function handleChatRequest(event){
  chatFunction(event);
}
