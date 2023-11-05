package br.com.TypesBalancas;

import br.com.Interface.IBalanca;
import br.com.Produto.produtos;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class ToledoMGV6 implements IBalanca<produtos> {
    @Override
    public void exportar(List<produtos> produtos, String pastaArquivoTxt) {

    }
}