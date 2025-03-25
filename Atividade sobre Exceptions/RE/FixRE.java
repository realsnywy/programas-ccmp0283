import java.util.Scanner;

public class FixRE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Digite o tamanho do array: ");
            int size = scanner.nextInt();

            if (size <= 0) {
                throw new IllegalArgumentException("O tamanho do array deve ser maior que zero.");
            }

            int[] numbers = new int[size];

            System.out.println("Digite o índice que deseja acessar: ");
            int index = scanner.nextInt();

            // Validação para evitar ArrayIndexOutOfBoundsException.
            if (index < 0 || index >= size) {
                throw new IndexOutOfBoundsException("Índice fora dos limites do array.");
            }

            System.out.println("Valor no índice " + index + ": " + numbers[index]);
        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Erro: " + e.getMessage());
        } catch (RuntimeException e) {
            System.out.println("Erro inesperado: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}