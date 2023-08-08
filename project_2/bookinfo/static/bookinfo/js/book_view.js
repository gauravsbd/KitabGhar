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
