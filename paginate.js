function getHash() {
  var hash = window.location.hash;
  if (hash === "")
  {
      hash = "#cover";
  }
  return hash;
}

function setHash(hash) {
    if (hash === "#cover")
    {
        window.location.hash = "";
    } else {
        window.location.hash = hash;
    }
}

function setCurrentPage(hash) {
    $(".page").hide();
    $(".page"+hash).show();
    setHash(hash);
    $("#progress span").removeClass("current");
    $("#progress #progress-"+hash.slice(1)+" span").addClass("current");
}

$(document).ready( function() {
  setCurrentPage(getHash());  

  $("#next").click(function(event){
    event.preventDefault();
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var next_page = curr_page.next();
    if (next_page.length !== 0) {
      setCurrentPage('#'+next_page.attr('id'));
    }
  });

  $("#prev").click(function(event){
    event.preventDefault();
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var prev_page = curr_page.prev();
    if (prev_page.length !== 0) {
      setCurrentPage('#'+prev_page.attr('id'));
    }
  });

  $("#progress a").click(function(event){
    event.preventDefault();
    setCurrentPage(event.currentTarget.hash); 
  });
});


