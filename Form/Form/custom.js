let toggle = document.getElementsByClassName("toggle-icon")[0];
let wrapper = document.getElementsByClassName("wrapper-box")[0]
let allHide = document.getElementsByClassName("d-n")[0];
let sec1 = document.getElementById("sec_1")
let sec2 = document.getElementById("sec_2")
let sec3 = document.getElementById("sec_3")
let sec4 = document.getElementById("sec_4")
toggle.addEventListener("click" , function(){
    wrapper.classList.toggle("toggle");
    allHide.classList.toggle("d");
    sec1.classList.toggle("section-1")
    sec2.classList.toggle("section-1")
    sec3.classList.toggle("section-1")
    sec4.classList.toggle("section-1")
})


var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

let bell = document.getElementById("bell");
let noti_view = document.getElementById("noti_view")
bell.addEventListener("click" , function(){
  noti_view.classList.toggle("notiShow")
})

let userEdit = document.getElementById("userEdit");
let editView = document.getElementById("editView")
userEdit.addEventListener("click" , function(){
  editView.classList.toggle("profileOption")
})