//Dogadkin: category menu animation
const categories = document.querySelectorAll('.category_button')

const slides = document.querySelectorAll('.slide')



for (const category_button of categories) {
    category_button.addEventListener('mouseover', () => {
        category_button.classList.add('active_categoty')
    })

    category_button.addEventListener('mouseout', () => {
        category_button.classList.remove('active_categoty')
    })

}



//Dogadkin: popup
const popupLinks = document.querySelectorAll('.popup-link')
const body = document.querySelector('body')
const lockPadding = document.querySelectorAll('.lock-padding')

let unlock = true

const timeout = 800

if (popupLinks.length > 0) {
    for (let index = 0; index < popupLinks.length; index++) {
        const popupLink = popupLinks[index]
        popupLink.addEventListener("click", function (e) {
            const popupName = popupLink.getAttribute('href').replace('#','')
            const currentPopup = document.getElementById(popupName)
            popupOpen(currentPopup)
            e.preventDefault()
        })
    }
}
const popupCloseIcon = document.querySelectorAll('.close-popup')
if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++) {
        const el = popupCloseIcon[index]
        el.addEventListener("click", function (e) {
            popupClose(el.closest('.popup'))
            e.preventDefault()
        })
    }
}

function popupOpen(currentPopup) {
    if (currentPopup && unlock){
        const popupActive = document.querySelector('.popup.open')
        if (popupActive) {
            popupClose(popupActive, false)
        } else {
            bodyLock();
        }
        currentPopup.classList.add('open')
        currentPopup.addEventListener('click', function (e) {
            if (!e.target.closest('popup__content')) {
                popupClose(e.target.closest('.popup'))
            }
        })
    }
}
function popupClose (popupActive, doUnlock = true) {
    if (unlock) {
        popupActive .classList.remove('open')
        if(doUnlock) {
            bodyUnlock();
        }
    }
}

function bodyLock() {
    const lockPaddingValue = window.innerWidth - document.querySelector('.main_shop').offsetWidth + 'px'

    if(lockPadding.length > 0) {
        for (let index = 0; index < lockPadding.length; index++) {
            const el = lockPadding[index]
            el.style.paddingRight = lockPaddingValue
        }
    }
    body.style.paddingRight = lockPaddingValue
    body.classList.add('lock')

    unlock = false
    setTimeout(() =>{
        unlock = true
    }, timeout)     
}

function bodyUnlock() {
    setTimeout(() => {
        for (let index = 0; index < lockPadding.length; index++) {
            const el = lockPadding[index]
            el.style.paddingRight = '0px'
        }
        body.style.paddingRight = '0px'
        body.classList.remove('lock')
    }, timeout)

    unlock = false
    setTimeout(() =>{
        unlock = true
    }, timeout)    
}



//Iglin: counter
const qtt = document.querySelectorAll('.qtt')
let cart = {
}

fetch("http://localhost:8000/api/products").then(response => {
    return response.json()
}).then((data)=>{
    return products = (data)
});


document.addEventListener("DOMContentLoaded", () => {
    const addCartBtns = document.querySelectorAll(".add_button")
    const rmCartBtns = document.querySelectorAll(".remove_button")


    for (const addCartBtn of addCartBtns) {
        cart[addCartBtn.id] = {
            quantity: 0,
            price:500
        }
        addCartBtn.addEventListener("click", () => {
            cart[addCartBtn.id]["quantity"] += 1;
            document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart)
            qtt[addCartBtn.id].innerHTML = cart[addCartBtn.id]["quantity"]
            console.log(qtt[addCartBtn.id])
        })
    }


    for (const rmCartBtn of rmCartBtns) {
        rmCartBtn.addEventListener("click", () => {
            cart[rmCartBtn.id]["quantity"] = cart[rmCartBtn.id]["quantity"] - 1;
            document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart)
            qtt[rmCartBtn.id].innerHTML = cart[rmCartBtn.id]["quantity"]
            console.log(qtt[rmCartBtn.id])
        })

    }

})



