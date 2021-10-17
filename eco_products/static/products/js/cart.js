document.addEventListener("DOMContentLoaded", () => {

  const cartLink = document.querySelector('.cart');
  const detailCart = document.querySelector('.detail_cart')
  const cartContent = document.querySelector('.cart__content')
  const lockPadding = document.querySelectorAll('.lock-padding')
  const body = document.querySelector('body')
  const lots = document.querySelector('.lots')
  const cartPrice = document.querySelector('.cart__price')
  const timeout = 800
  let unlock = true

  cartLink.addEventListener("click", () => {
    cartOpen(detailCart);
    fetch("http://localhost:8000/api/cart_detail")
      .then((response) => response.json())
      .then((data) => (products = data))
      .then(() => {
        let i = 0
        let final__qty = 0
        products["data"].forEach((product) => {
          final__qty += Number(products["qty"][i])
          lots.innerHTML += `<div class="cart_item">
                                <div class="cart_item_name">${product.name}</div>  
                                <div class="swing">
                                  <button class="remove_button buy_button">
                                      -
                                  </button>
                                  <div class="qtt">${products["qty"][i]}</div>
                                  <button class="add_button buy_button">
                                      +
                                  </button>
                                </div>
                                <div class="cart_item_final_price">${Number(product.price) * Number(products["qty"][i])} ₽</div>
                              </div>`
          i ++
        })
        cartPrice.innerHTML += `<div class="final__qty">Количество товаров: ${final__qty}</div>`
        cartPrice.innerHTML += `<div class="final__price">Стоимость продуктов: ${cart.final_price} ₽</div>`
        cartPrice.innerHTML += `<div class="order__btn">Оформить заказ</div>` 
        
        const orderBtn = document.querySelector('.order__btn')
        orderBtn.addEventListener('click', () => {
          lots.innerHTML = ''
          lots.innerHTML = `<form action="" method="post">
                              <label for="formName" class="form_label">Имя*</label>
                              <input type="text" name="name" id="">

                              <label for="formSurname" class="form_label">Фамилия*</label>
                              <input type="text" name="surname" id="">

                              <label for="formPhoneNumber" class="form_label">Номер телефона*</label>
                              <input type="number" name="phone_number" id="">

                              <label for="formAdress" class="form_label">Адрес*</label>
                              <input type="text" name="adress" id="">

                              <label for="formEmail" class="form_label">Email*</label>
                              <input type="email" name="email" id="">

                              <label for="formMessage" class="form_label">Сообщение</label>
                              <input type="text" name="message" id="">

                              <input type="submit" value="Отправить">
                            </form>`
        })

      })
  });

  function cartOpen(detailCart) {
    bodyLock();
    detailCart.classList.add("open");
    detailCart.addEventListener("click", function (e) {
      if (!e.target.closest(".cart__content")) {
        cartClose(e.target.closest(".detail_cart"));
        lots.innerHTML = ''
        cartPrice.innerHTML = ''
      }
    });
  }
  function cartClose(detailCart) {
    detailCart.classList.remove("open");
    bodyUnlock();
  }

  function bodyLock() {
    try {
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
    catch {
      const lockPaddingValue = window.innerWidth - document.querySelector(".main").offsetWidth + "px";
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
