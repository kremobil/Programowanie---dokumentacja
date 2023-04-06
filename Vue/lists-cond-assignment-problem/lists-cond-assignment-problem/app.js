const app = Vue.createApp({
  data() {
    return {
      userInput: '',
      tasks: [],
    };
  },
  methods: {
    addTask() {
      this.tasks.push(this.userInput);
      this.userInput = '';
    },
  },
});
app.mount('#assignment');
