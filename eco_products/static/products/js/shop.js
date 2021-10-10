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
