const openHistoryButton = document.getElementById("open-history-button");
const closeHistory = document.getElementById("close-history");
const historySobreposition = document.querySelector(".history-sobreposition");
const historyMenu = document.getElementById("history-menu");
const historyList = document.getElementById("items-container");

function renderCepHistory() {
  if (!historyList) return;
  
  const cepList = getCep().reverse();

  if (cepList.length === 0) {
    historyList.innerHTML = '<label class="empty-history">Nada aqui :(</label>';
    return;
  }
  
  historyList.innerHTML = cepList.map(itemCep => `
    <div class="history-item">
      <span class="cep-text" data-cep="${itemCep}">${itemCep}</span>
      <button class="history-trash-button" data-cep="${itemCep}">
        <svg class="trash-icon" data-action="delete">
          <use href="../static/icons/history.svg#icon-trash"></use>
        </svg>
      </button>
    </div>
  `).join('');
}

function addHistoryItem(CEP) {
  const cepInput = document.getElementById("CEP");
  if (cepInput) cepInput.value = CEP;
  
  if (!CEP || CEP.length < 8) {
    return;
  }
  if (historySobreposition) historySobreposition.classList.add("hidden");
  rst_CEP(CEP);
}

function deleteCepFromHistory(cep) {
  removeCep(cep);
  renderCepHistory();
}

function addNewCep(cep){
  console.log('Adicionando novo CEP:', cep);
  setCep(cep);
  renderCepHistory();
}


document.addEventListener('DOMContentLoaded', () => {
  renderCepHistory();

  if (openHistoryButton) {
    openHistoryButton.addEventListener("click", () => {
      historySobreposition.classList.remove("hidden");
    });
  }

  if (closeHistory) {
    closeHistory.addEventListener("click", () => {
      historySobreposition.classList.add("hidden");
    });
  }
});
