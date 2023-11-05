package br.com.Factory;

import br.com.TypesBalancas.FilizolaSmart;
import br.com.Enums.TipoBalanca;
import br.com.Interface.IBalanca;
import br.com.TypesBalancas.UranoIntegra;

public class BalancaFactory {

    public static IBalanca getBalanca(TipoBalanca tipoBalanca) {
        if(TipoBalanca.FILIZOLA_SMART.equals(tipoBalanca)) {
            return new FilizolaSmart();
        }
        if(TipoBalanca.URANO_INTEGRA.equals(tipoBalanca)){
            return new UranoIntegra();
        }
        return null;
    }
}
