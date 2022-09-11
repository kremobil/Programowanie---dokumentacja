const app = Vue.createApp({
  data() {
    return {
      name: 'Wiktor',
      age: 16,
      img: 'https://images.pexels.com/photos/11035366/pexels-photo-11035366.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    };
  },
  methods: {
    genNum() {
      return Math.round(Math.random());
    },
  },
});
app.mount('#assignment');
