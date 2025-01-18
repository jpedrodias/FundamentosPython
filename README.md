# Fundamentos de Python
> Entidade Formadora: EISnt
> 
> Duração: 50h
> 
> 2025-01 - 2025-04


## Windows: Configuração inicial do Ambiente Virtual 
```bash
python -m venv C:\TEMP\fundpython --prompt "Fundamentos de Python"
```

**Remover as restrições de segurança do powershell**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

## Windows: Ativação do ambiente virtual

**em PowerShell**:
```bash
C:\TEMP\fundpython\Scripts\Activate.ps1
```

**em cmd** (linha de comandos):
```bash
C:\TEMP\fundpython\Scripts\activate.bat
```

## Linux: Configuração de um ambiente virtual
```bash
python3 -m venv /tmp/fundpython --prompt "Fundamentos de Python"
```

## Linux: Ativação do ambiente virtual
```bash
source /tmp/fundpython/bin/activate
```

## Instalação de prerequesitos
```bash
pip install -r requirements.txt
```
