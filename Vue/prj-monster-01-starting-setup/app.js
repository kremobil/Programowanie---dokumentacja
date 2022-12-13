const randomValue = (min, max) => {
  return Math.round(Math.random() * (max - min) + min);
};

const app = Vue.createApp({
  data() {
    return {
      playerHp: 100,
      monsterHp: 100,
      specialAttackDelay: 0,
      endMessage: '',
      battleLog: [],
    };
  },
  watch: {
    playerHp(value) {
      this.specialAttackDelay--;
      if (value === 0 && this.monsterHp === 0) {
        this.endMessage = "it's a draw";
      } else if (value <= 0) {
        this.endMessage = 'You lost!';
      }
    },
    monsterHp(value) {
      if (this.playerHp === 0 && value === 0) {
        this.endMessage = "it's a draw";
      } else if (value <= 0) {
        this.endMessage = 'You win!';
      }
    },
  },
  methods: {
    attackMonster() {
      const damage = randomValue(0, 15);
      this.battleLog.push({
        message: `Player attacks monster with normal atack and deals damage: ${damage}`,
        color: '#b39800',
      });
      this.monsterHp -= damage;
      this.attackPlayer();
    },
    attackPlayer() {
      const damage = randomValue(0, 20);
      this.battleLog.push({
        message: `Monster attacks player with normal atack and deals damage: ${damage}`,
        color: 'red',
      });
      this.playerHp -= damage;
    },
    specialAtack() {
      const damage = randomValue(15, 25);
      this.battleLog.push({
        message: `Player attacks monster with special atack and deals damage: ${damage}`,
        color: '#7700ff',
      });
      this.monsterHp -= damage;
      this.attackPlayer();
      this.specialAttackDelay = 6;
    },
    healPlayer() {
      const heal = randomValue(8, 20);
      if (this.playerHp + heal > 100) {
        this.playerHp = 100;
      } else {
        this.playerHp += heal;
      }
      this.battleLog.push({
        message: `Player was heal: ${heal} and now has ${this.playerHp}`,
        color: 'green',
      });
      this.attackPlayer();
    },
    resetGame() {
      this.playerHp = 100;
      this.monsterHp = 100;
      this.specialAttackDelay = 0;
      this.endMessage = '';
      this.battleLog = [];
    },
    surrender() {
      this.endMessage = 'You lost!';
      this.playerHp = 0;
    },
  },
  computed: {
    monsterHpBar() {
      width = Math.abs(this.monsterHp) + '%';
      if (this.monsterHp === 0) {
        return { width: '0%' };
      } else if (this.monsterHp < 0) {
        return { width: width, backgroundColor: 'red' };
      } else {
        return { width: width };
      }
    },
    playerHpBar() {
      width = Math.abs(this.playerHp) + '%';
      if (this.playerHp === 0) {
        return { width: '0%' };
      } else if (this.playerHp < 0) {
        return { width: width, backgroundColor: 'red' };
      } else {
        return { width: width };
      }
    },
    specialAttackDelayMessage() {
      return this.specialAttackDelay <= 0
        ? 'Special Atack'
        : this.specialAttackDelay === 1
        ? '1 round left'
        : `${this.specialAttackDelay} rounds left`;
    },
  },
});
app.mount('#game');
