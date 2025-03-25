import java.util.Scanner;

public class FixISE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Digite algo: ");
            String input = scanner.nextLine();

            // Usando o scanner enquanto ele está em um estado válido.
            System.out.println("Você digitou: " + input);
        } finally {
            // Fechando o scanner apenas após o uso.
            scanner.close();
        }
    }
}