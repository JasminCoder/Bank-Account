from CuentaBancaria import CuentaBancaria

cuentaA = CuentaBancaria(0.15, 30000)
cuentaB = CuentaBancaria(0.05, 1000)

cuentaA.deposito(5000).deposito(3000).deposito(100000).retiro(40000).generar_interes().mostar_info_cuenta()

cuentaB.deposito(87000).deposito(60000).retiro(10000).retiro(20000).retiro(15000).retiro(50000).generar_interes().mostar_info_cuenta()

CuentaBancaria.cuenta()