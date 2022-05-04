function preencherInterfone() {
    bloco = document.getElementById("id_bloco")
    apartamento = document.getElementById("id_apartamento")

    bloco = bloco.options[bloco.selectedIndex].text
    apartamento = apartamento.options[apartamento.selectedIndex].text

    primeiroDigitoInterfone = 0

    if (bloco == 'A') {
        primeiroDigitoInterfone = 1
    } else if (bloco == 'B') {
        primeiroDigitoInterfone = 2
    } else if (bloco == 'C') {
        primeiroDigitoInterfone = 3
    } else {
        primeiroDigitoInterfone = 4
    }

    interfone = String(primeiroDigitoInterfone) + apartamento

    campoInterfone = document.getElementById("id_interfone")
    campoInterfone.value = interfone
}


bloco = document.getElementById("id_bloco")
apartamento = document.getElementById("id_apartamento")

bloco.onchange = preencherInterfone
apartamento.onchange = preencherInterfone