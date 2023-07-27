package main

import (
	"fmt"
)

// Fungsi untuk mengenkripsi teks dengan menggunakan nilai geser dari kunci
func encrypt(text, key string) string {
	result := ""
	keyLen := len(key)

	for i := 0; i < len(text); i++ {
		char := text[i]
		shift := key[i%keyLen]

		// Periksa apakah karakter adalah huruf (A-Z atau a-z)
		if char >= 'A' && char <= 'Z' {
			char = (char-'A'+byte(shift-'A'))%26 + 'A'
		} else if char >= 'a' && char <= 'z' {
			char = (char-'a'+byte(shift-'a'))%26 + 'a'
		}
		result += string(char)
	}
	return result
}

// Fungsi untuk mendekripsi teks yang telah dienkripsi dengan menggunakan nilai geser dari kunci
func decrypt(text, key string) string {
	result := ""
	keyLen := len(key)

	for i := 0; i < len(text); i++ {
		char := text[i]
		shift := key[i%keyLen]

		// Periksa apakah karakter adalah huruf (A-Z atau a-z)
		if char >= 'A' && char <= 'Z' {
			char = (char-'A'+26-byte(shift-'A'))%26 + 'A'
		} else if char >= 'a' && char <= 'z' {
			char = (char-'a'+26-byte(shift-'a'))%26 + 'a'
		}
		result += string(char)
	}
	return result
}

func main() {
	var choice int
	var inputText, key string

	fmt.Println("Selamat datang di program enkripsi dan dekripsi menggunakan metode nilai geser yang rumit.")
	fmt.Println("1. Enkripsi")
	fmt.Println("2. Dekripsi")

	fmt.Print("Masukkan pilihan (1/2): ")
	fmt.Scanln(&choice)

	fmt.Print("Masukkan teks: ")
	fmt.Scanln(&inputText)

	fmt.Print("Masukkan kunci: ")
	fmt.Scanln(&key)

	switch choice {
	case 1:
		encryptedText := encrypt(inputText, key)
		fmt.Println("Hasil enkripsi:", encryptedText)
	case 2:
		decryptedText := decrypt(inputText, key)
		fmt.Println("Hasil dekripsi:", decryptedText)
	default:
		fmt.Println("Pilihan tidak valid.")
	}
}
