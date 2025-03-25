public class BugNPE {
    public static void main(String[] args) {
        // Contexto: Um programa que tenta acessar o comprimento de uma string fornecida pelo usuário.
        String userInput = null; // Simulando uma entrada nula.

        // Causa raiz: Nenhuma validação foi feita para verificar se o objeto é nulo antes de usá-lo.
        System.out.println("O comprimento da string é: " + userInput.length());
    }
}