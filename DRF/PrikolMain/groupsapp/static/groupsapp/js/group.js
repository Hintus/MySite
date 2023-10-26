var group_but = document.getElementById('group_button');
var chats_but = document.getElementById('chats_button');
var basket_but = document.getElementById('basket_button');
var members_but = document.getElementById('members_button');

var active = 0;

const buttons = [group_but,chats_but,basket_but,members_but];

var group_block =document.getElementById('group_block');
var chats_block =document.getElementById('chats_block');
var basket_block =document.getElementById('basket_block');
var members_block =document.getElementById('members_block');

const bloks = [group_block, chats_block, basket_block, members_block]

group_but.addEventListener('click',()=>{
    if(active != 0){
        buttons[active].style.opacity = '50%';
        bloks[active].style.visibility = 'hidden';
        active = 0;        
        buttons[active].style.opacity = '100%';
        bloks[active].style.visibility = 'visible';
    }
})

chats_but.addEventListener('click',()=>{
    if(active != 1){
        buttons[active].style.opacity = '50%';
        bloks[active].style.visibility = 'hidden';
        active = 1;        
        buttons[active].style.opacity = '100%';
        bloks[active].style.visibility = 'visible';
    }
})

basket_but.addEventListener('click',()=>{
    if(active != 2){
        buttons[active].style.opacity = '50%';
        bloks[active].style.visibility = 'hidden';
        active = 2;        
        buttons[active].style.opacity = '100%';
        bloks[active].style.visibility = 'visible';
    }
})

members_but.addEventListener('click',()=>{
    if(active != 3){
        buttons[active].style.opacity = '50%';
        bloks[active].style.visibility = 'hidden';
        active = 3;        
        buttons[active].style.opacity = '100%';
        bloks[active].style.visibility = 'visible';
    }
})