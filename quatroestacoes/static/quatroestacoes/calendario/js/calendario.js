const date = new Date();

let todasReservas = () => {
  let reservasBruto = JSON.parse(document.getElementById("reservas").innerText);
  let moradores = JSON.parse(document.getElementById("moradores").innerText);

  let reservas = [];

  for (let i = 0; i < reservasBruto.length; i++) {
    let reserva = reservasBruto[i];

    let dataReserva = reserva.data;
    let moradorIdReserva = reserva.morador_id;

    let ano = dataReserva.slice(0, 4);
    let mes = dataReserva.slice(5, 7);
    let dia = dataReserva.slice(8, 10);

    dataReserva = new Date(ano, mes - 1, dia);

    reserva = { data: dataReserva, morador_id: moradorIdReserva };
    reservas.push(reserva);
  }

  for (let i = 0; i < moradores.length; i++) {
    let morador = moradores[i];

    let nome = morador.first_name;
    let sobrenome = morador.last_name;
    let morador_id = morador.id;

    for (j = 0; j < reservas.length; j++) {
      let reserva = reservas[j];
      if (reserva.morador_id == morador_id) {
        reserva.nome = nome;
        reserva.sobrenome = sobrenome;
      }
    }
  }

  return reservas;
};

let gerarMes = (anoInteiro, mes) => {
  let reservas = todasReservas();

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

  // adiciona as reservas nos dias dos meses
  for (i = 0; i < diasDoMes.length; i++) {
    let dia = diasDoMes[i];
    for (j = 0; j < reservas.length; j++) {
      let reserva = reservas[j];
      if (reserva.data.getTime() == dia.dia.getTime()) {
        dia.evento = reserva;
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
          days += `<div class="today" onclick="${paginaReservas}">${dia.getDate()}</div>`;
        } else {
          days += `<div class="" onclick="${paginaReservas}">${dia.getDate()}</div>`;
        }
      }
    } else {
      days += `<div class="reserva">${dia.getDate()}</div>`;
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
