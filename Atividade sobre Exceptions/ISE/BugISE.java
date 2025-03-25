import java.util.Scanner;

public class BugISE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite algo: ");
        String input = scanner.nextLine();

        // Fechando o scanner.
        scanner.close();

        // Causa raiz: Tentativa de usar o scanner após ele ter sido fechado.
        System.out.println("Você digitou: " + scanner.nextLine()); // Lança IllegalStateException.
    }
}