// connect to appropriate page elements via the DOM
var uploader = document.getElementById('uploader');
var fileButton =  document.getElementById('fileButton');
// add an event listener to the 
fileButton.addEventListener('change', function(e){
    var file = e.target.files[0];
    // Create file metadata including the content type
    var metadata = {
        customMetadata: {
            userid: '1',
            activity: 'Course Work',
            notes: 'A fixed message about this file'
        }
    };
    // set  upload locaation
    var storageRef = firebase.storage().ref('img/'+file.name);
    //upload file and metadata
    var task = storageRef.put(file, metadata);
    // set callback event + function, error function and complete function
    task.on('state_changed', function progress(snapshot) {
    var percentage = (snapshot.bytesTransferred/snapshot.totalBytes)*100;
    uploader.value = percentage;
   
  }, function error(err) {
    alert("File upload failed:" + err.message);

  },function complete() {
    alert("File upload successful");
    // For instance, get the download URL: https://firebasestorage.googleapis.com/...
        task.snapshot.ref.getDownloadURL().then(function(downloadURL) {
        console.log('File available at', downloadURL);
    });
  });
});  