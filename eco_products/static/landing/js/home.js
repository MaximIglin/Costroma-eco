const sliderTrack = document.querySelector('.slider_track')
const slidesCount = sliderTrack.querySelectorAll('.slider_item').length
const header = document.querySelector('.header')
const categories = document.querySelector('.categories')

let activeSlideIndex = 0;

function changeSlide() {
    sliderTrack.style.transform = `translateX(-${activeSlideIndex * 100}vw)`
    activeSlideIndex++
    if(activeSlideIndex === slidesCount) 
    {
        activeSlideIndex = 0;
    }
}

setInterval(changeSlide, 2500)

let isCartCookie = false
for (cookie of document.cookie.split("; ")) {
    if (cookie.indexOf("cart") != -1) {
        isCartCookie = true
        cart = JSON.parse(cookie.split("=")[1])
        document.querySelector(".final_price").innerHTML = cart["final_price"]
    }
}

if(isCartCookie == false){
    document.querySelector(".final_price").innerHTML = 0
}
