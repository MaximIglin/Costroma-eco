document.addEventListener("DOMContentLoaded", () => {

    const cartLink = document.querySelector('.cart');
    const detailCart = document.querySelector('.detail_cart')
    const cartContent = document.querySelector('.cart__content')

      cartLink.addEventListener("click", () => {
        cartOpen(detailCart);
        fetch("http://localhost:8000/api/cart_detail")
        .then((response) => response.json())
        .then((data) => (products = data))
        .then(() => {
            products.forEach((product) => {
                cartContent.innerHTML += `<h1>${product.name}</h1>`
            })
        })
      });

      function cartOpen(detailCart) {
        bodyLock();
        detailCart.classList.add("open");
        detailCart.addEventListener("click", function (e) {
          if (!e.target.closest("cart__content")) {
            console.log(!e.target.closest("cart__content"));
            cartClose(e.target.closest(".detail_cart"));
            cartContent.innerHTML = ''
          }
        });
      }
      function cartClose(detailCart) {
        detailCart.classList.remove("open");
        bodyUnlock();
      }

      function bodyLock() {
        const lockPaddingValue = window.innerWidth - document.querySelector(".main_shop").offsetWidth + "px";

        if (lockPadding.length > 0) {
          for (let index = 0; index < lockPadding.length; index++) {
            const el = lockPadding[index];
            el.style.paddingRight = lockPaddingValue;
          }
        }
        body.style.paddingRight = lockPaddingValue;
        body.classList.add("lock");

        unlock = false;
        setTimeout(() => {
          unlock = true;
        }, timeout);
      }

      function bodyUnlock() {
        setTimeout(() => {
          for (let index = 0; index < lockPadding.length; index++) {
            const el = lockPadding[index];
            el.style.paddingRight = "0px";
          }
          body.style.paddingRight = "0px";
          body.classList.remove("lock");
        }, timeout);

        unlock = false;
        setTimeout(() => {
          unlock = true;
        }, timeout);
      }
    
});
