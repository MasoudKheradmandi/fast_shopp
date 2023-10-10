var dropzone = document.getElementById('dropzone');
var filename = document.getElementById('filename');
var fileInput = document.getElementById('fileInput');

dropzone.addEventListener('dragover', function(event) {
    event.preventDefault();
    dropzone.classList.add('highlight');

});

fileInput.addEventListener('change', function(event) {
    filename.innerHTML = 'File name: ' + fileInput.files[0].name;
});

dropzone.addEventListener('click', function(event) {
    document.getElementById('fileInput').click()
    
});

dropzone.addEventListener('dragleave', function(event) {
    event.preventDefault();
    dropzone.classList.remove('highlight');
});

dropzone.addEventListener('drop', function(event) {
    event.preventDefault();
    dropzone.classList.remove('highlight');
    var fileInput = document.getElementById('fileInput');
    fileInput.files = event.dataTransfer.files;
    filename.innerHTML = 'File name: ' + fileInput.files[0].name;
});