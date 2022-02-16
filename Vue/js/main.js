new Vue ({
    el: "#app",
    
    data: {
        text: "Hello, world!",
        style: ""
    },

    methods: {
        change () {
            this.text = "Implemented method was runned"
        }
    }
});

