document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const areaSelect = document.getElementById('areaSelect');
    const courseGrid = document.getElementById('courseGrid');
    const courses = courseGrid.getElementsByClassName('course_item');
    const sortDurationButton = document.getElementById('sortDuration');
    const sortPriceButton = document.getElementById('sortPrice');

    let sortDurationState = 0; // 0: no sort, 1: asc, 2: desc
    let sortPriceState = 0; // 0: no sort, 1: asc, 2: desc

    function filterCourses() {
        const filter = searchInput.value.toLowerCase();
        const selectedArea = areaSelect.value.toLowerCase();

        Array.from(courses).forEach(course => {
            const title = course.querySelector('.course-title').textContent.toLowerCase();
            const area = course.querySelector('.course-area').textContent.toLowerCase();

            const matchesFilter = title.includes(filter);
            const matchesArea = !selectedArea || area === selectedArea;

            if (matchesFilter && matchesArea) {
                course.style.display = '';
            } else {
                course.style.display = 'none';
            }
        });
    }

    function sortCourses(order, type) {
        const sortedCourses = Array.from(courses).sort((a, b) => {
            let valueA, valueB;
            if (type === 'duration') {
                valueA = parseFloat(a.querySelector('.course-duration').textContent);
                valueB = parseFloat(b.querySelector('.course-duration').textContent);
            } else if (type === 'price') {
                valueA = parseFloat(a.querySelector('.course-price').textContent);
                valueB = parseFloat(b.querySelector('.course-price').textContent);
            }

            if (order === 'asc') {
                return valueA - valueB;
            } else if (order === 'desc') {
                return valueB - valueA;
            }
        });

        sortedCourses.forEach(course => courseGrid.appendChild(course));
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

    sortDurationButton.addEventListener('click', () => {
        sortDurationState = (sortDurationState + 1) % 3;
        sortPriceState = 0; // Reset price sort state
        updateSortButton(sortDurationButton, sortDurationState);
        updateSortButton(sortPriceButton, sortPriceState);

        if (sortDurationState === 1) {
            sortCourses('asc', 'duration');
        } else if (sortDurationState === 2) {
            sortCourses('desc', 'duration');
        } else {
            filterCourses(); // Reset to no sort
        }
    });

    sortPriceButton.addEventListener('click', () => {
        sortPriceState = (sortPriceState + 1) % 3;
        sortDurationState = 0; // Reset duration sort state
        updateSortButton(sortPriceButton, sortPriceState);
        updateSortButton(sortDurationButton, sortDurationState);

        if (sortPriceState === 1) {
            sortCourses('asc', 'price');
        } else if (sortPriceState === 2) {
            sortCourses('desc', 'price');
        } else {
            filterCourses(); // Reset to no sort
        }
    });

    searchInput.addEventListener('input', filterCourses);
    areaSelect.addEventListener('change', filterCourses);
});