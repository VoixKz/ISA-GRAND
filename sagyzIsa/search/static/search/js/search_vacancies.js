document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const specialtySelect = document.getElementById('specialtySelect');
    const vacancyGrid = document.getElementById('vacancyGrid');
    const vacancies = vacancyGrid.getElementsByClassName('vacancy_item');
    const sortDateButton = document.getElementById('sortDate');
    const sortSalaryButton = document.getElementById('sortSalary');

    let sortDateState = 0; // 0: no sort, 1: asc, 2: desc
    let sortSalaryState = 0; // 0: no sort, 1: asc, 2: desc

    function filterVacancies() {
        const filter = searchInput.value.toLowerCase();
        const selectedSpecialty = specialtySelect.value.toLowerCase();

        Array.from(vacancies).forEach(vacancy => {
            const title = vacancy.querySelector('.vacancy-title').textContent.toLowerCase();
            const specialty = vacancy.querySelector('.vacancy-area').textContent.toLowerCase();

            const matchesFilter = title.includes(filter);
            const matchesSpecialty = !selectedSpecialty || specialty === selectedSpecialty;

            if (matchesFilter && matchesSpecialty) {
                vacancy.style.display = '';
            } else {
                vacancy.style.display = 'none';
            }
        });
    }

    function sortVacancies(order, type) {
        const sortedVacancies = Array.from(vacancies).sort((a, b) => {
            let valueA, valueB;
            if (type === 'date') {
                valueA = new Date(a.querySelector('.vacancy-date').textContent);
                valueB = new Date(b.querySelector('.vacancy-date').textContent);
            } else if (type === 'salary') {
                valueA = parseFloat(a.querySelector('.vacancy-salary').textContent);
                valueB = parseFloat(b.querySelector('.vacancy-salary').textContent);
            }

            if (order === 'asc') {
                return valueA - valueB;
            } else if (order === 'desc') {
                return valueB - valueA;
            }
        });

        sortedVacancies.forEach(vacancy => vacancyGrid.appendChild(vacancy));
    }

    function updateSortButton(button, state) {
        if (state === 0) {
            button.textContent = button.textContent.replace(/↑|↓/g, '↕');
        } else if (state === 1) {
            button.textContent = button.textContent.replace(/↕|↓/g, '↑');
        } else if (state === 2) {
            button.textContent = button.textContent.replace(/↕|↑/g, '↓');
        }
    }

    sortDateButton.addEventListener('click', () => {
        sortDateState = (sortDateState + 1) % 3;
        sortSalaryState = 0; // Reset salary sort state
        updateSortButton(sortDateButton, sortDateState);
        updateSortButton(sortSalaryButton, sortSalaryState);

        if (sortDateState === 1) {
            sortVacancies('asc', 'date');
        } else if (sortDateState === 2) {
            sortVacancies('desc', 'date');
        } else {
            filterVacancies(); // Reset to no sort
        }
    });

    sortSalaryButton.addEventListener('click', () => {
        sortSalaryState = (sortSalaryState + 1) % 3;
        sortDateState = 0; // Reset date sort state
        updateSortButton(sortSalaryButton, sortSalaryState);
        updateSortButton(sortDateButton, sortDateState);

        if (sortSalaryState === 1) {
            sortVacancies('asc', 'salary');
        } else if (sortSalaryState === 2) {
            sortVacancies('desc', 'salary');
        } else {
            filterVacancies(); // Reset to no sort
        }
    });

    searchInput.addEventListener('input', filterVacancies);
    specialtySelect.addEventListener('change', filterVacancies);
});