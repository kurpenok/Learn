<template>
    <div>
        <h1>{{ message }}</h1>
        <app-input :msg="message" @message_change="message=$event"></app-input>
    </div>
</template>

<script>
import Input from './Field.vue';

export default {
    data() {
        return {
            message: "Example text"
        }
    },
    components: {
        "app-input": Input
    }
}

</script>

