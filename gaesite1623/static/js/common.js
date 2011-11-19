var myX = -40;
var x=5;

var myY = 100;
var y=1;
var swX = 1;
var swY = 1;

var swY2 = 1;
var swX2 = -1;
myTimer = setInterval(function (){
	
	var canvas = document.getElementById('canvasL');
	var ct = canvas.getContext('2d');
	
	ct.clearRect(0, 0, 300, 200);
	
	ct.beginPath();
	ct.arc(myX, myY, 10, 0,Math.PI*2, false);
	ct.fillStyle = '#54Fa5F';
	ct.fill();

	x=(x+(x*0.002)*swX2);	
	myX=myX+x*swX;

	y=(y+(y*0.001)*swY2)

	if(myX > 300){
		swX=-1;
	}else if(myX<0){
		swX=1;
	}

	myY=myY+y*swY
	if(myY > 140){
		swY=-1;
	}else if(myY<5){
		swY=1;
	}
	
	if(y>5){
		swY2=-1;
	}else if(y<1){
		swY2=1;
	}
	
	if(x>5){
		swX2=-1;
	}else if(x<1){
		swX2=1;
	}
	
	
}, 10);
window.onload = myTimer;