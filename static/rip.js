$(document).ready(function() {
    var selected;
    var reset_selected_skills = function() {
      $("#skills .selected").animate({fontSize: "1.25em"},500).removeClass("selected");
    }
    var select_skill = function(name) {
      var id = name.replace(/[ .!]+/g,"");
      $("#"+id).animate({fontSize: "1.5em"}, 500).addClass("selected");
    }
    var select_skills_for_experience = function(exp) {
      var title = exp.id.replace(/[ .!]+/g,"");
      for (var i=0; i<experiences.length; i++) {
	var obj = experiences[i];
	if (title == obj.id) {
	  for (var j=0; j<obj.skills.length; j++) select_skill(obj.skills[j]);
	  break;
	}}};
    var reset_selected_experience = function() {
      $(".experience").removeClass("selected").children("p").slideUp('slow');
    };
    var select_experience = function() {
      reset_selected_experience();
      reset_selected_skills();
      selected = this;
      $(this).addClass("selected").children("p").show();
      select_skills_for_experience(this);
    };
    $(".experience").hover(select_experience, function(){});
    selected = $(".experience:first")[0];
    var first = $(".experience:first").addClass("selected").children("p").show();
    select_skills_for_experience($(".experience:first")[0]);
  });

