import java.util.Scanner;

public class BugNFE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número inteiro: ");
        String userInput = scanner.nextLine();

        // Causa raiz: Nenhuma validação foi feita para garantir que a entrada é um número válido.
        int number = Integer.parseInt(userInput); // Pode lançar NumberFormatException.
        System.out.println("O número digitado foi: " + number);

        scanner.close();
    }
}