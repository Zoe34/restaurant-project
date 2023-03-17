
$(document).ready(function(){
    $('.done').mouseover("hover", function(){
        $('.done').css('color', 'green');
    });
});
    
document.addEventListener('DOMContentLoaded', function() {
    var navbar = document.querySelectorAll('.navbar');
    M.Navbar.init(navbar);
  });