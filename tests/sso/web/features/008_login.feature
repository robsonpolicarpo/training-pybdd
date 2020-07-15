#language:pt

@web @b2badmin @portalweb
Funcionalidade: 008 Login
  Para validar a autenticação no sistema
  Como usuário cadastrado no sistema
  Realizo o login e faço as validações da tela de login

  @logintest
  Cenário: CN01 Login realizado com sucesso
    Dado   que esteja logado no B2B Admin

  @logintest
  Cenário: CN02 TESTE 2
    Dado   que esteja logado no B2B Admin

  Cenário: CN01 Login realizado com sucesso 2
    Dado   que estou na tela de Login
    Quando preencho os campos email e senha com dados válidos
    Quando clico no botão 'Entrar' do formulário de login
    Então  o sistema verifica os dados e apresenta a tela de dashboard

  Cenário: CN02 Logout realizado com sucesso
    Quando clico no menu dropdown do usuário logado no topo à direita da página
    Quando clico na opção 'Sair' do dropdown
    Então  o sistema realiza o logout redirecionando para a página de login

  Esquema do Cenário: Outline: CN03 Verificar obrigatoriedade dos campos
    Dado   que estou na tela de Login
    Quando não informo o campo <campo> do formulário de login
    Quando clico no botão 'Entrar' do formulário de login
    Então  o sistema deverá apresentar a mensagem para campo obritatório <campo> de login
    Exemplos:
      | campo    |
      | email    |
      | password |

  Esquema do Cenário: CN04 Verificação de Email ou Senha incorreto
    Dado   que estou na tela de Login
    Quando informo o email <email> e senha <senha>
    Quando clico no botão 'Entrar' do formulário de login
    Então  o sistema deverá apresentar a mensagem <mensagem> na tela de login
    Exemplos:
      | email           | senha         | mensagem                          |
      | admin@invalid   | admin         | Erro! Usuário ou senha incorretos |
      | admin@admin.com | admin-invalid | Erro! Usuário ou senha incorretos |