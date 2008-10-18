
$(document).ready(function() {
    var selected;
    var reset_selected_experience = function() {
      if (selected) {
	$(selected).removeClass("selected");
	$(selected).children("p").slideUp('slow',function() {});
	selected = null;
      }
    };
    var select_experience = function() {
      reset_selected_experience();
      selected = this;
      $(this).addClass("selected");
      $(this).children("p").slideDown('slow',function() {});
    };
    $(".experience").hover(select_experience, function(){});
    
    var first = $(".experience:first").addClass("selected").children("p").slideDown('slow');
    window.console.log(first);
  });
