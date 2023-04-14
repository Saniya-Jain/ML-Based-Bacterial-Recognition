var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    // console.log(event.target.files[0])
};

x_coord = document.getElementById('x-coord')
y_coord = document.getElementById('y-coord')

xCoords = []
yCoords = []

//  const cursorSquare = document.querySelector('.square');
//  const cursorPointed = document.querySelector('.pointed');
 
 
//  const moveCursor = (e)=> {
//     cursorSquare.visibility = 'visible'
//    const mouseY = e.clientY;
//    const mouseX = e.clientX;
    
//    cursorSquare.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
   
//    cursorPointed.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
  
//  }
 
// document.querySelector('#output').addEventListener('mousemove', moveCursor)

var colonyCount = 0

function genBox(e){
    var rectElement = document.getElementById('box');

    // Get the target
    const target = e.target;

    // Get the bounding rectangle of target
    const rect = target.getBoundingClientRect();

    // Mouse position
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    console.log(e.pageX,e.pageY,rect);

    // if(rectElement.style.display === 'none'){
    //     rectElement.style.display = 'block';
    //     rectElement.style.top = (e.pageY - 25) + "px" ;
    //     rectElement.style.left = (e.pageX - 25) + "px";
    //     console.log(e.pageY - 25,e.pageX - 25)

    // }else{
        var box = document.createElement('div')
        box.id = 'box-'+colonyCount
        box.classList.add('box')
        box.style.top = (e.pageY - 25) + "px"
        box.style.left = (e.pageX - 25) + "px"
        console.log(e.pageY - 25,e.pageX - 25)
        box.innerHTML = colonyCount
        var ele = document.getElementById('element')
        ele.appendChild(box);
    // }

    xCoords.push(x-15);
    yCoords.push(y+15);
    x_coord.value = xCoords;
    y_coord.value = yCoords;
    colonyCount += 1;
    
};
