// Burger nav work
//https://www.youtube.com/watch?v=At4B7A4GOPg - Web Dev Simplified

const burgerButton = document.getElementsByClassName('burger-button')[0]
const navLinks = document.getElementsByClassName('nav-links')[0]

burgerButton.addEventListener('click', () => {
    navLinks.classList.toggle('active')
})

// On scroll page
//https://www.youtube.com/watch?v=T33NN_pPeNI - Beyond Fireship + Understending with Web Dev Simplified https://www.youtube.com/watch?v=2IbRtjez6ag&t=1s
const hiddenElements = document.querySelectorAll('.hidden');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
        else {
            entry.target.classList.remove('show');
        }
    });
});

hiddenElements.forEach((el) => observer.observe(el));

//hover animation
const card1 = document.getElementById('1');
const text2 = document.getElementById('2');

//Touch on mobile
//https://www.youtube.com/watch?v=TaPdgj8mucI Understanding with Web Dev Simplified
card1.addEventListener("touchstart", function() {
    text2.classList.add('card-hover');
})

const card3 = document.getElementById('3');
const text4 = document.getElementById('4');


card3.addEventListener("touchstart", function() {
    text4.classList.add('card-hover');
})

const card5 = document.getElementById('5');
const text6 = document.getElementById('6');


card5.addEventListener("touchstart", function() {
    text6.classList.add('card-hover');
})

const card7 = document.getElementById('7');
const text8 = document.getElementById('8');


card7.addEventListener("touchstart", function() {
    text8.classList.add('card-hover');
})

const card9 = document.getElementById('9');
const text10 = document.getElementById('10');


card9.addEventListener("touchstart", function() {
    text10.classList.add('card-hover');
})

const card11 = document.getElementById('11');
const text12 = document.getElementById('12');


card11.addEventListener("touchstart", function() {
    text12.classList.add('card-hover');
})