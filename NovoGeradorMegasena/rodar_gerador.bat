@echo off
REM === Script para rodar o gerador da Mega Sena ===
REM Agora pede as configurações ao usuário antes de rodar

color 0A
chcp 65001 >nul

echo =============================================
echo      GERADOR DE JOGOS MEGA SENA
set /p NUMEROS_POR_JOGO=Digite a quantidade de numeros por jogo [padrão: 6]: 
set /p QTD_JOGOS=Digite a quantidade de jogos a gerar [padrão: 3]: 

echo =============================================
if not "%NUMEROS_POR_JOGO%"=="" (
    echo      Números por jogo: %NUMEROS_POR_JOGO%
) else (
    echo      Números por jogo: [padrão]
)
if not "%QTD_JOGOS%"=="" (
    echo      Quantidade de jogos: %QTD_JOGOS%
) else (
    echo      Quantidade de jogos: [padrão]
)
echo =============================================

REM Verifica se o pip está disponível
where pip >nul 2>nul
if errorlevel 1 (
    echo Erro: pip não encontrado. Instale o Python e adicione o pip ao PATH.
    pause
    exit /b 1
)

REM Instala os requirements
pip install -r requirements.txt
if errorlevel 1 (
    echo Erro ao instalar os requirements.
    pause
    exit /b 1
)

echo.
echo Rodando o gerador...
echo.
if "%NUMEROS_POR_JOGO%"=="" (
    if "%QTD_JOGOS%"=="" (
        python gerador.py
    ) else (
        python gerador.py 6 %QTD_JOGOS%
    )
) else (
    if "%QTD_JOGOS%"=="" (
        python gerador.py %NUMEROS_POR_JOGO%
    ) else (
        python gerador.py %NUMEROS_POR_JOGO% %QTD_JOGOS%
    )
)
echo.
echo =============================================
echo Execução finalizada.
pause
