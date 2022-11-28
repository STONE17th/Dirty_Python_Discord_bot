FROM python:slim
RUN pip install discord
WORKDIR /cx3-bot
RUN apt-get update && apt-get install -y git && git clone https://github.com/STONE17th/Cx3-Bot.git .
CMD ["git", "pull", "&&", "python3", "main.py"]