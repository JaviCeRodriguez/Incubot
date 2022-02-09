# Incubot 🍃🤖

Bot de Discord, hecho en Python y MongoDB.

## 🟩 Módulos

- **Help**: Ayuda del bot. Muestra los comandos disponibles.
- **Welcome**: Mensaje de bienvenida a los nuevos usuarios del servidor.
- **DailyReport**: Mensaje diario de reporte de usuarios. Se ejecuta cada día a las 11:00 y los guarda en MongoDB.

## 🟩 Comandos

- **>help**: Muestra la lista de comandos disponibles.
- **>daily**: Muestra el mensaje de reporte diario.

## Variables de entorno

Crear un archivo `.env` con las siguientes variables:
```
DISCORD_PREFIX=<PREFIJO>
DISCORD_TOKEN=<TOKEN_BOT>
DISCORD_WELCOME_CH_ID=<ID_CANAL>
```

## 🟩 Instalación

```bash
git clone https://github.com/JaviCeRodriguez/Incubot.git
cd Incubot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python ./src/bot.py
```