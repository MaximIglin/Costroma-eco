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
        })
    }


    for (const rmCartBtn of rmCartBtns) {
        rmCartBtn.addEventListener("click", () => {
            cart[rmCartBtn.id]["quantity"] = cart[rmCartBtn.id]["quantity"] - 1;
            document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart)
        })

    }

})




