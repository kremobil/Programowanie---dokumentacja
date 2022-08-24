/* Set up using Vue 3 */
import { createApp } from 'vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core';

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

/* import specific icons */
import { faCircleUser } from '@fortawesome/free-regular-svg-icons';
import {
  faCartShopping,
  faBars,
  faPlus,
  faMinus,
} from '@fortawesome/free-solid-svg-icons';
import App from './App.vue';
import router from './router';

/* add icons to the library */
library.add(faCircleUser, faCartShopping, faBars, faPlus, faMinus);

createApp(App)
  .use(router)
  .component('font-awesome-icon', FontAwesomeIcon)
  .mount('#app');
