import java.util.Scanner;

public class FixNFE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número inteiro: ");
        String userInput = scanner.nextLine();

        // Prevenção: Validar a entrada do usuário antes de convertê-la para um número.
        try {
            int number = Integer.parseInt(userInput); // Tentativa de conversão.
            System.out.println("O número digitado foi: " + number);
        } catch (NumberFormatException e) {
            // Tratamento: Informar ao usuário que a entrada é inválida.
            System.out.println("Erro: A entrada fornecida não é um número inteiro válido.");
        }

        scanner.close();
    }
}