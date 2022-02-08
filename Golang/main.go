package main

import ("fmt"
		"net/http")

func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Go was started!")
}

func contacts(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Contacts was started!")
}

func handle() {
	http.HandleFunc("/", home)
	http.HandleFunc("/contacts/", contacts)

	http.ListenAndServe(":8000", nil)
}

func main() {
	handle()
}

