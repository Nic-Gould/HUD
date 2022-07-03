const elem = document.getElementById("leftPanel")
function slide(){
	if (elem.style.left)="0px";
		{
		slidein()
		}
	if (document.getElementById("leftPanel").style.left)="-350";
		{
			slideout()
		}
}

function slideout() {
	let id = null;
	clearInterval(id);
  	id = setInterval(frame, 5);
  	const elem = document.getElementById("leftPanel");   
  	
	let pos = -350;
	if (pos <=0) {
		pos++
		elem.style.left = pos + "px"; 
	}
 
}
function slidein() {
	let id = null;
	clearInterval(id);
  	id = setInterval(frame, 5);
  	const elem = document.getElementById("leftPanel");   
  	
	let pos = 0;
	if (pos >=350) 
		{
		pos--
		elem.style.left = pos + "px"; 
		}
// asdfg<iframe width="1920px" height="1080px" src="https://camstreamer.com/embed/c7ccfbc99611d99/S-884?rel=0" frameborder="0" allowfullscreen="yes"></iframe>	}
}