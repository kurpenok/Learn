new Vue ({
    el: "#app",
    
    data: {
        text: "Hello, world!",
        style: "",
        value: 1,
        show: true,
        cars: [
            {model: "Lada", speed: 200},
            {model: "UAZ", speed: 100}
        ]
    },

    methods: {
        change () {
            this.text = "Implemented method was runned"
        },
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

