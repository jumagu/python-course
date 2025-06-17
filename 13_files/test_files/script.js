
document.body.onclick = function() {
    const colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'];
    const colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
    document.body.style.backgroundColor = colorAleatorio;
};

console.log('¡Haz clic en cualquier parte para cambiar el color!');
