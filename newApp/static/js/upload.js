var colonyCount = 1
x_coord = document.getElementById('x-coord')
y_coord = document.getElementById('y-coord')

xCoords = []
yCoords = []

var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    // console.log(event.target.files[0])
    document.getElementsByTagName('button')[0].disabled = false;
    var boxes = document.getElementsByClassName('box');
    var l = boxes.length;
    var ele = document.getElementById('element');
    console.log('boxes', boxes);
    for(i = 0; i < l; i++){
        ele.removeChild(boxes[0])
    }
    colonyCount = 1
};

colonies = {}


function genBox(e){
    // Get the target
    const target = e.target;

    // Get the bounding rectangle of target
    const rect = target.getBoundingClientRect();

    // Mouse position
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    console.log(e.pageX,e.pageY,rect);

    var coords = []

    var box = document.createElement('div')
    box.id = 'box-'+colonyCount
    box.classList.add('box')
    box.style.top = (e.pageY - 25) + "px"
    box.style.left = (e.pageX - 25) + "px"
    // console.log(e.pageY - 25,e.pageX - 25)
    // box.innerHTML = "<i class='fa-regular fa-xmark'></i>"
    box.innerHTML = '<span class = "cut" onclick = "deleteBox(event);">&times</span>'
    // box.innerHTML = '<button type="button" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
    var ele = document.getElementById('element')
    ele.appendChild(box);

    xCoords.push(x-15);
    yCoords.push(y+15);
    coords.push(x-15);
    coords.push(y+15);

    x_coord.value = xCoords;
    y_coord.value = yCoords;
    colonies[box.id] = coords
    console.log(colonies)
    colonyCount += 1;
    
};

function deleteBox(e){
    const target = e.target.parentNode.id;
    console.log(target);
    var ele = document.getElementById('element');
    ele.removeChild(document.getElementById(target));
    delete colonies[target]
}

function addCoords(){
    document.forms["form"]["colony"].value = JSON.stringify(colonies);
}