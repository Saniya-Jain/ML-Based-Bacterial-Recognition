var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
 };

 x_coord = document.getElementById('x-coord')
 y_coord = document.getElementById('y-coord')

 document.getElementById('output').addEventListener('mousedown', (e) => {
    var rectElement = document.getElementById('box');

    // Get the target
    const target = e.target;

    // Get the bounding rectangle of target
    const rect = target.getBoundingClientRect();

    // Mouse position
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    console.log(x,y,rect);
    
    // if(rectElement.style.display === 'none'){
        rectElement.style.display = ''
        rectElement.style.position = 'absolute'
        rectElement.style.top = y + 15
        rectElement.style.left = x - 15

        x_coord.value = x-15
        y_coord.value = y+15
    // }else{
    //     var form = document.getElementsByTagName('form')[0]

    //     var svg = document.createElement('svg')
    //     svg.setAttribute("style",`position:absolute;top:${y+15};left:${x-15}`)

    //     var box = document.createElement('rect')
    //     box.setAttribute("width", "50")
    //     box.setAttribute("height", "50")
    //     box.setAttribute("style", "fill:none;stroke-width:1;stroke:red")
        
    //     svg.appendChild(box)

    //     form.appendChild(svg)
    // }
});