var div = document.getElementById('search_div');
var img = document.getElementById('img_search');

div.style.width = '40px';

img.addEventListener('click',()=>{
    div.style.borderRadius = '20px';
    if(div.style.width == '40px'){
        let start = Date.now();
        let timer = setInterval(function(){
            let timePassed = Date.now()-start;
            if(timePassed >= 200 )
            {clearInterval(timer);
            return;
            }
            div.style.width = timePassed*1.4+'px';
        },20)
        setTimeout(() => {
            div.insertAdjacentHTML('afterBegin',
            '<form id = "parent"><input id = "input" class = "search_input_group"></input></form>'
            )
            img.src = "https://cdn-icons-png.flaticon.com/128/3917/3917759.png";    
        }, 290);
    }
    else{
        var input = document.getElementById('input');
        var parent = document.getElementById('parent');
        parent.removeChild(input)
        img.src = "https://cdn-icons-png.flaticon.com/128/3917/3917132.png";
        let start = Date.now();
        let timer = setInterval(function(){
            let timePassed = start-Date.now();
            if(timePassed <= -200 )
            {clearInterval(timer);
            return;
            }
            div.style.width = 280+(timePassed*1.3)+'px';
        },20)
        setTimeout(() => {            
        div.style.width = '40px'
        }, 281)
    }
})

