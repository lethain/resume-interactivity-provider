
$(document).ready(function() {
    var select_experience = function() {
      $(this).addClass("selected");
    };
    var unselect_experience = function() {
      //$(this).removeClass("selected");
    };
    $(".experience").hover(select_experience, unselect_experience);
    

  });
