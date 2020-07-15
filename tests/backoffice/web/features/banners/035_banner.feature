#language:pt

@web @b2badmin @FT035
Funcionalidade: FT035 Banners
  Como usuário do sistema
  Desejo cadastrar imagens como banners de campanhas

  Contexto:
    Dado   que esteja logado no B2B Admin

  @automating
  Esquema do Cenário: CN01 Cadastrar novo banner de fornecedor
    Dado   na tela inicial acionar o card "Banners"
    Quando no card 'B2B Experience' acionar o botão "Novo banner de fornecedor"
    Quando no popup preencher as informações do banner <fornecedor> <vigencia> <data> <publico>
    Quando acionar a opção para criar o banner de fornecedor
    Então  o sistema deve apresentar mensagem de sucesso para criação do banner
    Exemplos:
      | fornecedor     | vigencia      | data   | publico                                    |
      | QABOT SUPPLIER | Personalizado | D, D+1 | Todos os varejos atendidos pelo fornecedor |
#      | QABOT SUPPLIER | 1 semana      | D      | Subir lista                                |

  @automated
  Esquema do Cenário: CN02 Cadastrar novo banner de simulador de margem
    Dado   na tela inicial acionar o card "Banners"
    Quando no card 'B2B Experience' acionar o botão "Novo banner de simulador de margem"
    Quando no popup preencher as informações do banner <fornecedor> <vigencia> <data> <publico>
    Quando acionar a opção para criar o banner de fornecedor
    Então  o sistema deve apresentar mensagem de sucesso para criação do banner
    Exemplos:
      | fornecedor | vigencia      | data   | publico          |
      |            | Personalizado | D, D+1 | Todos os varejos |
      |            | 1 semana      | D      | Subir lista      |

  @automated
  Esquema do Cenário: CN03 Cadastrar banner repositório de marketing
    Dado   na tela inicial acionar o card "Banners"
    Quando acionar a opção 'Repositório de marketing'
    Quando no repositório preencher os campos <slot> <tipo> <link> <vigencia> <data> para criar banner
    Quando no repositório, na opção de novo banner, realizar upload da imagem
    Quando no repositório acionar a opção para criar o banner
    Então  o sistema deve apresentar mensagem de sucesso para criação do banner de repositório
    Exemplos:
      | slot          | tipo     | link                                               | vigencia      | data   |
      | Home do HUB   | Sem Link |                                                    | Personalizado | D, D+1 |
      | Institucional | Com Link | https://b2b-admin-staging.devyandeh.com.br/banners | 1 semana      | D      |

  @automated
  Cenário: CN04 Upload imagem em solicitação de banner repositório de marketing
    Dado   na tela inicial acionar o card "Banners"
    Quando em 'Repositório de marketing' exista uma solicitação de banner
    Quando estou na tela 'Repositório de marketing'
    Quando na lista de solicitações de banner, realizar upload da imagem
    Então  o sistema deve apresentar mensagem de sucesso de upload do banner de repositório
    Então  o registro deverá ser apresentado na tela inicial de banner com imagem
