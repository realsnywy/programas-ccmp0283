import java.util.Objects;
import java.util.Scanner;

public class FixNPE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite uma string: ");
        String userInput = scanner.nextLine();

        // Prevenção: Garantir que a entrada do usuário não seja nula.
        userInput = Objects.requireNonNull(userInput, "A entrada não pode ser nula.");

        // Prevenção: Validar se a string está vazia antes de acessar seus métodos.
        if (!userInput.isEmpty()) {
            System.out.println("O comprimento da string é: " + userInput.length());
        } else {
            System.out.println("A string está vazia.");
        }

        scanner.close();
    }
}