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
