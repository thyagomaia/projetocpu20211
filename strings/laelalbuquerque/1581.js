var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var testes = parseInt(lines.shift());
var idioma, atual = ''
var ingles = false

while (testes--) {
    var pessoas = parseInt(lines.shift());
    idioma = lines.shift().substr(0,19).toLowerCase();
    atual = idioma
    pessoas--
    while (pessoas--) {
        if ((idioma !== atual) && ingles === false){
            ingles = true;

        } else {
            atual = idioma
        }
        idioma = lines.shift().substr(0,19).toLowerCase();
        
    }
    if (ingles){
        console.log("ingles");
    }else {
        console.log(atual);
    }
    ingles = false;
}