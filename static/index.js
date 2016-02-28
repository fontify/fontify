Dropzone.options.uploadDropzone = {
  paramName: "file", // The name that will be used to transfer the file
  maxFilesize: 20, // MB
  maxFiles: 1,
  acceptedFiles: ".png, .jpg",
  dictDefaultMessage: "drop image here<br>or click to upload",
  accept: function(file, done) {
    if (file.name == "justinbieber.jpg") {
      done("Naha, you don't.");
    }
    else { done(); }
  },
  init: function() {
    this.on("complete", function(file) { 
        alert("completed uploading file");
        this.removeFile(file);
    });
  }
};