package main

import ("fmt"
		"net/http"
		"html/template")

type User struct {
	Name string
	Age uint16
	Money int16
	Avg_grades, Happiness float64

	Hobbies []string
}

func (u *User) getAllInfo() string {
	return fmt.Sprintf("" +
		"[+] User name: %s\n" +
		"[+] Age: %d\n" +
		"[+] Money: %d\n",
		u.Name, u.Age, u.Money)
}

func (u *User) setNewName(name string) {
	u.Name = name
}

func home(w http.ResponseWriter, r *http.Request) {
	bob := User{"Bob", 21, 10243, 4.2, 0.8, []string{"Football", "Dance"}}
	// bob.setNewName("Alex")
	// fmt.Fprintf(w, bob.getAllInfo())
	
	temp, _ := template.ParseFiles("templates/home.html")
	temp.Execute(w, bob)
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

