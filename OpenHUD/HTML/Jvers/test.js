<button onclick="myFunction()">Try it</button>
    <script>
    function myFunction() {
        var x = document.getElementById("gfg");
        x.querySelector("p").style.backgroundColor = "Green";
        x.querySelector("p").style.color = "white";
    }
    </script>



// Get the video
var video = document.getElementById("myVideo");

// Get the button
var btn = document.getElementById("myBtn");

// Pause and play the video, and change the button text
function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}

