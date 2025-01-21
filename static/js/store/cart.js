    // JavaScript to dynamically update quantities and totals
    document.addEventListener('DOMContentLoaded', () => {
        const cartContainer = document.querySelector('.cart-container');

        cartContainer.addEventListener('click', (e) => {
            const target = e.target;
            const cartItem = target.closest('.cart-item');
            if (!cartItem) return;

            const quantityInput = cartItem.querySelector('.quantity-input');
            const price = parseFloat(cartItem.querySelector('.item-price').textContent.replace('Price: $', ''));
            let quantity = parseInt(quantityInput.value, 10);

            if (target.classList.contains('increase')) {
                quantity += 1;
            } else if (target.classList.contains('decrease') && quantity > 1) {
                quantity -= 1;
            } else if (target.classList.contains('remove-item')) {
                cartItem.remove();
            }

            quantityInput.value = quantity;

            updateTotals();
        });

        function updateTotals() {
            const cartItems = document.querySelectorAll('.cart-item');
            let subtotal = 0;

            cartItems.forEach((item) => {
                const quantity = parseInt(item.querySelector('.quantity-input').value, 10);
                const price = parseFloat(item.querySelector('.item-price').textContent.replace('Price: $', ''));
                subtotal += quantity * price;
            });

            document.querySelector('.subtotal-value').textContent = `$${subtotal.toFixed(2)}`;
            document.querySelector('.total-value').textContent = `$${subtotal.toFixed(2)}`;
        }
    });