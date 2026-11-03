const input = document.getElementById("CEP")

function format_to_rstCEP(CEP) {
    return CEP.replace(/\D/g, '')
}

async function rst_CEP(CEP, event = null) {
    if (event) {
        event.preventDefault();
    }
    addNewCep(CEP)
    CEP = format_to_rstCEP(CEP)
    const url = '/api/cep/'+CEP

    let rst = ""
    let data = ""
    try {
        const resp = await fetch(url)
        if (!resp.ok){
            if (resp.status === 400) {
                input.setCustomValidity("CEP inválido")
                input.reportValidity()
                return
            }
            throw new Error('Resposta inválida: '+resp.statusText)
        }
        rst = await resp.json()
        data = rst['data']
        
    } catch (err) {
        console.error('Ocorreu algum erro: '+err)
        alert("Ocorreu algum erro")
        return
    }

    const infs = ['localidade', 'regiao', 'bairro', 'complemento', 'logradouro', 'ibge', 'gia', 'ddd', 'siafi']

    for (const inf of infs) {
        if (inf == 'localidade'){
            document.querySelectorAll(`[data-inf="${inf}"]`).forEach(elmt => elmt.textContent = data[inf]+", "+data['uf'])
            continue;
        }

        document.querySelectorAll(`[data-inf="${inf}"]`).forEach(elmt => elmt.textContent = data[inf])
    }
}

function format(CEP) {
    let value = CEP.value;

    let cursorPosition = CEP.selectionStart;
    const originalLength = value.length;

    let formatedValue = value.replace(/\D/g, '');
    console.log(formatedValue)
    if (formatedValue.length > 5) {
        formatedValue = formatedValue.replace(/(\d{5})(\d)/, "$1-$2");
    }

    CEP.value = formatedValue

    const lengthDifference = formatedValue.length - originalLength;
    let newPosition = cursorPosition + lengthDifference;

    if (newPosition === 6 && formatedValue.charAt(5) === '-') {
        if (lengthDifference < 0) newPosition = 5; 
    }

    CEP.setSelectionRange(newPosition, newPosition);
}

document.getElementById("form1").addEventListener("submit", (event) => {
    rst_CEP(CEP.value, event)

})

input.addEventListener("input", (event) =>{
    format(event.target)
    input.setCustomValidity("")

})