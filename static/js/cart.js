document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".cart_quantity").forEach(function (cart) {
        const minusButton = cart.querySelector(".minus");
        const plusButton = cart.querySelector(".plus");
        const inputField = cart.querySelector(".quantity_add_to_cart");

        function updateValue(change) {
            let currentValue = parseInt(inputField.value) || 1;
            let newValue = currentValue + change;

            if (newValue >= 1 && newValue <= 100) {
                inputField.value = newValue;
            }
        }

        plusButton.addEventListener("click", function () {
            updateValue(1);
        });

        minusButton.addEventListener("click", function () {
            updateValue(-1);
        });

        inputField.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "");
            let value = parseInt(this.value);

            if (isNaN(value) || value < 1) {
                this.value = 1;
            }
            else if (value > 100) {
                this.value = 100;
            }
        });
    });
});
