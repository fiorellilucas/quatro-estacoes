const date = new Date()

let todosEventos = () => {
  let eventos = JSON.parse(document.getElementById("eventos").innerText)

  for (let i = 0; i < eventos.length; i++) {
    let evento = eventos[i]

    let dataEvento = evento.data

    dataEvento = new Date(`${dataEvento} 00:00`)
    evento.data = dataEvento
  }

  return eventos
}

let gerarMes = (anoInteiro, mes) => {
  let eventos = todosEventos()

  let inicioMes = new Date(anoInteiro, mes)
  let fimMes = new Date(anoInteiro, mes + 1, 0)

  let diasDoMes = []

  // cria os dias do mês atual
  for (i = inicioMes.getDate(); i <= fimMes.getDate(); i++) {
    let dia = new Date(anoInteiro, mes, i)
    let diaObjeto = { dia: dia, evento: null }
    diasDoMes.push(diaObjeto)
  }

  // cria os dias do próximo mês que aparecem no mês atual
  if (fimMes.getDay() != 6) {
    for (i = fimMes.getDate() + 1; i <= 100; i++) {
      let dia = new Date(anoInteiro, mes, i)
      let diaObjeto = { dia: dia, evento: null }
      diasDoMes.push(diaObjeto)
      if (dia.getDay() >= 6) {
        break
      }
    }
  }

  // cria os dias do mês passado que aparecem no mês atual
  if (inicioMes.getDay() != 0) {
    for (i = inicioMes.getDate() - 1; i >= -100; i--) {
      let dia = new Date(anoInteiro, mes, i)
      let diaObjeto = { dia: dia, evento: null }
      diasDoMes.splice(0, 0, diaObjeto)
      if (dia.getDay() <= 0) {
        break
      }
    }
  }

  // adiciona os eventos nos dias dos meses
  for (i = 0; i < diasDoMes.length; i++) {
    let dia = diasDoMes[i]
    for (j = 0; j < eventos.length; j++) {
      let evento = eventos[j]
      if (
        evento.data.getDate() == dia.dia.getDate() &&
        evento.data.getMonth() == dia.dia.getMonth() &&
        evento.data.getFullYear() == dia.dia.getFullYear()
      ) {
        dia.evento = evento
      }
    }
  }

  return diasDoMes
}

let renderCalendar = () => {
  const PAGINA_RESERVAS = "location.href='/reservas/adicionar'"

  const MESES = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
  ]

  let diasDoMes = gerarMes(date.getFullYear(), date.getMonth())
  console.log(diasDoMes)
  
  document.querySelector(".mes").innerHTML = `${MESES[date.getMonth()]} ${date.getFullYear()}`

}

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1)
  renderCalendar()
})

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1)
  renderCalendar()
})

renderCalendar()
