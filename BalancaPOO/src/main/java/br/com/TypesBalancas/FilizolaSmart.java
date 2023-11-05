package br.com.TypesBalancas;

import br.com.Interface.IBalanca;
import br.com.Produto.produtos;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class FilizolaSmart implements IBalanca<produtos> {
    @Override
    public void exportar(List<produtos> produtos, String pastaArquivoTxt) {
        try {
            FileWriter arquivo = new FileWriter(pastaArquivoTxt, true);
            PrintWriter escreverArquivo = new PrintWriter(arquivo);

            for (produtos produto : produtos) {
                String codigo = String.format("%06d", produto.getCodigo());
                String tipo = String.format("%s", produto.getTipo());
                String descricao = String.format("%-22.22s", produto.getDescricao());
                String valor = String.format("%f", produto.getValor()).replace(",", "");
                String texto = String.format("%s%s%s000%s\n", codigo, tipo, descricao, valor);

                escreverArquivo.append(texto);
            }
            escreverArquivo.close();
            arquivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
