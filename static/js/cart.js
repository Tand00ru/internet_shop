document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".cart_quantity").forEach(function (cart) {
        const minusButton = cart.querySelector(".minus");
        const plusButton = cart.querySelector(".plus");
        const inputField = cart.querySelector(".quantity_add_to_cart");

        function updateValue(change) {
            let currentValue = parseInt(inputField.value) || 1; // Если пусто, ставим 1
            let newValue = currentValue + change;

            // Ограничиваем в диапазоне от 1 до 100
            if (newValue >= 1 && newValue <= 100) {
                inputField.value = newValue;
            }
        }

        // Обработчики кнопок
        plusButton.addEventListener("click", function () {
            updateValue(1);
        });

        minusButton.addEventListener("click", function () {
            updateValue(-1);
        });

        // Ограничение ввода только числами и проверка на max
        inputField.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, ""); // Убираем буквы
            let value = parseInt(this.value);

            // Если введено меньше 1 — ставим 1
            if (isNaN(value) || value < 1) {
                this.value = 1;
            }
            // Если введено больше 100 — ставим 100
            else if (value > 100) {
                this.value = 100;
            }
        });
    });
});
