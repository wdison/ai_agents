param(
    [string]$WorkingDirectory
)


# Recuperar a pasta que está esse script para poder subir um nível entrar no mcp_server, fazer a execução e depois ficar na pasta pai da pasta desse script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
echo ""
echo "Pasta do script: $scriptPath"

# Subir um nível para a pasta pai
$parentPath = Split-Path -Parent $scriptPath
echo ""
echo "Pasta pai: $parentPath"

# Entrar na pasta pai
echo ""
echo "Entrando na pasta pai com 'cd $parentPath'"
cd $parentPath


echo ""
echo "Entrando na pasta de trabalho: $WorkingDirectory com 'cd $WorkingDirectory'"
cd $WorkingDirectory

echo ""
echo "Removendo o ambiente virtual no powershell se existir com 'rm .venv -Recurse -Force'"
if (Test-Path -Path .venv) {
    echo "Ambiente virtual encontrado, removendo com 'rm .venv -Recurse -Force'"
    rm .venv -Recurse -Force

} else {
    echo "Ambiente virtual não encontrado"
}

echo ""
echo "Criando o ambiente virtual '.venv' com 'python -m venv .venv'"
python -m venv .venv

echo ""
echo "Ativando o ambiente virtual com '.\.venv\Scripts\Activate.ps1'"
.\.venv\Scripts\Activate.ps1

echo ""
echo "Listando as bibliotecas padrões inicias com 'pip list'"
pip list

echo ""
echo "Listando as bibliotecas que serão instaladas com 'cat requirements.txt'"
cat requirements.txt

echo ""
echo "Instalando as bibliotecas do projeto com 'pip install -r requirements.txt'"
pip install -r requirements.txt

echo ""
echo "Listando as bibliotecas após a instalação com 'pip list'"
pip list

echo ""
echo "Revendo as bibliotecas que foram instaladas com 'cat requirements.txt'"
cat requirements.txt

echo ""
echo "Voltando para a pasta raiz com 'cd $parentPath'"
cd $parentPath