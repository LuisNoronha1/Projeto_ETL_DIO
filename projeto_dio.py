import pandas as pd
import openai
import time
import sys

# Configure stdout para usar UTF-8
sys.stdout.reconfigure(encoding='utf-8')

##Organizar as informaçoes importadas da planilha##

df = pd.read_csv('alunos.csv', encoding='utf-8')

curso = df['curso'].tolist()

nome = df['nome'].tolist()

matricula = df['numero de matricula'].tolist()

faculdade = df['faculdade'].tolist()

semestre = df['semestre'].tolist()

habilidade = df['habilidade'].tolist()

experiencia = df['experiencia'].tolist()

area = df['area'].tolist()


##Filtrar caso nao encontre nenhum ID de usuario.##
def get_user_nome(nome):
    
    user_data = df[df['nome'] == nome]
    
    if not user_data.empty:
        return user_data.iloc[0].to_dict()

    else:
        print(f"Aluno {nome} não encontrado.")
        return None

##confeccionando a IA##

openai_api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = openai_api_key


def generate_ai_news(name, curse, habilit, experince, aria):
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {   'role': 'system', 
            'content': 'Voce e um consultor para alunos de tecnologia, no qual ajudara-los a arurmar emprego.'},
        {   'role': 'user', 
            'content': f'crie uma mensagem para {name} sobre a importancia de arrumar um emprego, e da melhor maneira de consegui-lo na area em que eles desejam {aria}'
                       f'O curso que ele faz é {curse} e sua habilidade é {habilit} e sua experiencia em trabalho é {experince}. A mensagem deve' 
                       f'ser profissional como um consultor e ter ate 100 caracteres.'}
    ]
)
    return  completion.choices[0].message.content.strip()
    
    
for i in range(len(df)):
    name = df['nome'][i]
    curso = df['curso'][i]
    habilidade = df['habilidade'][i]
    experiencia = df['experiencia'][i]
    area = df['area'][i]
    
    news = generate_ai_news(name, curso, habilidade, experiencia, area)
    print(f"Mensagem para {name}: {news}")
    time.sleep(5)
    
    
##gerar mensagens e adiciona-las a lista de alunos##

df['mensagens'] = df.apply(lambda row: generate_ai_news(row['curso'], row['nome'], row['habilidade'], row['experiencia'], row ['area']), axis=1)

##salvar a planilha atualizada##
df.to_csv('alunos.csv', index=False, encoding='utf-8')

print('Mensagens geradas e adicionadas a planilha com sucesso.')
 
##Apresentar toda a tabela##
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df.to_string(index=False))                          