# Brendinha Gold Tracker

![Brendinha Gold Tracker](resources/hello_kitty.png)

**Um tracker simples e fofo para gerenciar seu gold no Black Desert, com metas diárias e mensais.**  
Feito com PyQt6 + SQLite, focado em praticidade e visual limpo para acompanhar sua evolução de farm.

## Funcionalidades

✅ Cadastro diário de gold inicial e final.  
✅ Visualização do ganho diário, falta para meta diária e falta para meta mensal.  
✅ Estimativa de dias para alcançar meta mensal.  
✅ Exportação do histórico em CSV.  
✅ Gráfico de evolução de farm.  
✅ Configuração de metas diárias e mensais.  
✅ Tema claro (rosa) e escuro.  
✅ Formatação automática com pontos enquanto digita.  
✅ Banco de dados local em SQLite, sem necessidade de conexão com internet.

## Instalação

1️⃣ Clone o projeto:

```bash
git clone https://github.com/WalmirJunior/BGT.git
```
2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

4️⃣ Execute o projeto:
```bash
python main.py
```

## Estrutura do Projeto
```bash
BGT/
├── db/
│   └── gold_tracker.db (criado automaticamente)
├── resources/
│   └── hello_kitty.png
├── utils/
│   ├── csv_exporter.py
│   └── chart_generator.py
├── main.py
└── README.md

```

## Como Usar
1️⃣ Insira o Gold Inicial e Gold Final do dia e clique em Salvar Dia.

2️⃣ Visualize seu progresso na tabela, metas e estimativas de dias restantes.

3️⃣ Clique em Exportar CSV para salvar seus registros.

4️⃣ Clique em Ver Gráfico para visualizar seu progresso visualmente.

5️⃣ Use Configurar Metas para definir suas metas diárias e mensais.

6️⃣ Marque Modo escuro se preferir um visual dark.


## Contribuição

Se quiser sugerir melhorias, adicionar recursos ou corrigir bugs, abra uma Issue ou envie um Pull Request.

## Licença
MIT © Walmir Junior