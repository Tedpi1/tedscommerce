var slides= document.querySelectorAll('.slide');
var btns = document.querySelectorAll('.radio');
let currentSlide = 1;

//javascript for image slider manual navigation
var manualNav = function(manual){
    slides.forEach((slide) =>{
        slide.classList.remove('active');
        btns.forEach((btn) =>{
            btn.classList.remove('active');
        })
    });
    slides[manual].classList.add('active');
    btns[manual].classList.add('active');
}
btns.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        manualNav(i);
        currentSlide = i
    })
})  
//image autoplay
var repeat= function(activeClass){
    let active= document.getElementsByClassName('active');
    let i = 1;
    var repeater = () => {
        setTimeout(function(){
            [...active].forEach((activeSlide) => {
                activeSlide.classList.remove('active');
            })
            slides[i].classList.add('active')
            btns[i].classList.add('active')
            i++
            if(slides.length == i){
                i=0
            }
            if(i >= slides.length){
                return;
            }
            repeater()
        }, 10000);
    }
    repeater()
}
repeat()


//testimonial
// Access the testimonials
let testSlide = document.querySelectorAll('.testItem');
// Access the indicators
let dots = document.querySelectorAll('.dot');

var counter = 0;

// Add click event to the indicators
function switchTest(currentTest){
    currentTest.classList.add('active');
    var testId = currentTest.getAttribute('attr');
    if(testId > counter){
        testSlide[counter].style.animation = 'next1 0.5s ease-in forwards';
        counter = testId;
        testSlide[counter].style.animation = 'next2 0.5s ease-in forwards';
    }
    else if(testId == counter){return;}
    else{
        testSlide[counter].style.animation = 'prev1 0.5s ease-in forwards';
        counter = testId;
        testSlide[counter].style.animation = 'prev2 0.5s ease-in forwards';
    }
    indicators();
}

// Add and remove active class from the indicators
function indicators(){
    for(i = 0; i < dots.length; i++){
        dots[i].className = dots[i].className.replace(' active', '');
    }
    dots[counter].className += ' active';
}

// Code for auto sliding
function slideNext(){
    testSlide[counter].style.animation = 'next1 0.5s ease-in forwards';
    if(counter >= testSlide.length - 1){
        counter = 0;
    }
    else{
        counter++;
    }
    testSlide[counter].style.animation = 'next2 0.5s ease-in forwards';
    indicators();
}
function autoSliding(){
    deleteInterval = setInterval(timer, 4000);
    function timer(){
        slideNext();
        indicators();
    }
}
autoSliding();

// Stop auto sliding when mouse is over the indicators
const container = document.querySelector('.indicators');
container.addEventListener('mouseover', pause);
function pause(){
    clearInterval(deleteInterval);
}

// Resume sliding when mouse is out of the indicators
container.addEventListener('mouseout', autoSliding);
//adding placeholder to input field
var form_fields= document.getElementsByTagName('input');
form_fields[0].placeholder="first_sname";
form_fields[1].placeholder="last_name";
form_fields[2].placeholder="username";
form_fields[3].placeholder="email";
form_fields[4].placeholder="password"
form_fields[5].placeholder="confirm password"

for(var fields in form_fields){
    form_fields[fields].className+=" form-control"
}

// product
const image = document.getElementById( 'productImg' );
const btn = document.getElementsByClassName( 'btn' );

btn[0].addEventListener( 'click', function(){
    image.src = './img/1.png';
    for( bt of btn ){
        bt.classList.remove( 'active' );
    }
    this.classList.add( 'active' );
} );
btn[1].addEventListener( 'click', function(){
    image.src = './img/2.png';
    for( bt of btn ){
        bt.classList.remove( 'active' );
    }
    this.classList.add( 'active' );
} );
btn[2].addEventListener( 'click', function(){
    image.src = './img/3.png';
    for( bt of btn ){
        bt.classList.remove( 'active' );
    }
    this.classList.add( 'active' );
} );

//product image
let bigImg =document.querySelector('.big-image img')
function showImg(pic){
    bigImg.src=pic
}
bigImg.addEventListener('click',function(){
    bigImg.src="{%static 'images/shoes.jpg'%}"
})

// add toggle button
const form= document.querySelector('form')
const fullName=document.getElementById('name')
const email=document.getElementById('email')
const subject=document.getElementById('subject')
const message=document.getElementById('message')


function sendEmail(){
    const bodyMessage =`Name:${fullName.value}<br> Email: ${email.value}<br> 
    Subject: ${subject.value} <br> Message: ${message.value}`;
    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "moroted16@gmail.com",
        Password : "D7D714AEDD302CF738A354160A9AD0646CEA",
        To : 'moroted16@gmail.com',
        From : "moroted16@gmail.com",
        Subject : subject.value,
        Body : bodyMessage
    }).then(
        message => {
            if(message=='OK'){
                Swal.fire({
                    title: "Success!",
                    text: "Message Sent Successfully!",
                    icon: "success"
                });
            }
        }
    );
}

form.addEventListener('submit', (e)=>{
    e.preventDefault();
    sendEmail();
})