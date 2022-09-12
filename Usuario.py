from cgi import print_arguments


class Usuario:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    def hacer_deposito(self, amount):	
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):	
        self.balance_cuenta -= amount
        return self

    def hacer_transferencia(self, terceros, amount):
        self.balance_cuenta-= amount
        terceros.balance_cuenta += amount
        return self
    
    def balance_final(self):
        print(f"{self.name} tiene un saldo de: {self.balance_cuenta}")
        return self



magdalena = Usuario("magdalena de la rosa", "delarosa@gmail.com")
fernando = Usuario("fernando martinez", "fernando22@gmail.com")
rosi = Usuario("rosi cat", "catwoman@gmail.com")

magdalena.hacer_deposito(1000).hacer_deposito(500).hacer_deposito(100).hacer_retiro(100).hacer_transferencia(fernando, 500).balance_final()
fernando.hacer_deposito(700).hacer_deposito(500).hacer_retiro(1000).hacer_retiro(300).hacer_transferencia(magdalena, 450).balance_final()
rosi.hacer_deposito(2000).hacer_retiro(150).hacer_retiro(200).hacer_retiro(80).hacer_transferencia(magdalena, 70).balance_final()

print("saldo actualizado magdalena: " + str(magdalena.balance_cuenta))
print("saldo actualizado fernando: " + str(fernando.balance_cuenta))
print("saldo actualizado rosi: " + str(rosi.balance_cuenta))