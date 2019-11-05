# Roteamento de veículos com Janela de tempo

Algoritmo para problema de roteamento de veículos, o qual gera rotas viáveis e calcula
soluções via simplex

## Configuração

Tenha um ambiente gurobi apropriadamente configurado.

```bash
## instalar python e PIP
apt-get install python3 python3-pip

# Executar o projeto
gurobi.sh main.py ./models/INSTANCIA.txt # modifique para sua instância
```

Para executar todas as instâncias, execute o script [benchmark.sh](benchmark.sh)

## Modelos

http://web.cba.neu.edu/~msolomon/problems.htm

### Instâncias

https://www.sintef.no/globalassets/project/top/vrptw/solomon/solomon-100.zip