import java.util.Scanner;

public class java_enkripsi {

    // Fungsi untuk mengenkripsi teks dengan menggunakan nilai geser dari kunci
    public static String encrypt(String text, String key) {
        StringBuilder result = new StringBuilder();
        int keyLen = key.length();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            char shift = key.charAt(i % keyLen);

            if (Character.isUpperCase(c)) {
                c = (char) (((c - 'A' + shift - 'A') % 26) + 'A');
            } else if (Character.isLowerCase(c)) {
                c = (char) (((c - 'a' + shift - 'a') % 26) + 'a');
            }
            result.append(c);
        }
        return result.toString();
    }

    // Fungsi untuk mendekripsi teks yang telah dienkripsi dengan menggunakan nilai geser dari kunci
    public static String decrypt(String text, String key) {
        StringBuilder result = new StringBuilder();
        int keyLen = key.length();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            char shift = key.charAt(i % keyLen);

            if (Character.isUpperCase(c)) {
                c = (char) (((c - 'A' + 26 - (shift - 'A')) % 26) + 'A');
            } else if (Character.isLowerCase(c)) {
                c = (char) (((c - 'a' + 26 - (shift - 'a')) % 26) + 'a');
            }
            result.append(c);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Selamat datang di program enkripsi dan dekripsi menggunakan metode nilai geser yang rumit.");
        System.out.println("1. Enkripsi");
        System.out.println("2. Dekripsi");

        System.out.print("Masukkan pilihan (1/2): ");
        int choice = scanner.nextInt();

        scanner.nextLine(); // Membuang karakter newline dari input sebelumnya

        System.out.print("Masukkan teks: ");
        String inputText = scanner.nextLine();

        System.out.print("Masukkan kunci: ");
        String key = scanner.nextLine();

        switch (choice) {
            case 1:
                String encryptedText = encrypt(inputText, key);
                System.out.println("Hasil enkripsi: " + encryptedText);
                break;
            case 2:
                String decryptedText = decrypt(inputText, key);
                System.out.println("Hasil dekripsi: " + decryptedText);
                break;
            default:
                System.out.println("Pilihan tidak valid.");
        }

        scanner.close();
    }
}
