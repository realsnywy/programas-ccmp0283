import java.util.Scanner;

public class FixIAE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número para calcular a raiz quadrada: ");
        double number = scanner.nextDouble();

        // Prevenção: Validar a entrada antes de chamar o método.
        if (number < 0) {
            System.out.println("Erro: Não é possível calcular a raiz quadrada de um número negativo.");
        } else {
            double result = calculateSquareRoot(number);
            System.out.println("A raiz quadrada é: " + result);
        }

        scanner.close();
    }

    public static double calculateSquareRoot(double number) {
        // Prevenção adicional: Garantir que o método não receba argumentos inválidos.
        if (number < 0) {
            throw new IllegalArgumentException("Número negativo: não é possível calcular a raiz quadrada.");
        }
        return Math.sqrt(number);
    }
}