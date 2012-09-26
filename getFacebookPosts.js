/* Add JQuery, if not already there */
var h = document.getElementsByTagName("head")[0];
var jq = document.createElement("script");
jq.setAttribute("src", "https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js");
h.appendChild(jq);

// wait for the script to load, then...

$('body').append('<pre id="l33t"></pre>')
var l33t = $('#l33t')

var posts = []

$('.storyContent').each(function(index) {
   var $story = $(this);
   var timestamp, humantimestamp;
   $story.find('.uiStreamFooter span.uiStreamSource abbr').each(function(index) {
      timestamp = this.getAttribute('data-utime');
      humantimestamp = this.getAttribute('title');
   });
   $story.find('.userContent').each(function(index) {
      
      posts.push({'text': this.innerText, 'timestamp': timestamp, 'humantimestamp': humantimestamp});
   });
});

JSON.stringify(posts, null, " ")
l33t.html(JSON.stringify(posts, null, " "))
