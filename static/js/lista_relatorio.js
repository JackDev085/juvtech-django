document.addEventListener('DOMContentLoaded', function () {
  const reportCard = document.querySelector('.card-relatorio');
  const downloadLink = document.getElementById('download-link');
  const buttonCopy = document.getElementById('button_copy');


  buttonCopy.addEventListener('click', function () {
    const reportUrl = reportCard.getAttribute('data-report-url');
    if (reportUrl) {
      navigator.clipboard.writeText(reportUrl)
        .then(() => {
          alert('Link copiado para a área de transferência!');
        })
        .catch((error) => {
          console.error('Erro ao copiar o link:', error);
        });
    } else {
      alert('URL do relatório não disponível.');
    }
  });


  reportCard.addEventListener('click', function () {
    const reportUrl = this.getAttribute('data-report-url');
    if (reportUrl) {
      downloadLink.href = reportUrl;
      downloadLink.click();
    } else {
      alert('URL do relatório não disponível.');
    }
  });
});

