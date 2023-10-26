var group_but = document.getElementById('group_button')
var profile_but = document.getElementById('profile_button')
var profile_block = document.getElementById('profile_content')
var group_block = document.getElementById('group_content')


var is_active = false;

group_block.style.visibility = 'hidden'

group_but.addEventListener('click',()=>{
    if(is_active == false){
        group_but.style.opacity = '100%'
        profile_but.style.opacity = '50%'
        is_active = true;
        profile_block.style.visibility = 'hidden';   
        group_block.style.visibility = 'visible';
    }
})

profile_but.addEventListener('click',()=>{
    if(is_active == true){
        group_but.style.opacity = '50%'
        profile_but.style.opacity = '100%'
        is_active = false;
        profile_block.style.visibility = 'visible';
        group_block.style.visibility = 'hidden';
    }
})