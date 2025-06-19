# ai_agents


## Config Enviroment
echo "Criando o ambiente virtual '.venv' com 'python -m venv .venv'"
python -m venv .venv

echo "Ativando o ambiente virtual com '.\.venv\Scripts\Activate.ps1'"
.\.venv\Scripts\Activate.ps1

echo "Listando as bibliotecas padrões inicias com 'pip list'"
pip list

echo "Listando as bibliotecas que serão instaladas com 'cat requirements.txt'"
cat requirements.txt

echo "Instalando as bibliotecas do projeto com 'pip install -r requirements.txt'"
pip install -r requirements.txt

echo "Listando as bibliotecas após a instalação com 'pip list'"
pip list