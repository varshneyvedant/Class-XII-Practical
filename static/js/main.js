document.addEventListener('DOMContentLoaded', function() {
    // This function makes rows in a table with the class 'clickable-row' clickable.
    // It's a simple way to improve user experience.
    // It demonstrates basic JavaScript event handling.
    const rows = document.querySelectorAll('.clickable-row');
    rows.forEach(row => {
        row.addEventListener('click', (e) => {
            // This check ensures that if you click on a link within the row,
            // it doesn't trigger the row's click event as well.
            if (e.target.tagName !== 'A') {
                window.location.href = row.dataset.href;
            }
        });
    });
});
