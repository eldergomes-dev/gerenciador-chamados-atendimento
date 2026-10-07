# Gerenciador de Chamados e Atendimento

Sistema corporativo completo para gestão de chamados, suporte técnico e atendimento ao cliente.

Este repositório contém a implementação do sistema de Helpdesk / Service Desk, projetado com foco em arquitetura de software para o mercado de trabalho, utilizando boas práticas de desenvolvimento, código limpo e padrões de segurança.

## Objetivo do Projeto

Fornecer uma solução eficiente e modular para controle de solicitações de suporte em ambiente empresarial, abrangendo:

- **Abertura e Acompanhamento de Chamados:** Cadastro de solicitações por usuários e clientes.
- **Gerenciamento de Atendimentos:** Painel para suporte técnico, atribuição de chamados e alteração de status.
- **Níveis de Acesso e Permissões:** Separação clara de papeis entre clientes, atendentes e administradores.
- **Acordo de Nível de Serviço (SLA):** Controle automatizado de prazos de resposta e resolução.
- **Notificações Automatizadas:** Envio de alertas por e-mail para atualizações de status.

## Diretrizes de Desenvolvimento

- **Nomes claros e expressivos:** Sem utilização de abreviações em pastas, arquivos, variáveis, funções ou classes.
- **Padrões de mercado:** Estrutura modular, testes automatizados e documentação clara de interface.
- **Código em Português:** Manutenção da nomenclatura de negócio em português para clareza dos conceitos.

## Estrutura do Repositório

| Módulo | Descrição | Tecnologias |
| :--- | :--- | :--- |
| `interface-programacao-aplicacao` | API Backend responsável pelas regras de negócio, banco de dados e autenticação. | Python, FastAPI, SQLAlchemy, MySQL |

---

Projeto desenvolvido para consolidação prática de desenvolvimento backend corporativo.