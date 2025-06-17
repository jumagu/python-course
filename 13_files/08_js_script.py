js_code = """
document.body.onclick = function() {
    const colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'];
    const colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
    document.body.style.backgroundColor = colorAleatorio;
};

console.log('¡Haz clic en cualquier parte para cambiar el color!');
"""
with open("test_files/script.js", "w") as js_file:
    js_file.write(js_code)

with open("test_files/script.js", "r") as js_file:
    content = js_file.read()
    print(content)
