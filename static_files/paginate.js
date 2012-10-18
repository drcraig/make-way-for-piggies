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
    var current_page = $(".page"+hash);
    current_page.show();
    setHash(hash);
    $("#progress span").removeClass("current");
    $("#progress #progress-"+hash.slice(1)+" span").addClass("current");
    
    var next_page = current_page.next();
    var prev_page = current_page.prev();
    if (next_page.length == 0) {
        $('.page-turn#next a').hide();
    } else {
        $('.page-turn#next a').show();
    }
    if (prev_page.length == 0) {
        $('.page-turn#prev a').hide();
    } else {
        $('.page-turn#prev a').show();
    }

    if( window.location.hash == "" ) {
        $('#top-title').hide();
    } else {
        $('#top-title').show();
    }
    window.scrollTo(0);
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

  $('body').on('swipeleft',  function(e){goToNextPage();})
            .on('swiperight', function(e){goToPrevPage();});

  $('body').on('movestart', function(e) {
      if ((e.distX > e.distY && e.distX < -e.distY) ||
                (e.distX < e.distY && e.distX > -e.distY)) {
              e.preventDefault();
                }
      });

  $(window).resize(function() {
    $('iframe').each(function(index, value) {
      var width = $(value.parentElement).width()-80;
      var height = Math.round(0.75 * width);
      value.setAttribute('width', width);
      value.setAttribute('height', height);
    });
  });
});

