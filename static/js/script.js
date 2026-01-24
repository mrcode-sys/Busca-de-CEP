const input = document.getElementById("CEP")

function format_to_rstCEP(CEP) {
    return CEP.replace(/\D/g, '')
}

async function rst_CEP(event, CEP) {
    event.preventDefault();
    console.log(CEP)
    CEP = format_to_rstCEP(CEP)
    const url = '/api/cep/'+CEP

    console.log(url)
    let rst = ""
    try {
        const resp = await fetch(url)
        console.log(resp.status)
        if (!resp.ok){
            if (resp.status === 400) {
                console.log(CEP)
                input.setCustomValidity("CEP inválido")
                input.reportValidity()
                return
            }
            throw new Error("A resposta não está certa: "+resp.statusText)
            return
        }
        rst = await resp.json()
    } catch (err) {
        console.error('Ocorreu algum erro: '+err)
        alert("Ocorreu algum erro")
        return
    }

    console.log(rst)
    console.log(typeof rst.erro)
    const infs = ['localidade', 'regiao', 'bairro', 'complemento', 'logradouro', 'ibge', 'gia', 'ddd', 'siafi']

    for (const inf of infs) {
        if (inf == 'localidade'){
            document.querySelectorAll(`[data-inf="${inf}"]`).forEach(elmt => elmt.textContent = rst[inf]+", "+rst['uf'])
            continue;
        }
        console.log(inf)
        console.log(rst[inf])
        document.querySelectorAll(`[data-inf="${inf}"]`).forEach(elmt => elmt.textContent = rst[inf])
    }
}

function format(CEP) {
    console.log(CEP)
    let valor = CEP.replace(/\D/g, '')

    valor = valor.replace(/(\d{5})(\d)/, "$1-$2")

    document.getElementById('CEP').value = valor
}

document.getElementById("form1").addEventListener("submit", (event) => {
    rst_CEP(event, CEP.value)

})

input.addEventListener("input", (event) =>{
    format(event.target.value)
    input.setCustomValidity("")

})