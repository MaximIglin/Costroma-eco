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


let cart = {};
let isCartCookie = false;

fetch("http://localhost:8000/api/products").then(
    response => response.json()).then(
        data => products = data).then(
            () => {
                if (isCartCookie == false) {
                    for (product of products) {
                        cart[product.id] = {
                            "quantity": 0,
                            "price": product.price
                        }
                        document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart) + "; path=/";
                    }
                }

            }
        )


document.addEventListener("DOMContentLoaded", () => {

    for (cookie of document.cookie.split("; ")) {
        if (cookie.indexOf("cart") != -1) {
            isCartCookie = true
            cart = JSON.parse(cookie.split("=")[1])
            document.querySelector(".final_price").innerHTML = cart["final_price"]
        }
    }
    setTimeout(() => {
        const addCartBtns = document.querySelectorAll(".add_button")
        const rmCartBtns = document.querySelectorAll(".remove_button")
        for (const addCartBtn of addCartBtns) {
            if (isCartCookie == false) {
                cart["final_price"] = 0
                document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart) + "; path=/";
                document.getElementById(`qty_${addCartBtn.id}`).innerHTML = 0
                document.querySelector(".final_price").innerHTML = cart["final_price"]
            } else {
                document.getElementById(`qty_${addCartBtn.id}`).innerHTML = Number(cart[addCartBtn.id]["quantity"])
                document.querySelector(".final_price").innerHTML = cart["final_price"]
            }
            addCartBtn.addEventListener("click", () => {
                cart[addCartBtn.id]["quantity"] += 1;
                document.getElementById(`qty_${addCartBtn.id}`).innerHTML = Number(cart[addCartBtn.id]["quantity"])
                cart["final_price"] += Number(cart[addCartBtn.id].price)
                document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart) + "; path=/";
                document.querySelector(".final_price").innerHTML = cart["final_price"]
            })
        }


        for (const rmCartBtn of rmCartBtns) {
            rmCartBtn.addEventListener("click", () => {
                if (cart[rmCartBtn.id]["quantity"] != 0) {
                    cart[rmCartBtn.id]["quantity"] = cart[rmCartBtn.id]["quantity"] - 1;
                    document.getElementById(`qty_${rmCartBtn.id}`).innerHTML = Number(cart[rmCartBtn.id]["quantity"])
                    cart["final_price"] = cart["final_price"] - Number(cart[rmCartBtn.id].price)
                    document.cookie = encodeURIComponent("cart") + '=' + JSON.stringify(cart) + "; path=/";
                    document.querySelector(".final_price").innerHTML = cart["final_price"]
                }
            })

        }
    }, 1500)
})



