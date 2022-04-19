// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

function open_modal(name, location, admin, police_dept, hospital_contact){
    var modal = document.querySelector('.modal');
    var img_cont = document.getElementById('img_container')
    var details_cont = document.getElementById('details_container')
//    img_cont.innerHTML="<img class=\"selected_img\" src=\"/files/"+url+"\">";
    details_cont.innerHTML="<p class=\"details_caption_txt\">"+name+"</p> <p class=\"details_description_txt\">in "+location+"</p> <p class=\"details_category_txt\">Admin - "+admin+"</p> <p class=\"details_location_txt\">Police department - "+police_dept +"</p> </p> <p class=\"details_description_txt\">Hospital contact - "+hospital_contact+"</p>";
    modal.style.display = "block";
}

function close_modal(){
    var modal = document.querySelector('.modal');
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modal = document.querySelector('.modal');
      if (event.target == modal) {
        modal.style.display = "none";
      }
}