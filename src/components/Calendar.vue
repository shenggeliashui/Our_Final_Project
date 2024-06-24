<template>
  <div class="calendar">
    <div class="header">
      <button @click="prevMonth">&lt;</button>
      <h2>{{ monthNames[currentMonth] }} {{ currentYear }}</h2>
      <button @click="nextMonth">&gt;</button>
    </div>
    <div class="weekdays">
      <div v-for="(day, index) in weekdays" :key="index">{{ day }}</div>
    </div>
    <div class="days">
      <div
        v-for="(day, index) in days"
        :key="index"
        class="day div"
        :class="{
          today: isToday(day),
          checked: !day.checked,
          empty: !day.date,
          'level-0': day.words === 0 && day.date,
          'level-2': day.words >= 1,
          'level-3': day.words === 3,
          'level-4': day.words === 4,
          'level-5': day.words === 5,
          'level-6': day.words >= 6.
        }"
        @click="toggleCheck(day)"
      >
        <div v-if="day.date" class="day-content">{{ day.date }}</div>
        <div v-else class="day-content">&nbsp;</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'UserCalendar',
  data () {
    return {
      currentDate: new Date(),
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      monthNames: [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
      ],
      weekdays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      wordsData: []
    }
  },
  mounted () {
    this.fetchWordsData()
  },
  computed: {
    // eslint-disable-next-line vue/no-dupe-keys
    days () {
      const daysArray = []
      const daysInCurrentMonth = this.daysInMonth(this.currentMonth, this.currentYear)
      const firstDay = this.firstDayOfMonth(this.currentMonth, this.currentYear)
      const today = new Date()

      // Clear the array before filling it with new days
      daysArray.length = 0

      for (let i = 0; i < firstDay; i++) {
        daysArray.push({ date: null, words: 0, checked: false })
      }

      for (let i = 1; i <= daysInCurrentMonth; i++) {
        let wordsCount = 0
        let checkedStatus = false

        // 判断是否加载后端数据或者使用默认值
        if (this.currentYear < today.getFullYear() ||
            (this.currentYear === today.getFullYear() && this.currentMonth < today.getMonth()) ||
            (this.currentYear === today.getFullYear() && this.currentMonth === today.getMonth() && i <= today.getDate())) {
          const wordDataForDay = this.wordsData.find(data => data.date === i)
          wordsCount = wordDataForDay ? wordDataForDay.words : 3
          checkedStatus = true
        }

        const day = {
          date: i,
          words: wordsCount,
          checked: checkedStatus
        }
        this.updateWordsCount(day)
        daysArray.push(day)
      }
      return daysArray
    }
  },
  methods: {
    async fetchWordsData () {
      try {
        // eslint-disable-next-line no-undef
        const response = await axios.get('your-backend-api-url')
        this.wordsData = response.data
      } catch (error) {
        console.error('Failed to fetch words data:', error)
      }
    },
    daysInMonth (month, year) {
      return new Date(year, month + 1, 0).getDate()
    },
    // Helper methods to calculate days in month and first day of month
    firstDayOfMonth (month, year) {
      return new Date(year, month, 1).getDay()
    },
    prevMonth () {
      if (this.currentMonth === 0) {
        this.currentMonth = 11
        this.currentYear--
      } else {
        this.currentMonth--
      }
      this.fetchWordsData()// 更新月份时获取新的数据
    },
    nextMonth () {
      if (this.currentMonth === 11) {
        this.currentMonth = 0
        this.currentYear++
      } else {
        this.currentMonth++
      }
      this.fetchWordsData()// 更新月份时获取新的数据
    },
    isToday (day) {
      if (!day) return false
      const today = new Date()
      return (
        day.date === today.getDate() &&
        this.currentMonth === today.getMonth() &&
        this.currentYear === today.getFullYear()
      )
    },
    toggleCheck (day) {
      day.checked = !day.checked
    },
    // This function can be customized to update words count based on your logic
    updateWordsCount (day) {
      day.words = Math.floor(Math.random() * 7) // 0 to 3
    }
  }
}
</script>

<style scoped>
.calendar {
  width: 400px;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: hidden;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* background-color: #f0f0f0; */
  background: linear-gradient(rgba(240, 240, 240, 0.5), rgba(240, 240, 240, 0.5)), url('../assets/photo2.png');
  background-size: cover; /* 适应容器大小 */
  background-repeat: no-repeat; /* 禁止重复 */
  background-position: center; /* 居中对齐 */
  padding: 10px;
}

.weekdays, .days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  text-align: center;
}

.weekdays div {
  background-color: #ddd;
  padding: 1px 0;
}

/* .days div {
  padding: 10px 0;
  cursor: pointer;
} */
.days {
  background-color: #fffcfc; /* 将days背景设置为灰色 */
}

.days div {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  padding: 5px;
  margin-top: 5px;   /* 上方间距 */
  margin-bottom: 5px; /* 下方间距 */
  margin: 10px 5px;
  cursor: pointer;
  border-radius: 13px;
  /* color: white; */
}

.day-content {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.days div.today {
  background-color: #87ceeb;
  color: #050000;
  font-weight: bold;
  text-decoration: underline;
}

.days div.checked {
  background-color: #cacec65c; /* Green color for checked days */
}

.days div.empty {
  background-color: #fffcfc;
}

.days div.level-0 {
  background-color: #C0C0C0;
}

.days div.level-1 {
  background-color: #b1f366de
}

.days div.level-2 {
  background-color: #96ed33
}

.days div.level-3 {
  background-color: #7cc924
}

.days div.level-4 {
  background-color: #81bd3d
}

.days div.level-5 {
  background-color: #76ad36
}

.days div.level-6 {
  background-color: #4e870e
}
</style>