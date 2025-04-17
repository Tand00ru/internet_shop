document.addEventListener('DOMContentLoaded', function() {
    const tableContainers = document.querySelectorAll('.table-container');

    function showTable(tableId) {
        tableContainers.forEach(container => {
            container.style.display = 'none';
        });
        document.getElementById(`${tableId}-table`).style.display = 'block';
    }

    // Показать таблицу пользователей по умолчанию
    showTable('users');
});
