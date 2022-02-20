<template>
    <div>
        <h3>{{ msg }}</h3>
        <input type="text" :value="msg" @input="change">
        <p>{{ message }}</p>
    </div>
</template>

<script>

export default {
    props: ["msg"],
    data() {
        return {
            message: ""
        }
    },
    methods: {
        change(event) {
            this.message = event.target.value;
            this.$emit("message_change", this.message);
        }
    }
}

</script>


