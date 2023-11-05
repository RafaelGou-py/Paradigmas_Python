package br.com;

import br.com.Enums.TipoBalanca;
import br.com.Factory.BalancaFactory;
import br.com.Interface.IBalanca;
import br.com.Produto.produtos;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        produtos produto1 = new produtos();
        produto1.setCodigo(170);
        produto1.setTipo("P");
        produto1.setDescricao("QUEIJO CHEDDAR KG");
        produto1.setValor(30.89);

        produtos produto2 = new produtos();
        produto2.setCodigo(880);
        produto2.setTipo("P");
        produto2.setDescricao("QUEIJO MUSSARELA KG");
        produto2.setValor(27.99);

        produtos produto3 = new produtos();
        produto3.setCodigo(299);
        produto3.setTipo("P");
        produto3.setDescricao("LANCHE CHESTER KG");
        produto3.setValor(18.29);


        List<produtos> produtos = new ArrayList<>();
        produtos.add(produto1);
        produtos.add(produto2);
        produtos.add(produto3);

        try {
            File file = new File("CADTXT.TXT");

            if (file.exists()) {
                file.delete();
            }

            file.createNewFile();

            FileWriter fw = new FileWriter(file, true);
            PrintWriter pw = new PrintWriter(fw);

            pw.close();
        } catch (IOException e) {
            System.out.println("Arquivo não conseguiu ser criado");
            e.printStackTrace();
        }

        IBalanca balanca = BalancaFactory.getBalanca(TipoBalanca.FILIZOLA_SMART);
        String caminho = "CADTXT.TXT";
        balanca.exportar(produtos, caminho);
    }

    private static List<produtos> obterProdutos() {
        List<produtos> produtos = new ArrayList<>();

        produtos produto1 = new produtos();
        produto1.setCodigo(170);
        produto1.setTipo("P");
        produto1.setDescricao("QUEIJO CHEDDAR KG");
        produto1.setValor(30.89);

        produtos produto2 = new produtos();
        produto2.setCodigo(880);
        produto2.setTipo("P");
        produto2.setDescricao("QUEIJO MUSSARELA KG");
        produto2.setValor(27.99);

        produtos produto3 = new produtos();
        produto3.setCodigo(299);
        produto3.setTipo("P");
        produto3.setDescricao("LANCHE CHESTER KG");
        produto3.setValor(18.29);


        produtos = new ArrayList<>();
        produtos.add(produto1);
        produtos.add(produto2);
        produtos.add(produto3);

        return produtos;
    }

    private static void gerarArquivo(List<produtos> produtos) {

        //produtos = obterProdutos();

        try {
            File file = new File("PRODUTOS.TXT");

            if (file.exists()) {
                file.delete();
            }

            file.createNewFile();

            FileWriter fw = new FileWriter(file, true);
            PrintWriter pw = new PrintWriter(fw);

            pw.close();
            System.out.println("Arquivo PRODUTOS.TXT criado com sucesso.");

        } catch (IOException e) {
            System.out.println("Arquivo não conseguiu ser criado");
            e.printStackTrace();
        }

            IBalanca balanca = BalancaFactory.getBalanca(TipoBalanca.URANO_INTEGRA);
            String caminho = "PRODUTOS.TXT";
            balanca.exportar(produtos, caminho);

    }
}

