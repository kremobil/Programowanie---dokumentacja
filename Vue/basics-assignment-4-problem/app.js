const app = Vue.createApp({
  data() {
    return {
      firstInput: '',
      showed: true,
      color: '',
    };
  },
  computed: {
    classes() {
      if (this.firstInput === 'user1') {
        return ['user1', this.showed ? 'visible' : 'hidden'];
      } else if (this.firstInput === 'user2') {
        return ['user2', this.showed ? 'visible' : 'hidden'];
      }
    },
  },
  methods: {
    show() {
      this.showed = !this.showed;
    },
  },
});
app.mount('#assignment');
