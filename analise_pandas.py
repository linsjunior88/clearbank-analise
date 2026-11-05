"""Leitura alternativa e comparação das métricas com a solução nativa."""
import math
import pandas as pd


def analisar_com_pandas(caminho, validar_transacao):
    brutas = pd.read_csv(caminho, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    registros = [validar_transacao(linha) for linha in brutas.to_dict("records")]
    registros = [linha for linha in registros if linha is not None]
    if not registros:
        return {}
    df = pd.DataFrame(registros).drop_duplicates(subset="id", keep="first")
    df["mes"] = pd.to_datetime(df["data"]).dt.strftime("%Y-%m")
    df["credito"] = df["valor"].where(df["tipo"].eq("credito"), 0.0)
    df["debito"] = df["valor"].where(df["tipo"].eq("debito"), 0.0)
    grupos = df.groupby("mes", sort=True).agg(
        quantidade=("id", "size"), total_credito=("credito", "sum"),
        total_debito=("debito", "sum"), media=("valor", "mean"),
        maior_valor=("valor", "max"), menor_valor=("valor", "min"))
    grupos["saldo"] = grupos["total_credito"] - grupos["total_debito"]
    return {mes: {campo: int(valor) if campo == "quantidade" else round(float(valor), 2)
                  for campo, valor in dados.items()}
            for mes, dados in grupos.to_dict("index").items()}


def comparar_resultados(nativo, alternativo):
    assert nativo.keys() == alternativo.keys(), "Meses diferentes."
    for mes, dados in nativo.items():
        assert dados.keys() == alternativo[mes].keys(), f"Campos diferentes em {mes}."
        for campo, valor in dados.items():
            assert math.isclose(valor, alternativo[mes][campo], rel_tol=0, abs_tol=1e-9), (mes, campo)
    print("Comparação aprovada: todas as métricas mensais coincidem.")
