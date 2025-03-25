import java.util.Scanner;

public class BugRE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o tamanho do array: ");
        int size = scanner.nextInt();

        int[] numbers = new int[size];

        System.out.println("Digite o índice que deseja acessar: ");
        int index = scanner.nextInt();

        // Causa raiz: Tentativa de acessar um índice fora dos limites do array.
        System.out.println("Valor no índice " + index + ": " + numbers[index]); // Lança ArrayIndexOutOfBoundsException.

        scanner.close();
    }
}