const app = Vue.createApp({
  data() {
    return {
      number: 0,
    };
  },
  methods: {
    addOne() {
      this.number++;
    },
    addFive() {
      this.number += 5;
    },
  },
  computed: {
    result() {
      if (this.number < 37) {
        return 'Not there yet';
      } else if (this.number === 37) {
        return this.number;
      } else {
        return 'Too much!';
      }
    },
  },
  watch: {
    result() {
      setTimeout(() => {
        this.number = 0;
        const notifications = document.querySelector('.notifications');
        const notify = document.createElement('div');
        notify.classList.add('notify', 'fade-in', 'fade-out');
        notify.textContent = 'Number reset';
        notifications.appendChild(notify);
      }, 5000);
    },
  },
});

app.mount('#assignment');
