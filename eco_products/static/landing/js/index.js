const sliderTrack = document.querySelector('.slider_track')
const slidesCount = sliderTrack.querySelectorAll('.slider_item').length
const header = document.querySelector('.header')
const categories = document.querySelector('.categories')

let activeSlideIndex = 0;
let positionHeader = header.getBoundingClientRect().top;
let positionCategories = categories.getBoundingClientRect().top;


function changeSlide() {
    sliderTrack.style.transform = `translateX(-${activeSlideIndex * 100}vw)`
    activeSlideIndex++
    if(activeSlideIndex === slidesCount) 
    {
        activeSlideIndex = 0;
    }
}

setInterval(changeSlide, 2500)

// let windowVerticalScroll = window.scrollY

// function hideHeader() {
//     let windowVerticalScroll = window.scrollY
//     if(0 >=categories.offsetTop - header.scrollTop - 1){
//         header.classList.add('hide')
//     } else {
//         header.classList.remove('hide')
//     }
// }

// hideHeader()