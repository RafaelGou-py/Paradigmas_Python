package br.com.TypesBalancas;

import br.com.Interface.IBalanca;
import br.com.Produto.produtos;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class UranoIntegra implements IBalanca<produtos> {
    @Override
    public void exportar(List<produtos> produtos, String pastaArquivoTxt) {
        try {
            FileWriter arquivo = new FileWriter(pastaArquivoTxt, true);
            PrintWriter escreverArquivo = new PrintWriter(arquivo);

            for (produtos produto : produtos) {
                String codigo = String.format("%06d", produto.getCodigo());
                String flag = "*";
                String tipo = "0";
                if (produto.getTipo().equals("6")) {
                    tipo = "6";
                }
                String descricao = String.format("%-20.20s", produto.getDescricao());
                String valor = String.format("%.2f", produto.getValor()).replace(",", "");
                String validade1 = "00000";
                String validade2 = "D";
                String texto = String.format("%s%s%s%s%s%s%s\n", codigo, flag, tipo, descricao, valor, validade1, validade2);

                escreverArquivo.append(texto);
            }
            escreverArquivo.close();
            arquivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

