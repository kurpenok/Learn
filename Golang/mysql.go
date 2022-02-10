package main

import (
	"fmt"
	"database/sql"
	
	_ "github.com/go-sql-driver/mysql"
)

type User struct {
	Name string `json:"name"`
	Age uint16 `json:"age"`
}

func main() {
	db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:8889)/golang")

	if err != nil {
		panic(err)
	}

	defer db.Close()
	
	// Add data to database
	// insert, err := db.Query("<SQL Command>")

	insert, err := db.Query("INSERT INTO `users` (`name`, `age`) VALUES ('Alex', 25)")
	if err != nil {
		panic(err)
	}

	// Show data from database
	// res, err := db.Query("<SQL Command>")

	res, err := db.Query("SELECT `name`, `age` FROM `users`")
	if err != nil {
		panic(err)
	}

	for res.Next() {
		var user User
		err = res.Scan(&user.Name, &user.Age)
		if err != nil {
			panic(err)
		}
		fmt.Println(fmt.Srintf("[+] User: %s with age %d", user.Name, user.Age))
	}
}

