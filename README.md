Prezado,

Para utilizardos recursos corretamente, faça o clone do projeto edite o arquivo contacts.json setando os emails que deverá ser encaminhado o alerta. O arquivo fica em "utils/contacts.json"

Após setar os emails no arquivo, salve o mesmo e execute o build da imagem em seu ambiente local (Lembre-se de estar como root ou estar com um usuario que tenha permissões para utilizar o docker).


Ex. de comando:
docker build -t emailpy .

Após o build você pode fazer executar sua imagem, apontando o arquivo principal "main.py" e passando os argumentos necessários para a autenticação no gmail, que são eles o --mail_user e o --mail_pass.

Ex. de comando:
docker run -it --name smailpy emailpy main.py --mail_user=emaildeacesso --mail_pass=senhadoemail

Se atente que para poder se conectar no email você tem que ativar a verificação de dois fatores e após isso gerar uma senha para apps, que é a senha que utilizaremos no nosso script.

Feito isso é para ser gerado logs se o processo deu falha ou se os emails foram encaminhados com sucesso.

