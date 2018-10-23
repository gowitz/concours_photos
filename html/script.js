var jcontent = {
  "firstName": "John",
  "lastName": "Smith"
}

var jcontentGellery = {
  "alt": "Preview Image 7",
  "source": "images/thumbs/thumb3.jpg",
  "image": "images/big/image3.jpg",
  "description": "Preview Image 7 Description"
}

var output = document.getElementById('output');
/*
<img alt="Preview Image 7"
   src="images/thumbs/thumb3.jpg"
   data-image="images/big/image3.jpg"
   data-description="Preview Image 7 Description">
*/
output.innerHTML = jcontent.firstName;
