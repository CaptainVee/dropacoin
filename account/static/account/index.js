let thems=[
    {
        name:'Offor Emeka',
        url: './images/Rectangl.png',
        des: 'I am a digital comedian ask around',
        likes: '95 Purchases'
    },
    {
        name:'Nnamdi Marko',
        url:'./images/Rectangle.png',
        des: 'Trumph enjoys my video',
        likes: '105 Purchases'
    },
    {
        name:'Adabi Clinton',
        url: './images/Rectangls.png',
        des: 'I make memes video',
        likes: '55 Purchases'
    },
    
    {
        name:'Joseph Daalu',
        url: './images/Rectanglss.png',
        des: 'Joseph Daalu Creating videos to change the world',
        likes: '395 Purchases'
    }, 
    
]
let photos =[
    {
        name:'photo 1',
        url: './images/Rectanglss.png',
        des: 'I am a digital comedian ask around',
        likes: '95 Purchases'
    },
    {
        name:'photo 2',
        url:'./images/Rectangle.png',
        des: 'Trumph enjoys my video',
        likes: '105 Purchases'
    },
    {
        name:'photo 3',
        url: './images/Rectangl.png',
        des: 'I make memes video',
        likes: '55 Purchases'
    },
    {
        name:'photo 4',
        url: './images/Rectangls.png',
        des: 'Joseph Daalu Creating videos to change the world 395 Purchases',
        likes: '395 Purchases'
    }, 
    
]
 
let main = document.querySelector('.main')
let videoes=document.querySelector('videoes')
let musices=document.querySelector('musices')


    
    /*musices.addEventListener('click', function (){
        const sit= photos.map((photo, index)=>{
            return `
               <div>
                   <div>
                       <img src=${photo.url} class="foot" alt="might">
                   </div>
                   <h1>${photo.name}</h1>
                   <h3>${photo.name}</h3>
               </div>
            `;
        });
        main.innerHTML=sit
    })*/
 function video(){
    const sit= photos.map((photo)=>{
        return `
            <div class="h">
                <div class="foots">
                   <img src=${photo.url}  class="foot" alt="might">
               </div>
              
                <h1 class="maph1">${photo.name}</h1>
                <p class="mapp1">${photo.des}</p>
                <p class="mapp2">${photo.likes}</p>
           </div>
        `;
    });
    main.innerHTML=sit

 }

function music(){
   
        const sit= thems.map((them, index)=>{
            return `
               <div class="h">
                   <div class="foots">
                       <img src=${them.url} class="foot" alt="might">
                   </div>
                   
                        <h1 class="maph1">${them.name}</h1>
                        <p class="mapp1">${them.des}</p>
                        <p class="mapp2">${them.likes}</p>
                   
               </div>
            `;
        });
        main.innerHTML=sit
    }

 window.addEventListener('DOMContentLoaded', function user(){
     const sit= photos.map((photo, index)=>{
         return `
         <div class="r">
         <div class="footses">
                <img src=${photo.url} class="foot" alt="might">
            </div>
            
            <h1 class="maph1">${photo.name}</h1>
            <p class="mapp1">${photo.des}</p>
            <p class="mapp2">${photo.likes}</p>
         </div>
  `;
     });
     main.innerHTML=sit
 })
