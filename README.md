# ai_agents


## Config Enviroment
### Criando ambiente virtual
```powershell
echo "Criando o ambiente virtual '.venv' com 'python -m venv .venv'"
python -m venv .venv
```

### Ativando ambiente virtual
```powershell
echo "Ativando o ambiente virtual com '.\.venv\Scripts\Activate.ps1'"
.\.venv\Scripts\Activate.ps1
```

### Listando as bibliotecas
```powershell
echo "Listando as bibliotecas padrões inicias com 'pip list'"
pip list
```

### Listando as bibliotecas do projeto/requirements
```powershell
echo "Listando as bibliotecas que serão instaladas com 'cat requirements.txt'"
cat requirements.txt
```

### Instalando bibliotecas do projeto
```powershell
echo "Instalando as bibliotecas do projeto com 'pip install -r requirements.txt'"
pip install -r requirements.txt
```

### Listando as bibliotecas instaladas
```powershell
echo "Listando as bibliotecas após a instalação com 'pip list'"
pip list
```