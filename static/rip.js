
$(document).ready(function() {
    var selected;
    var reset_selected_skills = function() {
      $(".skill").removeClass("selected");
    }
    var select_skill = function(name) {
      var id = encodeURIComponent(name);
      $("#"+id).addClass("selected");
    }
    var select_skills_for_experience = function(exp) {
      var title = decodeURIComponent(exp.id);
      for (var i=0; i<experiences.length; i++) {
	var obj = experiences[i];
	if (title == obj.title) {
	  for (var j=0; j<obj.skills.length; j++) {
	    select_skill(obj.skills[j]);
	  }
	  break;
	}
      }

    }

    var reset_selected_experience = function() {
      if (selected) {
	$(selected).removeClass("selected");
	$(selected).children("p").hide(); //('slow',function() {});
	selected = null;
      }
    };
    var select_experience = function() {
      reset_selected_experience();
      selected = this;
      $(this).addClass("selected");
      $(this).children("p").slideDown('slow',function() {});
      reset_selected_skills();
      select_skills_for_experience(this);
    };
    $(".experience").hover(select_experience, function(){});
 
    selected = $(".experience:first")[0];
    var first = $(".experience:first").addClass("selected").children("p").slideDown('slow');
    select_skills_for_experience($(".experience:first")[0]);
    //select_skill("Cappuccino");
  });
