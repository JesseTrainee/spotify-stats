# Usa uma imagem oficial do Node.js
FROM node:18

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o package.json e instala as dependências
COPY package.json package-lock.json ./
RUN npm install

# Copia os arquivos do frontend
COPY . .

# Expõe a porta do React
EXPOSE 3000

# Comando para rodar o frontend
CMD ["npm", "start"]
