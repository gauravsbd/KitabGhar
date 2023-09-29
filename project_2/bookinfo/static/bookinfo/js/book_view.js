const buyButton = document.getElementById("buy");
const popupWrapper = document.querySelector(".popup-wrapper");
const close = document.querySelector(".close");
const popup = document.querySelector(".popup");
const checkbox = document.getElementById("checkbox");
const submit = document.querySelector(".submit-btn");

buyButton.addEventListener("click", () => {
  alert("done")
  popupWrapper.style.display = "block";
});

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
    const book = document.getElementById("book-id");
    const book_id = book.getAttribute("attr");

    $.ajax({
      type: "GET",
      url: "/book-book/",
      data: {
        book_id: book_id,
      },
      success: function (data, textStatus, xhr) {
        alert("done");
        if (data.error === "authentication_required") {
          var redirectUrl = data.redirect_url;
          if (redirectUrl) {
            window.location.href = redirectUrl;
          }
        }
      },
      error: function (xhr, textStatus, errorThrown) {
        if (xhr.status === 401) {
          window.location.href = "/login/";
          // User is not authenticated, handle this scenario
          // You can redirect to the login page or show an error message
        } else {
          // Handle other errors
          console.error("AJAX error:", errorThrown);
        }
      },
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var imageInput = document.getElementById("id_image"); // Replace with your image field ID
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


// code for the book form
const form = document.getElementById("multi-step-form");
const progressBar = document.getElementById("progress-bar");
const steps = [...document.querySelectorAll(".step")];
const nextButtons = [...document.querySelectorAll(".next-button")];
const prevButtons = [...document.querySelectorAll(".prev-button")];

const lastStepIndex = steps.length - 1;
let currentStep = 0;

function updateProgressBar() {
  const percent = (currentStep / lastStepIndex) * 100;
  progressBar.style.width = percent + "%";
}

function showStep(step) {
  steps.forEach((step, index) => {
    step.style.display = index === currentStep ? "block" : "none";
  });
  updateProgressBar();
}

function updateNextButtonAvailability() {
  if (currentStep === 0) {
    const title = document.getElementById("id_title");
    const description = document.getElementById("id_description");
    const category = document.getElementById("id_category");

    if (
      title.value.trim() !== "" &&
      description.value.trim() !== "" &&
      category.value !== ""
    ) {
      nextButtons[0].removeAttribute("disabled");
    } else {
      nextButtons[0].setAttribute("disabled", "disabled");
    }
  } else if (currentStep === 1) {
    const originalPrice = document.getElementById("id_original_price");
    const sellingPrice = document.getElementById("id_selling_price");
    const image = document.getElementById("id_image");

    if (
      originalPrice.value.trim() !== "" &&
      sellingPrice.value.trim() !== "" &&
      image.value !== ""
    ) {
      nextButtons[1].removeAttribute("disabled");
    } else {
      nextButtons[1].setAttribute("disabled", "disabled");
    }
  }
}

nextButtons.forEach((button, index) => {
  button.addEventListener("click", () => {
    if (currentStep < lastStepIndex) {
      currentStep++;
      showStep(currentStep);
    }
  });
});

prevButtons.forEach((button, index) => {
  button.addEventListener("click", () => {
    if (currentStep > 0) {
      currentStep--;
      showStep(currentStep);
    }
  });
});

form.addEventListener("change", updateNextButtonAvailability);
updateNextButtonAvailability();
showStep(currentStep);
