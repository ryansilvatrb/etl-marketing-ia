import pandas as pd

# =========================
# EXTRAÇÃO
# =========================
df = pd.read_csv("data/users.csv")

# =========================
# TRANSFORMAÇÃO (IA simulada)
# =========================
def gerar_mensagem(nome, conta, cartao):
    return (
        f"Olá {nome}! 🎉\n"
        f"Temos novidades exclusivas para sua {conta}.\n"
        f"Aproveite benefícios especiais no seu cartão {cartao}.\n"
        f"Conte com o Santander para evoluir com você!"
    )

df["mensagem"] = df.apply(
    lambda row: gerar_mensagem(row["nome"], row["conta"], row["cartao"]),
    axis=1
)

# =========================
# LOAD
# =========================
df.to_csv("output/mensagens_marketing.csv", index=False)

print("✅ Pipeline ETL executado com sucesso!")
