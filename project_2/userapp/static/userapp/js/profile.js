const edit=document.querySelector(".edit-profile");
const formContainer=document.querySelector(".form-container");


formContainer.style.display='none';


edit.addEventListener("click",()=>{
    formContainer.style.display='block';
});
