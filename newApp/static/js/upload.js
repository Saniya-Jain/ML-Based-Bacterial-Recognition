var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
    // console.log(event.target.files[0])
};

 x_coord = document.getElementById('x-coord')
 y_coord = document.getElementById('y-coord')

 document.getElementById('output').addEventListener('onclick', (e) => {
    var rectElement = document.getElementById('box');

    // Get the target
    const target = e.target;

    // Get the bounding rectangle of target
    const rect = target.getBoundingClientRect();

    // Mouse position
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    console.log(e.PageX,e.PageY,rect);

    rectElement.style.display = ''
    rectElement.style.position = 'absolute'
    rectElement.style.top = e.PageY
    rectElement.style.left = e.PageX

    x_coord.value = x-15
    y_coord.value = y+15
});

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

    rectElement.style.display = ''
    rectElement.style.position = 'absolute'
    rectElement.style.top = e.pageY - 25
    rectElement.style.left = e.pageX - 25

    x_coord.value = x-15
    y_coord.value = y+15
    
};
