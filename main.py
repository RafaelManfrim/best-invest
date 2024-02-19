import pandas as pd
import matplotlib.pyplot as plt


def display_menu():
    print("===== Menu =====")
    print("1. Ações")
    print("2. Fundos Imobiliários")
    print("3. Tudo")
    print("4. Sair")


def quit_program():
    print("Finalizando o programa...")
    exit()


def carregar_segmentos():
    print('Carregando segmentos...')
    pass


def carregar_meta_investimento():
    print('Carregando meta de investimento por segmento...')
    pass


def carregar_carteira(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    df['Saldo bruto'] = df.apply(lambda row: row["Saldo bruto"].replace('.', '').replace(',', '.'), axis=1)
    df['Saldo bruto'] = df['Saldo bruto'].astype(float)
    df['Participação na carteira (%)'] = df.apply(lambda row: row["Participação na carteira (%)"].replace('.', '').replace(',', '.'), axis=1)
    df['Participação na carteira (%)'] = df['Participação na carteira (%)'].astype(float)
    return df.sort_values(by='Saldo bruto', ascending=False)


def gerar_grafico(df: pd.DataFrame):
    plt.pie(df['Participação na carteira (%)'], labels=df['Produto'], autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição por ativo')
    plt.savefig('grafico_pizza-fii.png')
    plt.show()


def calcular_investimento():
    print('Calculando investimento...')
    pass


if __name__ == '__main__':
    df = carregar_carteira("path")
    print(df)

    while True:
        display_menu()
        choice = input("Escolha o que deseja calcular: ")

        if choice == '1':
            df = df.loc[df['Classe do Ativo'] == "Ação"]
            print('Ações')
        elif choice == '2':
            df = df.loc[df['Classe do Ativo'] == "Fundo Imobiliário"]
            print('FIIs')
        elif choice == '3':
            print('Tudo')
        elif choice == '4':
            quit_program()
        else:
            print("Escolha inválida. Tente novamente.")
            continue

        carregar_segmentos()
        carregar_meta_investimento()
        gerar_grafico(df)
        calcular_investimento()
