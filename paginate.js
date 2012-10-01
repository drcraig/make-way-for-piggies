function getHash() {
  var hash = window.location.hash;
  if (hash === "")
  {
      hash = "#cover";
  }
  return hash;
}

$(document).ready( function() {
  $(".page").hide();
  
  var hash = getHash()
  $(".page"+hash).show();

  $("#next").click(function(event){
    event.preventDefault();
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var next_page = curr_page.next();
    curr_page.hide();
    next_page.show();
    window.location.hash = next_page.attr('id');
  });

  $("#prev").click(function(event){
    event.preventDefault();
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var prev_page = curr_page.prev();
    curr_page.hide();
    prev_page.show();
    window.location.hash = prev_page.attr('id');
  });
});


