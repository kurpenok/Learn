package main

import (
	"fmt"
	"net/http"
	"html/template"
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

type Article struct {
	Id uint16
	Title, Anons, Text string
}

var posts = []Article{}

func index(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/index.html", "templates/header.html", "templates/footer.html")

	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	
	db, err := db.Open("mysql", "root:root@tcp(127.0.0.1:8888)/golang")
	if err != nil {
		panic(err)
	}
	defer db.close()

	res, err := db.Query("SELECT * FROM `articles`")
	if err != nil {
		panic(err)
	}
	
	posts = []Article{}
	for res.Next() {
		var post Article
		err = res.Scan(&post.Id, &post.Title, &post.Anons, &post.Text)
		if err != nil {
			panic(err)
		}

		posts = append(posts, post)
	}

	t.ExecuteTemplate(w, "index", nil)
}

func create(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/create.html", "templates/header.html", "templates/footer.html")

	if err != nil {
		fmt.Fprintf(w, err.Error())
	}

	t.ExecuteTemplate(w, "create", nil)
}

func save(w, http.ResponseWriter, r *http.Request) {
	title := r.FormValue("title")
	anons := r.FormValue("anons")
	text := r.FormValue("text")
	
	if title == "" || anons == "" || text == "" {
		fmt.Fprintf(w, "Incorrect input")
	} else {
		db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:8888)/golang")
		if err != nil {
			panic(err)
		}
		defer db.Close()

		insert, err := db.Query(fmt.Sprintf("INSERT INTO `articles` (`title`, `anons`, `text`)
								VALUES('%s', '%s', '%s')", title, anons, text))
		if err != nil {
			panic(err)
		}
		defer insert.Close()

		http.Redirect(w, r, "/", http.StatusSeeOther)
	}
}

func handle() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
	http.HandleFunc("/", index)
	http.HandleFunc("/create", create)
	http.ListenAndServe(":8000", nil)
}

func main() {
	handle()
}

