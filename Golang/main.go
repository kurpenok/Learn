package main

import ("fmt"
		"net/http")

type User struct {
	name string
	age uint16
	money int16
	avg_grades, happiness float64
}

func (u *User) getAllInfo() string {
	return fmt.Sprintf("" +
		"[+] User name: %s\n" +
		"[+] Age: %d\n" +
		"[+] Money: %d\n",
		u.name, u.age, u.money)
}

func (u *User) setNewName(name string) {
	u.name = name
}

func home(w http.ResponseWriter, r *http.Request) {
	bob := User{"Bob", 21, 10243, 4.2, 0.8}
	bob.setNewName("Alex")
	fmt.Fprintf(w, bob.getAllInfo())

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
	// var bob User = ...
	// bob := User{name: "Bob", age: 21, money: 10243, avg_grades: 4.2, happiness: 0.8}

	handle()
}

