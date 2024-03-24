
document.addEventListener("DOMContentLoaded", function() {
    const filterButtons = document.querySelectorAll('.filters-menu li');
    const items = document.querySelectorAll('.grid .box');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filterValue = button.getAttribute('data-filter').substring(1); 
            items.forEach(item => {
                if (filterValue === item.classList.contains(filterValue)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
});
