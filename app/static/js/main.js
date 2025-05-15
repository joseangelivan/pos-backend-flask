document.addEventListener('DOMContentLoaded', function() {
    // Animación para las tarjetas de estadísticas
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = 'none';
        });
    });
    
    // Validación de formularios
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = this.querySelectorAll('input[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.classList.add('is-invalid');
                    isValid = false;
                } else {
                    input.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Por favor complete todos los campos requeridos.');
            }
        });
    });
});
