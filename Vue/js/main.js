new Vue ({
    el: "#app",
    
    data: {
        text: "Hello, world!",
        style: "",
        value: 1,
    },

    methods: {
        change () {
            this.text = "Implemented method was runned"
        }
        increment (value) {
            this.value = value
            if (value == 25) {
                alert("Number 25")
            }
        }
    },
    computed: {
        new_value () {
            return this.value * 2
        }
    }
});

