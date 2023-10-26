var but = document.getElementById('minion_activate');

var num = 0;

  function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;} 

but.addEventListener('click',()=>{
    num += 1;
    but.insertAdjacentHTML('BeforeBegin',
    `<img class = "minion" id = "minion_img${num}">`
    )
    var img = document.getElementById(`minion_img${num}`)
    img.src = "https://w7.pngwing.com/pngs/582/656/png-transparent-animal-steppe-horse-steed-horses.png";
    img.style.width = '150px';
    img.style.height = '150px';
    var right = getRandomInt(0,1300);
    img.style.right = right + 'px'
    let start = Date.now();
        let timer = setInterval(function(){
            let timePassed = Date.now()-start;
            if(timePassed >= 20000 )
            {clearInterval(timer);
            return;
            }
            img.style.top = timePassed*0.1+'px';
            },20)
})