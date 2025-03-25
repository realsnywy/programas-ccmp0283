public class BugIAE {
    public static void main(String[] args) {
        // Contexto: Um programa que calcula a raiz quadrada de um número.
        double number = -25; // Número inválido para cálculo de raiz quadrada.

        // Causa raiz: Nenhuma validação foi feita para garantir que o número é válido.
        double result = calculateSquareRoot(number); // Pode lançar IllegalArgumentException.
        System.out.println("A raiz quadrada é: " + result);
    }

    public static double calculateSquareRoot(double number) {
        if (number < 0) {
            throw new IllegalArgumentException("Número negativo: não é possível calcular a raiz quadrada.");
        }
        return Math.sqrt(number);
    }
}