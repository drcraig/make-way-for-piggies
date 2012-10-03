function getHash() {
  var hash = window.location.hash;
  if (hash === "")
  {
      hash = "#cover";
  }
  return hash;
}

function setHash(hash) {
    if (hash === "#cover") {
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

function goToNextPage() {
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var next_page = curr_page.next();
    if (next_page.length !== 0) {
      setCurrentPage('#'+next_page.attr('id'));
    }
}

function goToPrevPage() {
    var hash = getHash();
    var curr_page = $(".page"+hash);
    var prev_page = curr_page.prev();
    if (prev_page.length !== 0) {
      setCurrentPage('#'+prev_page.attr('id'));
    }
}

$(document).ready( function() {
  setCurrentPage(getHash());  

  $("#next").click(function(event){
    event.preventDefault();
    goToNextPage();
  });

  $(document).keydown(function(event) {
    var code = (event.keyCode ? event.keyCode : event.which);
    if(code == 74 || code == 39) {
        goToNextPage();
    }
    if(code == 75 || code == 37) {
        goToPrevPage();
    }
  });

  $("#prev").click(function(event){
    event.preventDefault();
    goToPrevPage();
  });

  $("a").click(function(event){
    var href = event.currentTarget.getAttribute("href");
    if (href[0] === "#") {
        event.preventDefault();
        setCurrentPage(href);
    }
    
  });
});


