Vue.filter("capitalize", function (value) {
    if (!value) {
        return ""
    }
    value = value.toString()
    return value.replace(/b\w/g, function(l) {
        return l.toUpperCase()
    })
});

Vue.component("app-car", {
    data: function() {
        return {
            cars: [
                {model: "Lada"},
                {model: "UAZ"}
            ]
        }
    },
    template: '<div><div class="car" v-for="car in cars"><p>{{ car.model }}</p></div></div>'
});

new Vue ({
    el: "#app",
    
    data: {
        text: "Hello, world!",
        style: "",
        value: 1,
        show: true,
        message: "Message"
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
        },
        show_message() {
            return this.message.toUpperCase()
        }
    },
    filters: {
        lower(value) {
            return value.toLowerCase()
        }
    }
});

