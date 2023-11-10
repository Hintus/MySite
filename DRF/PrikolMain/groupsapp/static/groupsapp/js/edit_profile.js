var but = document.getElementById('edit_but');
var edit_img = document.getElementById('edit_img')
var values = document.getElementById('profile_values')
var input = document.getElementById('inputs')
var name = document.getElementById('name_div')

input.style.opacity = '0%';

var cliked = true;

but.addEventListener('click',()=>{
    if(cliked == true){
        values.style.opacity = '0%';
        input.style.opacity = '100%';
        edit_img.style.backgroundColor = "rgb(21, 190, 32)"
        edit_img.src = 'https://i.ibb.co/q7Mk9R2/cross.png'
        cliked = false;
    }else{
        values.style.opacity = '100%';
        input.style.opacity = '0%';
        edit_img.style.backgroundColor = "rgb(0, 0, 0)"
        edit_img.src = 'https://i.ibb.co/FnSDqDK/pencil.png'
        cliked = true;
    }
})