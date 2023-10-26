var but = document.getElementById('edit_but');
var edit_img = document.getElementById('edit_img')

var cliked = true;

but.addEventListener('click',()=>{
    if(cliked == true){
        edit_img.src = 'https://i.ibb.co/q7Mk9R2/cross.png'
        cliked = false;
    }else{
        edit_img.src = 'https://i.ibb.co/FnSDqDK/pencil.png'
        cliked = true;
    }
})