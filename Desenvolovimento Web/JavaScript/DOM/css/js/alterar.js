function alterar(){
    let objpainel = document.getElementById("painel");
    let objcampo_1 = document.getElementById("campo_1");
    let objcampo_2 = document.getElementById("campo_2");

    objpainel.style.left = `${objcampo_1.value}px`;
    objpainel.style.top = `${objcampo_2.value}px`;
    objpainel.innerHTML = `(${objcampo_1.value}, ${objcampo_2.value})`
}