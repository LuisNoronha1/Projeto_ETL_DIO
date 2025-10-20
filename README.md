🧠 Consultor de Carreira Personalizado com IA

Este projeto em Python demonstra uma aplicação prática de Inteligência Artificial Generativa (OpenAI API) para criar mensagens de aconselhamento de carreira personalizadas para alunos de tecnologia. O script automatiza a criação de consultorias, utilizando dados estruturados de uma planilha para interagir com o modelo GPT-3.5-Turbo.

🎯 Objetivo

O objetivo principal é escalar a consultoria de carreira, gerando mensagens profissionais e individualizadas para estudantes com base em seu perfil (curso, habilidades, experiência e área de interesse). O resultado é uma nova coluna na planilha contendo o feedback do consultor de IA.

⚙️ Tecnologias e Bibliotecas

Python: Linguagem de desenvolvimento.

Pandas: Usado para importar (alunos.csv), manipular e salvar os dados da planilha.

OpenAI: Biblioteca oficial para interagir com o modelo GPT-3.5-Turbo para geração de texto.

Time, Sys, Os: Utilizados para controle de fluxo, configuração de encoding (UTF-8) e gerenciamento de variáveis de ambiente.

💻 Funcionalidades

Importação de Dados: Lê o arquivo alunos.csv e organiza as informações de cada aluno.

Consulta de Perfil: Implementa uma função de filtro para buscar dados de alunos pelo nome (opcional).

Geração de Mensagem (IA):

O modelo de IA é configurado com a persona de um "consultor para alunos de tecnologia".

É fornecido um prompt detalhado, incluindo nome, curso, habilidade, experiência e área de interesse, para gerar um conselho de carreira focado.

Automação de Geração: Utiliza df.apply() para iterar sobre todos os alunos da planilha e gerar uma mensagem de IA para cada um.

Persistência de Dados: Adiciona as mensagens geradas na nova coluna mensagens e salva a planilha atualizada em alunos.csv.

⚠️ Pré-requisitos e Configuração

Para executar este projeto, você precisará configurar sua chave de API da OpenAI.

1. Instalar Dependências

pip install pandas openai


2. Configurar a Chave de API

O script espera que sua chave de API da OpenAI seja definida como uma variável de ambiente chamada OPENAI_API_KEY.

No Linux/macOS:

export OPENAI_API_KEY="SUA_CHAVE_AQUI"


No Windows (Prompt de Comando):

set OPENAI_API_KEY="SUA_CHAVE_AQUI"


3. Estrutura de Arquivos

Você deve ter o arquivo de dados alunos.csv na raiz do projeto, com as colunas esperadas (nome, curso, habilidade, experiencia, area, etc.).

.
├── alunos.csv                # Planilha de entrada/saída
├── [SEU_ARQUIVO].py          # O script principal de IA
└── README.md


🚀 Como Executar

Após configurar o ambiente e a chave de API, execute o script:

python [NOME_DO_SEU_ARQUIVO].py


O script imprimirá as mensagens geradas e, em seguida, o DataFrame completo e atualizado no console. Por fim, o arquivo alunos.csv será salvo com a nova coluna mensagens.
