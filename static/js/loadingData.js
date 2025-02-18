async function carregarDados(endpoint, tabelaId) {
    const response = await fetch(`http://localhost:8000/${endpoint}`);
    const dados = await response.json();
    
    let tabela = document.getElementById(tabelaId);
    let colunas = Object.keys(dados[0]);

    // Cabeçalho
    let thead = tabela.createTHead();
    let row = thead.insertRow();
    colunas.forEach(coluna => {
        let th = document.createElement("th");
        th.textContent = coluna;
        row.appendChild(th);
    });

    // Corpo da tabela
    let tbody = tabela.createTBody();
    dados.forEach(item => {
        let row = tbody.insertRow();
        colunas.forEach(coluna => {
            let cell = row.insertCell();
            cell.textContent = item[coluna];
        });
    });
}

carregarDados("clientes", "clientes-table");
carregarDados("pedidos", "pedidos-table");
