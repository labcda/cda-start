# Plano — CDA Start

## Objetivo
Criar um PWA estático, mobile-first e responsivo, em português do Brasil, para onboarding de novos colaboradores do Laboratório CDA. A experiência será um AVA compacto: painel com progresso local, módulos de consulta, busca de exames e quizzes rápidos.

## Arquitetura
- **Entrega:** frontend estático (HTML/CSS/JS vanilla), sem servidor, banco ou login; a natureza operacional e de consulta não exige persistência remota.
- **Rotas:** uma única rota `/` com navegação por módulos no cliente; `public/manus-routes.json` declara a rota.
- **PWA:** manifesto próprio em `public/manifest.webmanifest` e service worker simples para cache do shell e uso offline básico. A interface não coleta dados de pacientes.
- **Persistência:** `localStorage` para status de módulos, progresso e respostas de quiz no dispositivo.
- **Conteúdo:** dados públicos do site oficial do CDA + regras internas fornecidas na solicitação. A tabela de exames usa preparos resumidos e inclui aviso para conferir sistema/protocolo vigente.

## Estrutura
- `index.html`: shell semântico, navegação, regiões de conteúdo e templates.
- `styles.css`: tokens visuais, responsividade, cards, painéis e acessibilidade.
- `app.js`: dados dos módulos e exames, renderização, busca, filtros, progresso, quizzes e registro do service worker.
- `public/manifest.webmanifest`: metadados instaláveis.
- `public/sw.js`: cache-first do shell estático.
- `public/manus-routes.json`: manifesto obrigatório de rotas.
- `logo.svg`: identidade CDA Start reutilizada no cabeçalho e favicon.

## Direção de deployment
Frontend estático servido por um servidor local simples no Preview, com fallback de rota apenas na aplicação de uma rota (`/`). Não há APIs, autenticação nem dados dinâmicos externos. Em publicação, o output será o diretório raiz do projeto; assets versionados podem ser cacheados e o HTML deve permanecer atualizável.

## Verificação
- inspeção dos arquivos e sintaxe JavaScript;
- iniciar servidor na porta 3000 e validar `GET /` e `GET /manus-routes.json` com HTTP 200;
- confirmar que o manifesto servido é JSON com a rota `/`;
- conferir presença dos módulos, dos 36 exames, dos textos críticos (urina 10h, fezes 15h, pisos, LGPD) e interação de busca/progresso por inspeção e checks locais.
