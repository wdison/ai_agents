# Recuperar a pasta que está esse script para poder subir um nível entrar no mcp_server, fazer a execução e depois ficar na pasta pai da pasta desse script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
# echo "Pasta do script: $scriptPath"

& "$scriptPath\prepare_env_base_win.ps1" "mcp_client"
