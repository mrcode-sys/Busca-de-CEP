function getCep() {
  return JSON.parse(localStorage.getItem("CEPList")) || [];
}

function removeCep(Cep) {
  const currentCeps = getCep();
  const index = currentCeps.indexOf(Cep);
  if (index > -1) {
    currentCeps.splice(index, 1);
  }
  localStorage.setItem("CEPList", JSON.stringify(currentCeps));
}

function setCep(newCep) {
  if (!newCep || newCep.length < 8) {
    return;
  }
  removeCep(newCep);
  const currentCeps = getCep();
  currentCeps.push(newCep);
  localStorage.setItem("CEPList", JSON.stringify(currentCeps));
}

function clearCep() {
  localStorage.removeItem("CEPList");
}


document.addEventListener('DOMContentLoaded', () => {
  const clearButton = document.getElementById("clear-all-button");
  const itemsContainer = document.getElementById("items-container");

  if (clearButton) {
    clearButton.addEventListener("click", () => {
      clearCep();
      renderCepHistory();
    });
  }

  if (itemsContainer) {
    itemsContainer.addEventListener('click', (event) => {
      const button = event.target.closest('.history-item');
      if (!button) return;

      const trashButton = event.target.closest('.history-trash-button');
      const cepElement = button.querySelector('[data-cep]');
      if (!cepElement) return;

      const cep = cepElement.dataset.cep;

      if (trashButton) {
        event.stopPropagation();
        deleteCepFromHistory(cep);
        return;
      }
      
      addHistoryItem(cep);
    });
  }
});
