from funçoes import validarCartao
from funçoes import validarCvv

cartao = str(input('Digite o numero do cartão:'))
cvv = str(input('Digite o codigo CVV do cartão: '))

validarCartao(cartao)
validarCvv(cvv)