const date = new Date();

let todosEventos = () => {
  let eventos = JSON.parse(document.getElementById("eventos").innerText)

  for (let i = 0; i < eventos.length; i++) {
    let evento = eventos[i];

    let dataEvento = evento.data;

    dataEvento = new Date(`${dataEvento} 00:00`);
    evento.data = dataEvento
  }

  return eventos;
};

let gerarMes = (anoInteiro, mes) => {
  let eventos = todosEventos()

  let inicioMes = new Date(anoInteiro, mes);
  let fimMes = new Date(anoInteiro, mes + 1, 0);

  let diasDoMes = [];

  // cria os dias do mês atual
  for (i = inicioMes.getDate(); i <= fimMes.getDate(); i++) {
    let dia = new Date(anoInteiro, mes, i);
    let diaObjeto = { dia: dia, evento: null };
    diasDoMes.push(diaObjeto);
  }

  // cria os dias do próximo mês que aparecem no mês atual
  if (fimMes.getDay() != 6) {
    for (i = fimMes.getDate() + 1; i <= 100; i++) {
      let dia = new Date(anoInteiro, mes, i);
      let diaObjeto = { dia: dia, evento: null };
      diasDoMes.push(diaObjeto);
      if (dia.getDay() >= 6) {
        break;
      }
    }
  }

  // cria os dias do mês passado que aparecem no mês atual
  if (inicioMes.getDay() != 0) {
    for (i = inicioMes.getDate() - 1; i >= -100; i--) {
      let dia = new Date(anoInteiro, mes, i);
      let diaObjeto = { dia: dia, evento: null };
      diasDoMes.splice(0, 0, diaObjeto);
      if (dia.getDay() <= 0) {
        break;
      }
    }
  }

  // adiciona os eventos nos dias dos meses
  for (i = 0; i < diasDoMes.length; i++) {
    let dia = diasDoMes[i];
    for (j = 0; j < eventos.length; j++) {
      let evento = eventos[j];
      if (evento.data.getDate() == dia.dia.getDate() && evento.data.getMonth() == dia.dia.getMonth() && evento.data.getFullYear() == dia.dia.getFullYear()) {
        dia.evento = evento;
      }
    }
  }

  return diasDoMes;
};

let renderCalendar = () => {
  const paginaReservas = "location.href='/reservas/adicionar'"
  
  const meses = [
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
  ];

  document.querySelector(".date h1").innerHTML =
    meses[date.getMonth()] + " " + date.getFullYear();
  let diasMes = gerarMes(date.getFullYear(), date.getMonth());
  let monthDays = document.querySelector(".days");
  let days = " ";
  let dataHoje = new Date()

  for (i = 0; i <= diasMes.length - 1; i++) {
    let dia = diasMes[i].dia;
    if (diasMes[i].evento == null) {
      if (dia.getMonth() < date.getMonth()) {
        days += `<div class="prev-date">${dia.getDate()}</div>`;
      } else if (dia.getMonth() > date.getMonth()) {
        days += `<div class="next-date">${dia.getDate()}</div>`;
      } else {
        if (
          dia.getDate() == dataHoje.getDate() &&
          dia.getFullYear() == dataHoje.getFullYear() &&
          dia.getMonth() == dataHoje.getMonth()
        ) {
          days += `<div class="hoje" onclick="${paginaReservas}">${dia.getDate()}</div>`;
        } else {
          days += `<div class="normal" onclick="${paginaReservas}">${dia.getDate()}</div>`;
        }
      }
    } else if (diasMes[i].evento.tipo_evento == "reserva") {
      if (
        dia.getDate() == dataHoje.getDate() &&
        dia.getFullYear() == dataHoje.getFullYear() &&
        dia.getMonth() == dataHoje.getMonth()
      ) {
        days += `<div class="hoje reserva" onclick="${paginaReservas}">${dia.getDate()}</div>`;
      } else {
        days += `<div class="normal reserva" onclick="${paginaReservas}">${dia.getDate()}</div>`;
      }
    } else if (diasMes[i].evento.tipo_evento == "reuniao") {
      if (
        dia.getDate() == dataHoje.getDate() &&
        dia.getFullYear() == dataHoje.getFullYear() &&
        dia.getMonth() == dataHoje.getMonth()
      ) {
        days += `<div class="hoje reuniao" onclick="${paginaReservas}">${dia.getDate()}</div>`;
      } else {
        days += `<div class="normal reuniao" onclick="${paginaReservas}">${dia.getDate()}</div>`;
      }
    }
  }

  monthDays.innerHTML = days;
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
