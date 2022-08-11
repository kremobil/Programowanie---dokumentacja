<template>
  <div class="home">
    <Welcome />
    <Post v-for="post in posts" :key="post.title" :item="post" />
  </div>
</template>

<script>
import Welcome from '@/components/welcome.vue';
import Post from '@/components/post.vue';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    Welcome,
    Post,
  },
  data() {
    return {
      posts: [
        {
          upload: '22 czerwca 2022',
          author: 'Agnieszka',
          title: 'Wakacyjne życzenia',
          tekst: false,
          textContent: '',
          zdjecia: true,
          imgurl: [
            'http://sp46.netstrefa.pl/images/wn.png',
          ],
          video: false,
          vidurl: '',
        },
        {
          upload: '8 lipca 2022',
          author: 'Agnieszka',
          title: 'Półkolonie w Naszej szkole',
          tekst: true,
          textContent: 'Po raz kolejny w naszej szkole zorganizowano dwa turnusy półkolonii letnich (w terminie 27.06-8.07.2022 r.). Uczestniczyło w nich 90 dzieci pod opieką wychowawców: Agnieszki Kosickiej, Małgorzaty Abramowskiej, Bożeny Nowak, Alicji Gach i czuwającej nad całością półkolonii kierownikiem Anną Brzostek.Półkoloniści brali udział w szczegółowo przygotowanym programie, który składał się z zajęć rekreacyjnych oraz zajęć o charakterze profilaktycznym, które prowadziła pani Maria Strabel. Odpowiednie metody i formy pracy pozwoliły na stworzenie pozytywnego klimatu zachęcającego do aktywnego wypoczynku. Półkolonie były bardzo ciekawą i bezpieczną formą spędzania wolnego czasu przez dzieci naszej szkoły w czasie wakacji. Ich uśmiechy na buziach utwierdziły nas w przekonaniu, że wszyscy miło i przyjemnie spędzili czas. Również swoje zadowolenie wyrazili rodzice i opiekunowie naszych uczniów. A gdzie byliśmy i co robiliśmy, obejrzycie na fotografiach poniżej :)',
          zdjecia: true,
          imgurl: [
            'http://sp46.netstrefa.pl/images/pa.png',
            'http://sp46.netstrefa.pl/images/pa1.png',
          ],
          video: false,
          vidurl: '',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
  .home {
    transition: all 0.5s;
    width: 100%;
    @media (min-width: 1024px) {
      width: 90%;
    }
  }
</style>
